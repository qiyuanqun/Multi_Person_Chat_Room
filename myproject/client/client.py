import sys
from threading import Thread

from event_handler.event_handler import clear_inputs, send_login_data, send_chat_data, get_respponse_data
from gui_modular.windowlogin import WindowLogin
from gui_modular.window_chat import WindowChat
from socket_modular.client_socket import ClientSocket


class Client(object):
    '''客户端类'''

    def __init__(self):
        '''客户端初始化'''
        self.client_socket = ClientSocket()

        self.window_login = WindowLogin()
        self.window_chat = WindowChat()
        self.window_chat.withdraw()  # 隐藏窗口

        self.window_login.on_reset_button_click(lambda: clear_inputs(self))
        self.window_login.on_login_button_click(lambda: send_login_data(self))
        self.window_login.on_window_close(self.exit)

        self.window_chat.on_send_button_click(lambda: send_chat_data(self))
        self.window_chat.on_window_close(self.exit)

        self.running = True

    def startup(self):
        '''客户端开启'''
        self.client_socket.connect()
        # 单独开启线程负责接收
        t = Thread(target=get_respponse_data, args=(self,))
        t.setDaemon(True)
        t.start()
        self.window_login.mainloop()

    def exit(self):
        self.running = False
        self.client_socket.close()
        sys.exit(0)


if __name__ == '__main__':
    Client().startup()