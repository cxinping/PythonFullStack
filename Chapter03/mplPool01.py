from multiprocessing import Pool
import os, time, random

def worker(msg):
    t_start = time.time()
    print("任务 %s开始执行,进程号为%d" % (msg, os.getpid()))
    # random.random()随机生成0~1之间的浮点数
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print( "任务 %s，执行完毕，耗时%0.2f 秒" % (msg, (t_stop - t_start)))

if __name__ == '__main__':
    print('⽗进程 %d.' % os.getpid())
    pool = Pool(3)  # 定义1个进程池，最大进程数是3
    for i in range(0, 5):
        # Pool.apply_async(要调⽤的⽬标,(传递给⽬标的参数元祖,))
        # 每次循环将会用空闲出来的子进程去调用目标
		pool.apply_async(worker, (i,))

     pool.close()  # 关闭进程池，关闭后进程池后就不再添加新的进程
     pool.join()  # 等待pool中所有子进程执行完成，必须放在close语句之后
