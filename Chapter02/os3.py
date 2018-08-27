# -*- coding: utf-8 -*-

import os
import time

while True:
    data = os.popen('top').read()
    print(data)
    time.sleep(5)
