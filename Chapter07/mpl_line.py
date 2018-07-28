# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 对第一列的日期进行时间转换,指定转换的日期格式，对转换的数据需要进行解码.
def datestr2num(s):
    return mdates.strpdate2num("%m/%d/%Y")(s.decode('gb2312'))

date,open,close=np.loadtxt('stack01.csv',delimiter=',',
                            converters={0:datestr2num} ,
                           skiprows=1,usecols=(0,1,4),unpack=True)

# 设置X轴标签
plt.xlabel('date')
# 设置Y轴标签
plt.ylabel('open')

plt.plot_date(date,open,'y-')
# 自动旋转日期标记
plt.gcf().autofmt_xdate()
plt.show()
