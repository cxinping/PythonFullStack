# -*- coding: utf-8 -*-

import socket

cSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cSocket.connect(('127.0.0.1', 5000))
# 配置5M缓存
content = cSocket.recv(1024 * 1024 * 5)
#content = cSocket.recv(1024 * 50 )

with open('photo2.jpg', 'wb') as file:
    file.write(content)

print('===recv file ok===')

