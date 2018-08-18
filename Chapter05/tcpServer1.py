# -*- coding: utf-8 -*-

from socket import socket

socket1 = socket()
#print(socket1)
port = 12345
socket1.bind(("127.0.0.1", port) )

# 设置最大连接数
socket1.listen(10)

while True:
    # 建立客户端连接
    clientSocket,addr  = socket1.accept()
    print("新连接:",addr )
    msg = 'socket test'

    print('start Socket Server ...')
    clientSocket.send(msg.encode('utf'))
    clientSocket.close()
    #socket1.close()

