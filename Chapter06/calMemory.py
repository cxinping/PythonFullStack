# -*- coding: utf-8 -*-
import os

memData = os.popen('free -m').read()
print(memData)