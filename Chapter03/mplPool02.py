# -*- coding: utf-8 -*-

from multiprocessing import Pool
import os, time, random

def worker(msg):
    t_start = time.time()
    print("任务 %s开始执行,进程号为%d" % (msg, os.getpid()))
    # random.random()随机生成0~1之间的浮点数
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print( "任务 %s， 执行完毕， 耗时%0.2f 秒" % (msg, (t_stop - t_start)))

if __name__ == '__main__':
    print('父进程 %d.' % os.getpid())
    pool = Pool(3)  # 定义一个进程池， 最大进程数为3
    for i in range(0, 5):
        # Pool.apply(要调用的目标,(传递给目标的参数元组,))
        #  使用阻塞式式调用worker函数
        pool.apply(worker, (i,))

    pool.close()  # 关闭进程池， 关闭后pool不再接收新的请求
    pool.join()  # 等待pool中所有⼦进程执⾏完成， 必须放在close语句之后


