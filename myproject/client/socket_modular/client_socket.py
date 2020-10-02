import socket
from socket_modular import *


class ClientSocket(socket.socket):
    '''自定义客户端套接字'''

    def __init__(self):
        '''初始化套接字'''
        # TCP类型
        super(ClientSocket, self).__init__(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        super().connect((SERVER_IP, SERVER_PORT))

    def recv_server_data(self):
        '''接收数据并自动转换为字符串返回'''
        return self.recv(1024).decode('utf-8')

    def send_client_data(self, message):
        '''接收一个数据，并转换为字节数据发送'''
        return self.send(message.encode('utf-8'))