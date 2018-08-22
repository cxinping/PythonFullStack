# -*- coding: utf-8 -*-

import threading
import time

class TestThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        # 设置停止的标志位
        self._running = True

    def terminate(self):
        self._running = False

    def run(self):
        count = 1
        threadName = threading.current_thread().getName()
        while self._running:
            print("threadName={0},count={1}".format(threadName,count))
            count = count + 1
            time.sleep(1)  # 暂停一秒钟

if __name__ == "__main__":
    thr1 = TestThread()
    thr1.start()
    #3秒钟后停止
    time.sleep(3)

    # 停止thr1 线程
    thr1.terminate()

    print("主线程结束")