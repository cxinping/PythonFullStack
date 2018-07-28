# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

y=[20,10,30,25,15]
# 生成一个数组，从0到4
index = np.arange(5)
#  画图，生成5个高度为y，红色的柱体
p1 = plt.bar(left=index, height=y , width=0.5 , color='r' )
# 添加图的标题
plt.title("bar demo")
plt.show()
