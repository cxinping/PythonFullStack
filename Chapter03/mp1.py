# -*- coding: utf-8 -*-

from multiprocessing import Process
import os

def handle(name):
    print('name={0},pid={1},ppid={2}'.format(name, os.getpid(),os.getppid()))

if __name__ == '__main__':
    p1 = Process(target=handle, args=('python',))
    p2 = Process(target=handle, args=('java',))
    p1.start()
    p2.start()
    # 等待当前进程完，在执行主进程
    p1.join()
    p2.join()
    print('multiprocess end')

