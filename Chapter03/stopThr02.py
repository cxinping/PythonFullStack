# -*- coding: utf-8 -*-

from StopThread import stop_thread
import threading
import time

def run():
    while True:
        print(threading.current_thread().getName(), " --- run ---"   )
        time.sleep(1) #暂停一秒钟

if __name__ == "__main__":
    thr1 = threading.Thread(target=run, args=(), name='thr1')
    thr2 = threading.Thread(target=run,args=(), name='thr2')
    thr1.start()
    thr2.start()

    #3秒钟后停止
    time.sleep(3)
    # 停止t1,thr2 线程
    stop_thread(thr1)
    stop_thread(thr2)
