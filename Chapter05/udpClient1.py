# -*- coding: utf-8 -*-

import socket
HostPort = ('127.0.0.1',7777)
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    user_input = input('请输入要发送给对方的消息：')
    if user_input == 'quit':
        break
    # 指定地址端口发送数据，数据必须encode
    sock.sendto(user_input.encode('utf8'),HostPort)
sock.close()
