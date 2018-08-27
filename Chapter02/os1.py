# -*- coding: utf-8 -*-

import os
import time

# 每5秒执行一次iostat命令
while True:
    # 获得执行命令的输出
    data = os.popen('iostat').read()
    print(data)
    time.sleep(5)

