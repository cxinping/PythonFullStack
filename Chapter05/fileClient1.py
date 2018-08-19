# -*- coding: utf-8 -*-

import socket
import os
import sys

cSocket = socket.socket()
cSocket.connect(('127.0.0.1', 5000))
content = cSocket.recv(1024 * 1024 * 5)  #配置5M缓存
with open('photo3.jpg', 'wb') as file:
    file.write(content)

print('===recv file ok===')

