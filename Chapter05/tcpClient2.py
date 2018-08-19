# -*- coding: utf-8 -*-

import socket

# 创建 socket 对象
tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置端口号
port = 12345

# 连接服务，指定主机和端口
tcpCliSock.connect(("127.0.0.1", port))
print('start Socket client ...')

while True:
    data = input("请在客户端输入发送的内容：")

    if not data :
        break
    tcpCliSock.send(data.encode("utf8"))
    client_data = tcpCliSock.recv(1024)
    if not client_data:
        break

    print("客户端接收的消息为：",client_data.decode("utf8"))

# 关闭连接
tcpCliSock.close()