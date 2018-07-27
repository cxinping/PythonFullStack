# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

open,close=np.loadtxt('stack01.csv',delimiter=',',skiprows=1,usecols=(1,4),unpack=True)
#一维数组的前150条数据
#open = open[0:150]
#close = close[0:150]

plt.xlabel('open')
plt.ylabel('close')
plt.scatter(open,close )
plt.show()
