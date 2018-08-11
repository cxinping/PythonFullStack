# -*- coding: utf-8 -*-

import os
import time

pid = os.fork()

if pid == 0 :
   print("子进程(pid={0}),对应的父进程id={1})".format(os.getpid(),os.getppid()))

else:
    print('父进程(pid={0}),生成了子进程(cpid={1})'.format(os.getpid(), pid))

time.sleep(60)
print("ok")