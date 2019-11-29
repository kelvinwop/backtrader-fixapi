import sys
import time
import logging, random
import quickfix as fix
import quickfix44 as fix44

from helpers.fix_helpers import parse_fix_message, extract_header_field_value, extract_message_field_value

class FixPricing(fix.Application):
	"""FIX class for getting price info from the server."""

	def __init__(self, 	session, username, password, 
				 client_str = '[CLIENT (FIX API V4.4)]', 
				 server_str = '[SERVER (FIX API V4.4)]'):
		"""Constructor for Fix Pricing Class
		
		Arguments:
			session {Object} -- Fix Session Object
			username {str} -- User identification info
			password {str} -- User authentication info
		
		Keyword Arguments:
			client_str {str} -- Prefix message for Client messages (default: {'[CLIENT (FIX API V4.4)]'})
			server_str {str} -- Prefix message for Server messages (default: {'[SERVER (FIX API V4.4)]'})
		"""
		super(FixPricing, self).__init__()
		self.logger = logging.getLogger(self.__class__.__base__)
		self.session = session
		self.connected = False

		self.username = username
		self.password = password

		self._client_str = client_str
		self._server_str = server_str
	
	def onCreate(self, sessionID): 
		"""Called the App is initialized
		
		Arguments:
			sessionID {object} -- Session identifier object
		"""
		self.sessionID = sessionID
		self.logger = logging.getLogger(f'{self.__class__.__name__}({sessionID})')
		self.logger.info(f'[KERNEL] Application created with the sessionID: {self.sessionID.toString()}')
		
	def onLogon(self, sessionID): 
		"""Called after session login.
		
		Arguments:
			sessionID {object} -- Session identifier object
		"""
		self.logger.info('[KERNEL] Logon.')
		self.connected = True
		print(f'{self._client_str} Login complete successfully!')
	
	def onLogout(self, sessionID):
		"""	Called on session logout.

		
		Arguments:
			sessionID {object} -- Session identifier object
		"""
		self.logger.info('[KERNEL] Logout.')
		self.connected = False
		print(f'{self._client_str} Logout complete!')

	def onMessage(self, message, sessionID):
		"""Prints out the received message.
		
		Arguments:
			message {object} -- message object
			sessionID {object} -- Session identifier object
		"""
		self.logger.info(f'[KERNEL] Message: {parse_fix_message(message)}')
		print(f'[KERNEL] [onMessage] {parse_fix_message(message)}')
		
	def toAdmin(self, message, sessionID):
		"""Get all the session level messages before they are sent to the FIX server.
		This includes Logon, Logout, Heartbeat etc.
		
		Arguments:
			message {object} -- message object
			sessionID {object} -- Session identifier object
		"""

		self.logger.info(f'[KERNEL] Sending the admin message: {parse_fix_message(message)}')

		msgType = fix.MsgType()
		message.getHeader().getField(msgType)

		if msgType.getValue() == fix.MsgType_Logon:
			print(f'{self._client_str} Sending Logon request.')

			message.setField(fix.Username(self.username))
			message.setField(fix.Password(self.password))

		elif msgType.getValue() == fix.MsgType_Logout:
			print(f'{self._client_str} Sending Logout request.')

		elif msgType.getValue() == fix.MsgType_Heartbeat:
			print(f'{self._client_str} Heartbeart!')

		else:
			print(f'[KERNEL] [toAdmin] {parse_fix_message(message)}')
			
	def fromAdmin(self, sessionID, message):
		"""Get all the session level messages from the Admin.
		This includes Logon, Logout, Heartbeat etc.
		QuickFix handles and processes them automatically.

		Arguments:
			message {object} -- message object
			sessionID {object} -- Session identifier object
		"""
		self.logger.info(f'[KERNEL] Received the admin message: {parse_fix_message(message)}')

		msgType = fix.MsgType()
		message.getHeader().getField(msgType)

		if msgType.getValue() == fix.MsgType_Logon:
			print(f'{self._client_str} Logon success!.')

		elif msgType.getValue() == fix.MsgType_Logout:
			print(f'{self._client_str} Logout success!.')

		elif msgType.getValue() == fix.MsgType_Heartbeat:
			print(f'{self._client_str} Heartbeart sucess!')

		else:
			print(f'[KERNEL] [fromAdmin] {parse_fix_message(message)}')
			
	def toApp(self, sessionID, message):
		"""Process the App level messages before sending.
		
		Arguments:
			message {object} -- message object
			sessionID {object} -- Session identifier object
		"""
		self.logger.info(f'[KERNEL] Sending app message: {parse_fix_message(message)}')
		print(f'[KERNEL] [toApp] {parse_fix_message(message)}')
	
	def fromApp(self, message, sessionID):
		"""Process incoming App level messages.
		
		Arguments:
			message {object} -- message object
			sessionID {object} -- Session identifier object
		"""
		self.logger.info(f'[KERNEL] Received app message: {parse_fix_message(message)}')

		msgType = fix.MsgType()
		message.getHeader().getField(msgType)
		msgType = msgType.getValue()

		timestamp = fix.SendingTime()
		message.getHeader().getField(timestamp)
		timestamp = timestamp.getString()

		if msgType == fix.MsgType_MassQuote:
			print(f'{self._server_str} MassQuote.')

			# NoQuoteSets_Group = fix44.MassQuote.NoQuoteSets()

			# message.getGroup(1, NoQuoteSets_Group)
			# reqID = extract_message_field_value(fix.QuoteSetID(), NoQuoteSets_Group)

			# NoQuoteEntries_Group = fix44.MassQuote.NoQuoteSets.NoQuoteEntries()
			# NoQuoteSets_Group.getGroup(1, NoQuoteEntries_Group)

			if message.isSetField(fix.QuoteID()):
				self.send_MassQuoteAcknowledgement(message)
	
	def send_MassQuoteAcknowledgement(self, message):
		"""Send the Ack for the received MassQuote.
		
		Arguments:
			message {object} -- message object
		"""
		quoteID = extract_message_field_value(fix.QuoteID(), message)

		message = fix.Message()
		header = message.getHeader()
		header.setField(fix.MsgType(fix.MsgType_MassQuoteAcknowledgement))
		message.setField(fix.QuoteID(quoteID))

		self.session.sendToTarget(message, self.sessionID)