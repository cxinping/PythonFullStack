# -*- coding: utf-8 -*-

import psutil
import time
import CpuDao as cpuDao

def monitorCpu():
    # 通过循环，对系统进行监控
    while True:
        # 获取系统cpu使用率（每隔1秒）
        cpus = psutil.cpu_percent(interval=1, percpu=True)

        # 获取系统时间（只取分:秒）
        curTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
       # print(type(cpus), cpus)

        # 保存到数据库
        cpuDao.saveToDb( curTime, cpus )

if __name__ == "__main__":
    monitorCpu()