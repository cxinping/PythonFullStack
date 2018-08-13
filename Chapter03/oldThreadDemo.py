# -*- coding: utf-8 -*-

import _thread
import time

# 参数依次为：threadNum 是线程名字，i是 循环多少次，锁对象
def printNum(threadNum, i,lock):
    for num in range(i ):
        print("{0}\tnum={1}".format(threadNum, num) )
        time.sleep(1)
    # 释放锁
    lock.release()

# 线程循环次数
loops =[2,2,3]

def main():
    print("开始多线程 ", time.ctime())
    locks = []
    nloops = range(len(loops))

    for i in nloops:
        # 分配锁对象
        lock = _thread.allocate_lock()
        # 获取锁对象
        lock.acquire()
        locks.append(lock)

    for i in nloops:
        threadName = "thread-{0}".format(i)
        index = loops[i]
        print("-- 线程名字={0},循环次数={1}".format(threadName, index))
        _thread.start_new_thread(printNum, (threadName, index, locks[i]))

    # 等待所有锁被释放
    for i in nloops:
        while(locks[i].locked()):
            pass
    print("线程结束", time.ctime())

if __name__ == "__main__" :
    main()
   