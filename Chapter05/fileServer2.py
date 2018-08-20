# -*- coding: utf-8 -*-

import socket
import os

sSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sSocket.bind(('127.0.0.1', 5000))
sSocket.listen(10)

fileName = 'photo.jpg'
while True:
    cSocket, addr = sSocket.accept()
    with open(fileName, 'rb') as file:
        # Step1： 获取文件大小
        fileSize = os.stat(fileName).st_size
        # Step2： 发送文件大小给客户端
        cSocket.send(str(fileSize).encode("utf8"))
        # Step3: 等待客户端确认
        data = cSocket.recv(1024).decode("utf8")
        # Step4: 通过文件迭代器遍历文件，边读文件边发送数据
        for line in file:
            cSocket.send(line)
            print("send data length=>{0}".format(len(line)))

    print('===send file ok===')

