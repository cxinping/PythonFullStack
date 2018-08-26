# -*- coding: utf-8 -*-

import socket

HostPort = ('127.0.0.1',7777)
#创建UDP套接字
udpSerSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#服务器端绑定端口
udpSerSock.bind(HostPort)

while True:
    # 接收数据和端口
    data,addr = udpSerSock.recvfrom(1024)
    # 打印数据
    print("服务器 接收消息：",data.decode('utf8'))
    sendMsg = "hello {0}".format(data.decode('utf8'))
    udpSerSock.sendto(sendMsg.encode("utf8") , addr)