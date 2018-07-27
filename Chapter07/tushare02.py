# -*- coding: utf-8 -*-

import tushare as ts
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

data = ts.get_hist_data('600848',start='2018-03-01',end='2018-03-31')
# 对时间进行降序排列
data = data.sort_index()

xs = [mdates.strpdate2num('%Y-%m-%d')(d ) for d in data.index ]

plt.plot_date( xs , data['open'] , 'b-')
plt.gcf().autofmt_xdate()  # 自动旋转日期标记
plt.show()


