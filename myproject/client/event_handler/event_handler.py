import _thread
from threading import Thread

from protocol_modular import DELIMITER, RESPONSE_LOGIN, RESPONSE_CHAT
from protocol_modular.request_protocol import RequestProtocol
from tkinter.messagebox import showinfo

import sys


def clear_inputs(client_obj):
    '''清空登录窗口内容'''
    client_obj.window_login.clear_username_password()


def send_login_data(client_obj):
    '''发送登录消息到服务器并接收响应'''
    # 获取用户名和密码
    userneme = client_obj.window_login.get_username()
    password = client_obj.window_login.get_password()

    # 发送登录数据
    clirent_login_data = RequestProtocol.login_request(userneme, password)
    client_obj.client_socket.send_client_data(clirent_login_data)


def send_chat_data(client_obj):
    message = client_obj.window_chat.get_input()
    client_obj.window_chat.clear_input()

    clirent_chat_data = RequestProtocol.chat_request(client_obj.nickname, message)
    client_obj.client_socket.send_client_data(clirent_chat_data)

    # 添加自己的聊天消息到自己的聊天区
    client_obj.window_chat.append_message('我', message)


def get_respponse_data(client_obj):
    while True:
        response_data = client_obj.client_socket.recv_server_data()
        response_data_handler(client_obj, response_data)


def response_data_handler(client_obj, response_data):
    response_data_list = response_data.split(DELIMITER)
    if response_data_list[0] == RESPONSE_LOGIN:
        if response_data_list[1] == '0':
            showinfo('提示', '用户名或密码错误!')
        elif response_data_list[1] == '1':
            showinfo('提示', '登录成功')
            nickname = response_data_list[2]
            client_obj.nickname = nickname
            client_obj.window_login.withdraw()
            client_obj.window_chat.title('欢迎 %s 进入聊天室~~' % nickname)
            client_obj.window_chat.update()
            client_obj.window_chat.deiconify()

    elif response_data_list[0] == RESPONSE_CHAT:
        nickname = response_data_list[1]
        message = response_data_list[2]
        print('收到聊天响应:昵称--%s,聊天消息--%s' % (nickname, message))
        client_obj.window_chat.append_message(nickname, message)
