# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# 生成一个数组，从0到4
index=np.arange(4)

# 某商品在北京的月销售额
sales_BJ=[52,55,63,53]
# 某商品在上海的月销售额
sales_SH=[44,66,55,41]

# 设置柱体的宽度
bar_width=0.3

plt.bar(index,sales_BJ,bar_width,color='b' ,label='sales_BJ')
plt.bar(index,sales_SH,bar_width,color='r',bottom=sales_BJ ,label='sales_SH')

# 设置图例
plt.legend(loc = 0 )
plt.title("bar demo")
plt.show()

