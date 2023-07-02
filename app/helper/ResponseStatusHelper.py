ERROR_CODE1 = '0000'

# Put all the response messages here
def message(code):
    message_dict = {
        ERROR_CODE1: 'ERROR CODE 1 FOR calling',
    }
    return message_dict[code]