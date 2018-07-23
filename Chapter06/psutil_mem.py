# -*- coding: utf-8 -*-
import psutil

memory = psutil.virtual_memory()
print( memory )
print('物理总内存=' , memory.total)
print('可使用内存=' , memory.available)
print('已使用内存百分比=' , memory.percent)
print('已使用内存=' , memory.used)
print('空闲的内存数=' , memory.free)
