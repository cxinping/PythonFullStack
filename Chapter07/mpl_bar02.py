# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

N = 5
# 柱的高度
y=[20,10,30,25,15]
# 柱的个数
index = np.arange(N)

p2 = plt.bar(left=0,bottom=index, width=y,height=0.8,orientation ='horizontal' )
# 添加图的标题
plt.title("bar demo")
plt.show()
