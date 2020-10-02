from protocol_modular import DELIMITER, RESPONSE_LOGIN, RESPONSE_CHAT

class ResponseProtocol(object):
    '''服务器响应协议的格式字符串处理'''

    @staticmethod
    def login_response(is_login, nickname):
        return DELIMITER.join([RESPONSE_LOGIN, is_login, nickname])

    @staticmethod
    def chat_response(nickname, messages):
        return DELIMITER.join([RESPONSE_CHAT, nickname, messages])