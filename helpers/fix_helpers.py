
def parse_fix_message(message):
    """Get fix message from the mesage object
    
    Arguments:
        message {object} -- FIX message object
    """
    return message.toString().replace('\x01', ' ')


def extract_message_field_value(_FIX_API_Object, message):
    if message.isSetField(_FIX_API_Object.getField()):
        message.getField(_FIX_API_Object)
        return _FIX_API_Object.getValue()
    else:
        return None


def extract_header_field_value(_FIX_API_Object, message):
    if message.getHeader().isSetField(_FIX_API_Object.getField()):
        message.getField(_FIX_API_Object)
        return _FIX_API_Object.getValue()
    else:
        return None
