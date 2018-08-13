# -*- coding: utf-8 -*-

import threading
import time,random,math

# i 循环次数
def printNum(idx):
    for num in range(idx +1):
        print("{0}\tnum={1}".format(threading.current_thread().getName(), num) )
        delay = math.ceil(random.random() * 2)
        time.sleep(delay)

if __name__ == '__main__':
    t1 = threading.Thread(target=printNum, args=(2,),name="thread1" )
    t2 = threading.Thread(target=printNum, args=(3,),name="thread2")
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("{0} 线程结束".format(threading.current_thread().getName()))
