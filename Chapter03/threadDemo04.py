# -*- coding: utf-8 -*-

import threading

balance = 100
lock = threading.Lock()

def change(num, counter):
    global balance
    for i in range(counter):
        # 先要获取锁
        lock.acquire()
        balance += num
        balance -= num
        # 释放锁
        lock.release()
        
        if balance != 100:
            # 如果输出这句话，说明线程不安全
            print("balance=%d" % balance)
            break

if __name__ == "__main__":
    thr1 = threading.Thread(target=change,args=(100,500000),name='t1')
    thr2 = threading.Thread(target=change,args=(100,500000),name='t2')
    thr1.start()
    thr2.start()
    thr1.join()
    thr2.join()
    print("{0} 线程结束".format(threading.current_thread().getName()))