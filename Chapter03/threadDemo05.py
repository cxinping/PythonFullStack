# -*- coding: utf-8 -*-

import threading
import time,random,math

# 本地线程变量——全局变量
local = threading.local()

def loop():
    local.num = 0
    for i in range(3):
        local.num += 1
        print('threadName=%s num=%d' % (threading.current_thread().getName(), local.num))
        delay = math.ceil(random.random() * 3)
        time.sleep(delay)

if __name__ == '__main__':
    thr1 = threading.Thread(target=loop, args=(), name='t1')
    thr2 = threading.Thread(target=loop, args=(), name='t2')
    thr1.start()
    thr2.start()
    thr1.join()
    thr2.join()
    print('=== main end===')
