# -*- coding: utf-8 -*-

import subprocess

result = subprocess.call(['ping','127.0.0.1'])
# 返回命令运行状态
print('result={0}'.format(result))