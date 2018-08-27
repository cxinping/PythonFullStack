# -*- coding: utf-8 -*-

import os
import time

while True:
    data = os.popen('top -n 1').read()
    print(data)
    print(type(data))
    time.sleep(1)
