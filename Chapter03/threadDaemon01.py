# -*- coding: utf-8 -*-

import threading, time

def run(taskName):
    print("任务:", taskName)
    time.sleep(2)
    print("{0} 任务执行完毕".format(taskName))  # 查看每个子线程

if __name__ == '__main__':
    start_time = time.time()
    for i in range(3):
        thr = threading.Thread(target=run, args=("task-{0}".format(i),))
        thr.start()

    # 查看主线程和当前活动的所有线程数
    print("{0}线程结束，当线程数量={1}".format( threading.current_thread().getName(), threading.active_count()))
    print("消耗时间:", time.time() - start_time)