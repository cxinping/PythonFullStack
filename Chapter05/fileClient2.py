# -*- coding: utf-8 -*-

import socket
import os
import sys

cSocket = socket.socket()
cSocket.connect(('127.0.0.1', 5000))

serverResponse =  cSocket.recv(1024).decode('utf8')
fileTotalSize = int(serverResponse)
print(fileTotalSize,type(fileTotalSize))
#with open('photo3.jpg', 'wb') as file:
#    file.write(content)

print('===recv file ok===')

