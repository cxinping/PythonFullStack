# -*- coding: utf-8 -*-

import socket
import os
import sys

cSocket = socket.socket()
cSocket.connect(('127.0.0.1', 5000))

# Step1： 获得接收文件的大小
serverResponse =  cSocket.recv(1024).decode('utf8')
fileTotalSize = int(serverResponse)
print(fileTotalSize,type(fileTotalSize))
# Step2：发送确认信息
cSocket.send("ready to recv file".encode("utf8"))
# 初始化接收大小
revivedSize = 0
fileName = 'photo3.jpg'
with open(fileName, 'wb') as file:
#    file.write(content)
    count = 0
    # 判断接收大小和文件大小比较
    while revivedSize < fileTotalSize:
        # 配置1M缓存
        data = cSocket.recv(1024 * 1024)
        # 接收文件大小
        revivedSize = revivedSize + len(data)
        print("revivedSize={0},count={1}，data={2}".format(revivedSize,count,len(data)) )
        count = count + 1
        file.write(data)
    else:
        pass
print('===recv file ok===')

