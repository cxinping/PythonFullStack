# -*- coding: utf-8 -*-

from multiprocessing import Process, Queue

def putData(queue):
    queue.put("java")
    queue.put("python")
    queue.put("c++")

if __name__ == '__main__':
    queue = Queue() # 创建队列queue
    process = Process(target=putData, args=(queue,)) # 创建一个进程
    process.start()
    print(queue.get())
    print(queue.get())
    print(queue.get())
    process.join()