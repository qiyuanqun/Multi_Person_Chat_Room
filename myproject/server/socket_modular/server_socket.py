import socket
from socket_modular import SERVER_IP, SERVER_PORT


class ServerSocket(socket.socket):
    '''自定义客户端套接字'''

    def __init__(self):
        '''初始化套接字'''
        # TCP类型
        super(ServerSocket, self).__init__(socket.AF_INET, socket.SOCK_STREAM)
        self.bind((SERVER_IP, SERVER_PORT))
        self.listen(128)