# -*- coding: utf-8 -*-

import socket
import threading        # 使用多线程

sSocket = socket.socket()
sSocket.bind(('127.0.0.1', 5000))
sSocket.listen(10)
cSocket, addr = sSocket.accept()

def sendMsg():
    while True:
        # print('msg')
        msg = input('\ninput your message to client:')
        msg_bytes = msg.encode('utf-8')
        cSocket.send(msg_bytes)
        print('%s\t%s' % ('msg', msg))

def recvMsg():
    while True:
        msg_bytes = cSocket.recv(1024)
        msg = msg_bytes.decode('utf-8')
        print('%s\t%s' % ('msg', msg))

if __name__ == '__main__':
    t1 = threading.Thread(target=recvMsg, args=(), name='recv_thread')
    t2 = threading.Thread(target=sendMsg, args=(), name='send_thread')
    t1.start()
    t2.start()
