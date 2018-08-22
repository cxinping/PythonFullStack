# -*- coding: utf-8 -*-

import socket
import threading        # 使用多线程模块

def main():
    # 创建socket对象。调用socket构造函数
    sSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 将socket绑定到指定地址，第一个参数为ip地址，第二个参数为端口号
    sSocket.bind(('127.0.0.1', 5000))
    # 设置最多连接数量
    sSocket.listen(10)
    print('开始启动服务器 ...')

    while True:
        # 服务器套接字通过socket的accept方法等待客户请求一个连接
        cSocket, address = sSocket.accept()
        print("客户端{0} 连接到服务器".format(address))
        thr1 = threading.Thread(target=recvMsg, args=(cSocket, address))
        thr1.start()

def recvMsg(cSocket,addr):
    while True:
        msg_bytes = cSocket.recv(1024)
        msg = msg_bytes.decode('utf8')
        print('从{0}客户端收到消息：{1}'.format(addr,msg) )
        if not msg or  msg == "exit":
            print("关闭客户端{0}连接".format(addr))
            cSocket.close()
            break

        # 将接收到的信息原样的返回到客户端中
        cSocket.send(msg_bytes)

if __name__ == '__main__':
    main()