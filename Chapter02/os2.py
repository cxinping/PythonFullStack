# -*- coding: utf-8 -*-

import os

data = os.popen("dir").read()
print(data)
