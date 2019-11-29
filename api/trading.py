import sys
import time
import logging, random
import quickfix as fix
import quickfix44 as fix44

class FixTrading(fix.Application):
    def __init__(self):
        super(FixTrading, self).__init__()
        pass
    
    def onCreate(self, sessionID): 
		pass

    def onLogon(self, sessionID): 
        pass
    
    def onLogout(self, sessionID):
        pass

    def toAdmin(self, sessionID, message):
        pass

    def fromAdmin(self, sessionID, message):
        pass

    def toApp(self, sessionID, message):
        pass
    
    def fromApp(self, message, sessionID):
        pass
