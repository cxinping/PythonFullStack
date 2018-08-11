# -*- coding: utf-8 -*-

import time
import os

print('fork1 pid={0}'.format(os.getpid()) )
# 程序挂起60秒
time.sleep(60)
print("ok")


