# -*- coding: utf-8 -*-

import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345

socket.connect(("127.0.0.1", port))
print('start Socket client ...')
msg = socket.recv(1014).decode('utf-8')
print("client receive message={0}".format(msg))
socket.close()


