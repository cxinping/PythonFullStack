# -*- coding: utf-8 -*-

import socket
HostPort = ('127.0.0.1',7777)
#创建UDP套接字
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#服务器端绑定端口
sock.bind(HostPort)

while True:
    # 接收端口数据
    data,addr = sock.recvfrom(1024)
    # 打印数据
    print("接收消息：",data.decode('utf8'))
