# -*- coding: utf-8 -*-

import psutil

print('获取cpu的完整信息=', psutil.cpu_times() )
print('获取cpu的所有逻辑信息=', psutil.cpu_times_percent() )
print('CPU逻辑数量=', psutil.cpu_count())
print('CPU物理核心=', psutil.cpu_count(logical=False))


