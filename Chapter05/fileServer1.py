# -*- coding: utf-8 -*-

import socket

sSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sSocket.bind(('127.0.0.1', 5000))
sSocket.listen(10)

while True:
    cSocket, addr = sSocket.accept()
    with open('photo.jpg', 'rb') as file:
        # 一次性读取整个文件
        content = file.read()
        cSocket.send(content)
    print('===send file ok===')

