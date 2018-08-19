# -*- coding: utf-8 -*-

import socket
import time
# 创建 socket 对象
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置端口号
port = 12345

# 绑定端口号
serversocket.bind(("127.0.0.1", port))
# 设置最大连接数，监听最多10个连接请求
serversocket.listen(10)
print('start Socket Server ...')

while True:
    # 阻塞等待链接，创建套接字clientSocket链接和地址信息addr
    tcpCliSock,addr = serversocket.accept()
    print("从{0}连接上客户端".format(addr))

    while True:
        # 接收客户端数据
        client_data = tcpCliSock.recv(1024).decode("utf8")
        print("服务器端接收消息: ", client_data)

        # 如果客户端输入空格或quit，就退出循环，释放掉客户端连接
        if not client_data or client_data == 'quit' :
            break

        msg = "服务器当前时间={0}".format(time.ctime())
        tcpCliSock.send(msg.encode("utf8"))

    tcpCliSock.close()

# 关闭连接
serversocket.close()



