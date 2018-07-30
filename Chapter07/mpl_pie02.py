# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

labels = 'A', 'B', 'C', 'D'
fracs = [15, 30, 45, 10]
plt.axes(aspect=1)

# 显示饼状图的百分比
plt.pie(fracs, labels=labels, autopct='%.0f%%'   )
plt.show()

