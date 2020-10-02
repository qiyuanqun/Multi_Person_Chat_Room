from database_modular.db import DB
from request_handler.request_handler import client_handler, request_login_handler, request_chat_handler
from socket_modular.server_socket import ServerSocket
from threading import Thread
from protocol_modular import REQUEST_LOGIN, REQUEST_CHAT


class Server(object):
    '''服务器类'''

    def __init__(self):
        self.server_socket = ServerSocket()  # 创建服务器套接字
        self.db = DB()  # 创建数据库对象
        self.online_user = dict()

    def startup(self):
        '''开启服务器'''
        while True:
            print('正在获取客户端连接~~')
            new_client_socket, addr = self.server_socket.accept()
            print('获取到客户端连接~~:', str(addr))

            # 开启线程单独为每个客户端服务
            Thread(target=client_handler, args=(self, new_client_socket, addr)).start()


if __name__ == '__main__':
    Server().startup()