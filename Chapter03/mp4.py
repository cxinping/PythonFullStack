# -*- coding: utf-8 -*-

from multiprocessing import Queue,Process
import random,time

#写数据进程执行的代码
def wirteQueue(queue):
    print('写入队列开始')
    for i in range(5) :
        print("写入数据={0}".format(i))
        queue.put(str(i))
        time.sleep(random.random() * 5)
    print("写入队列结束")

#读数据进程执行的代码
def readQueue(queue):
    print('读取队列')
    while True:
        print("读取队列的数据={0}".format(queue.get()))

if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程
    q = Queue()
    pw = Process(target=wirteQueue,args=(q,))
    pr = Process(target=readQueue,args=(q,))
    # 启动子进程pw，写入数据
    pw.start()
    # 启动子进程pr，读取数据
    pr.start()
    # 等待pw进程结束
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止
    pr.terminate()
    print("==== main thread ===")



