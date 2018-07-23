# -*- coding: utf-8 -*-
import psutil

print('获取磁盘的详细信息=',psutil.disk_partitions())
print( '磁盘中C:盘的使用情况=',psutil.disk_usage('c:/'))
print('磁盘I/O信息=',psutil.disk_io_counters())