# -*- coding: utf-8 -*-

import socket

# 创建一个服务器端的 socket 对象
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置端口号
port = 12345

# 绑定端口号
serversocket.bind(("127.0.0.1", port))

# 设置最大连接数，超过后排队
serversocket.listen(10)
print('start Socket Server ...')

while True:
    # 建立客户端连接
    clientSocket,addr  = serversocket.accept()
    #print("新连接:",addr )
    msg = '成功连接到服务器 socket message'

    clientSocket.send(msg.encode('utf8'))
    clientSocket.close()

# 关闭连接
serversocket.close()

