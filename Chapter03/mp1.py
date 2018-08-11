# -*- coding: utf-8 -*-

from multiprocessing import Process
import os
import time

def handle(name,num):
    for i in range(num):
        print('name={0},i={1},pid={2},ppid={3}'.format(name,i, os.getpid(),os.getppid()))

if __name__ == '__main__':
    p1 = Process(target=handle, args=('python',2))
    p2 = Process(target=handle, args=('java',3))
    p1.start()
    p2.start()
    # 等待当前进程完，在执行主进程
    p1.join()
    p2.join()
    time.sleep(10)
    print('multiprocess end')


