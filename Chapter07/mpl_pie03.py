# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

labels = 'A', 'B', 'C', 'D'
fracs = [15, 30, 45, 10]
plt.axes(aspect=1)

explode=[0, 0.1 , 0, 0 ]
plt.pie(fracs, labels=labels, autopct='%.0f%%' ,explode=explode  )
plt.show()

