# -*- coding: utf-8 -*-

import threading
import time,random,math

# idx 循环次数
def printNum(idx):
    for num in range(idx ):
        print("{0}\tnum={1}".format(threading.current_thread().getName(), num) )
        delay = math.ceil(random.random() * 2)
        time.sleep(delay)

if __name__ == '__main__':
    th1 = threading.Thread(target=printNum, args=(2,),name="thread1"  )
    th2 = threading.Thread(target=printNum, args=(3,),name="thread2" )
    # 启动线程
    th1.start()
    th2.start()
    # 等待至线程中止
    th1.join()
    th2.join()
    print("{0} 线程结束".format(threading.current_thread().getName()))
