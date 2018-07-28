# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

# 每一块饼图外侧显示的说明文字
labels = 'A', 'B', 'C', 'D'
# 每一块饼图的数据
fracs = [15, 30, 45, 10]

#plt.axes(aspect=1)

# 画图
plt.pie(fracs, labels=labels )
plt.title("pie demo")
plt.show()

