# -*- coding: utf-8 -*-

import threading
import socket
import os
import sys

cSocket = socket.socket()
cSocket.connect(('127.0.0.1', 5000))
msg = ' '

def recvMsg():
    global msg
    while msg:
        msg_bytes = cSocket.recv(1024)
        msg = msg_bytes.decode('utf-8')
        if msg != 'exit!':
            print('\n%s\t%s' % ('msg:', msg))

def sendMsg():
    global msg
    while msg:
        # print('msg')
        msg = input('请输入要发送给对方的消息：')
        msg_bytes = msg.encode('utf-8')
        cSocket.send(msg_bytes)

if __name__ == '__main__':
    t1 = threading.Thread(target=recvMsg, args=(), name='recv_thread')
    t2 = threading.Thread(target=sendMsg, args=(), name='send_thread')
    t1.start()
    t2.start()
