# -*- coding: utf-8 -*-

import os
import time

while True:
    data = os.popen('iostat').read()
    print(data)
    print(type(data))
    time.sleep(1)
