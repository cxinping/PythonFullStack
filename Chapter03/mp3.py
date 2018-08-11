# -*- coding: utf-8 -*-

from multiprocessing import Queue

qu = Queue()
qu.put("java")
qu.put("python")
qu.put("C++")

print(qu.get())
print(qu.get())
print(qu.get())

