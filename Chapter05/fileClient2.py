# -*- coding: utf-8 -*-

import socket
import os

cSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cSocket.connect(('127.0.0.1', 5000))

# Step1： 获得接收文件的大小
serverResponse =  cSocket.recv(1024).decode('utf8')
fileTotalSize = int(serverResponse)
print("fileTotalSize={0}".format(fileTotalSize))
# Step2：发送确认信息
cSocket.send("ready to recv file".encode("utf8"))
# 初始化接收大小
revivedSize = 0
fileName = 'photo3.jpg'
with open(fileName, 'wb') as file:
    # Step3： 判断是否已经接收完文件，对接收文件大小和接收文件总大小进行比较
    while revivedSize < fileTotalSize:
        # 配置5KB 缓存
        data = cSocket.recv(1024 * 50)
        # 接收文件大小
        revivedSize = revivedSize + len(data)
        #print("revivedSize={0},data={1}".format(revivedSize,len(data)) )
        file.write(data)
    else:
        print("fileTotalSize={0},revivedSize={1}".format(fileTotalSize, revivedSize))
print('===recv file ok===')

