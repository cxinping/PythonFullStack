# -*- coding: utf-8 -*-

import socket

# 创建 socket 对象
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置端口号
port = 12345

# 连接服务，指定主机和端口
socket.connect(("127.0.0.1", port))
print('start Socket client ...')

# 接收消息，接收小于 1024 字节的数据
msg = socket.recv(1024).decode('utf8')
print("client receive message={0}".format(msg))

# 关闭连接
socket.close()


