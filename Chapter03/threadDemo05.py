# -*- coding: utf-8 -*-

import threading

v1 = 0  # 全局变量
v2 = threading.local()# 本地线程变量——全局变量

def f1():
    global v1
    v3 = 100
    for i in range(100):
        v1 += 1
        print('threadName: %s\tv1 = %d' %
(threading.current_thread().getName(), v1))

def f2():
    global v1
    v3 = 100
    v2.v1 = 0
    for i in range(100):
        v2.v1 += 1
        print('threadName: %s\tv1 = %d' %
(threading.current_thread().getName(), v2.v1))

if __name__ == '__main__':
    # f1()
    # print(v1)
    # print(v2)       # v2可访问，即全局变量
    # print(v3)     # 报错，局部变量

    t1 = threading.Thread(target=f1, args=(), name='t1')
    t2 = threading.Thread(target=f2, args=(), name='t2')

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print('===end===')
