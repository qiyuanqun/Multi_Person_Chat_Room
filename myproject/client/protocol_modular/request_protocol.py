from protocol_modular import *

class RequestProtocol(object):

    @staticmethod
    def login_request(username, password):
        return DELIMITER.join([REQUEST_LOGIN, username, password])

    @staticmethod
    def chat_request(nickname, message):
        return DELIMITER.join([REQUEST_CHAT, nickname, message])