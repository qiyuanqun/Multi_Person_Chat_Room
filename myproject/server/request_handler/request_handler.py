from protocol_modular import DELIMITER, REQUEST_LOGIN, REQUEST_CHAT
from protocol_modular.response_protocol import ResponseProtocol


def client_handler(server_obj, client_socket, addr):
    '''为客户端服务'''
    while True:
        print('正在接收客户端：%s 发来的数据' % str(addr))

        # 获取客户端请求数据
        client_request_data = client_socket.recv(1024)
        if not client_request_data:
            if server_obj.online_user:
                wait_del_username = None

                # 注意，可迭代对象在迭代过程中不能改变其尺寸大小，即不能增加或删除，只能修改
                for username, info in server_obj.online_user.items():
                    if info['sock'] == client_socket:
                        wait_del_username = username
                del server_obj.online_user[wait_del_username]
            client_socket.close()
            print('客户端： %s 断开连接' % str(addr))
            break
        client_request_data = client_request_data.decode('utf-8')
        print('接收到客户端 %s 发来的数据：%s' % (str(addr),client_request_data))

        # 解析数据并调用相应处理函数
        client_request_data_list = client_request_data.split(DELIMITER)
        if client_request_data_list[0] == REQUEST_LOGIN:
            request_login_handler(server_obj, client_socket, client_request_data_list)
        elif client_request_data_list[0] == REQUEST_CHAT:
            request_chat_handler(server_obj, client_socket, client_request_data_list)


def request_login_handler(server_obj, cli_soc, client_login_request_data_list):
    '''处理登录请求'''
    username = client_login_request_data_list[1]  # 用户名
    password = client_login_request_data_list[2]  # 密码

    sql = "select * from user where username='%s' and password='%s'" % (username, password)
    result = server_obj.db.get_one(sql)
    print('从数据库中查询到的用户数据:',result)
    if result:
        is_login = '1'
        nickname = result['nickname']

        server_obj.online_user[username] = {'sock': cli_soc}
        print('在线用户:',server_obj.online_user.keys())
    else:
        is_login = '0'
        nickname = ''

    # 发送登录响应
    response_str = ResponseProtocol.login_response(is_login, nickname)
    cli_soc.send(response_str.encode('utf-8'))


def request_chat_handler(server_obj, cli_soc, client_chat_request_data_list):
    '''处理聊天请求'''
    # 向在线用户转发消息
    for user, info in server_obj.online_user.items():
        if info['sock'] != cli_soc:
            nickname = client_chat_request_data_list[1]
            message = client_chat_request_data_list[2]
            response_str = ResponseProtocol.chat_response(nickname, message)
            info['sock'].send(response_str.encode('utf-8'))
