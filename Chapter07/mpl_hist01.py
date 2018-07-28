# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

mu = 100  #均值
sigma = 20  #标准差

# 设置随机数种子，是为了使每次随机数组生成的结果是一样的
np.random.seed(1)
x = mu + sigma * np.random.randn(2000)

# 画直方图，图中箱子的个数为50
plt.hist(x, bins=50,color='green',normed=True)
plt.title("hist demo")
plt.show()

