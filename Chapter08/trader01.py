# -*- coding: utf-8 -*-

import tushare as ts
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import matplotlib.dates as mdates

data = ts.get_hist_data('600848')
#data = data.head(5)

xs = [mdates.strpdate2num('%Y-%m-%d')(d ) for d in data.index ]
plt.plot_date(xs, data['open'],'-')
plt.gcf().autofmt_xdate()
plt.show()
 