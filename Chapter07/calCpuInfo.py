# -*- coding: utf-8 -*-

import os

cpuData = os.popen("cat /proc/cpuinfo").readlines()
sep = ','
output = ''
title = ''
value = ''

#对返回的CPU信息字符串匹配指标
for item in cpuData:
    if( item.find('cpu cores') > -1 or item.find('physical id') > -1 ):
        title = title + item.split(":")[0].strip() + sep
        value = value + item.split(":")[1].strip() + sep

output = title + '\r\n'+ value
print(output)
