# -*- coding: utf-8 -*-

import socket
import os
sSocket = socket.socket()
sSocket.bind(('127.0.0.1', 5000))
sSocket.listen(10)

fileName = 'photo.jpg'
while True:
    cSocket, addr = sSocket.accept()
    with open('photo.jpg', 'rb') as file:
        fileSize = os.stat(fileName).st_size  # 获取文件大小
        cSocket.send(str(fileSize).encode("utf8"))
        #content = file.read()
        #cSocket.send(content)
        for line in file:
            print(line)
    print('===send file ok===')

