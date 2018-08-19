# -*- coding: utf-8 -*-

import socket

sSocket = socket.socket()
sSocket.bind(('127.0.0.1', 5000))
sSocket.listen(10)

while True:
    cSocket, addr = sSocket.accept()
    with open('photo.jpg', 'rb') as file:
        content = file.read()
        cSocket.send(content)
    print('===send file ok===')

