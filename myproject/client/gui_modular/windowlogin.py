from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import Frame
from tkinter import Button
from tkinter import LEFT
from tkinter import END


class WindowLogin(Tk):
    '''登录窗口类'''

    def __init__(self):
        '''初始化登录窗口'''
        super(WindowLogin, self).__init__()
        self.attribute_init()
        self.widgets_init()

    def  attribute_init(self):
        '''窗口属性初始化'''
        # 设置窗口标题
        self.title('登录窗口')
        # 设置窗口不能被拉伸
        self.resizable(False, False)
        # 窗口大小
        window_width = 255
        window_height = 95
        # 屏幕宽高
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        # 窗口位置
        pos_x = (screen_width - window_width) / 2
        pos_y = (screen_height - window_height) / 2
        # 设置窗口大小和位置  '宽x高+X+Y'
        self.geometry('%dx%d+%d+%d' % (window_width, window_height, pos_x, pos_y))

    def widgets_init(self):
        '''窗口控件初始化'''
        # 用户名
        username_label = Label(self)
        username_label['text'] = '用户名:'
        username_label.grid(row=0, column=0, padx=10, pady=5)
        username_entry = Entry(self, name='username_entry')
        username_entry['width'] = 25
        username_entry.grid(row=0, column=1)

        # 密码
        password_label = Label(self)
        password_label['text'] = '密   码:'
        password_label.grid(row=1, column=0)
        password_entry = Entry(self, name='password_entry')
        password_entry['width'] = 25
        password_entry.grid(row=1, column=1)
        password_entry['show'] = '*'

        # 按钮区
        button_frame = Frame(self, name='button_frame')
        # 重置按钮
        reset_button = Button(button_frame, name='reset_button')
        reset_button['text'] = '重置'
        reset_button.pack(side=LEFT, padx=20)
        # 登录按钮
        login_button = Button(button_frame, name='login_button')
        login_button['text'] = '登录'
        login_button.pack(side=LEFT)
        button_frame.grid(row=2, columnspan=2, pady=5)

    # 以下是登录窗口类提供的一些操作处理方法，但不在该模块调用，该模块只负责显示登录窗口
    def get_username(self):
        '''获取用户名'''
        return self.children['username_entry'].get()

    def get_password(self):
        '''获取密码'''
        return self.children['password_entry'].get()

    def clear_username_password(self):
        '''清空用户名和密码'''
        self.children['username_entry'].delete(0, END)
        self.children['password_entry'].delete(0, END)

    def on_reset_button_click(self, command):
        '''重置按钮响应注册'''
        reset_button = self.children['button_frame'].children['reset_button']
        reset_button['command'] = command

    def on_login_button_click(self, command):
        '''登录按钮响应注册'''
        login_button = self.children['button_frame'].children['login_button']
        login_button['command'] = command

    def on_window_close(self, command):
        '''关闭窗口的响应注册'''
        self.protocol('WM_DELETE_WINDOW', command)


if __name__ == '__main__':
    WindowLogin().mainloop()