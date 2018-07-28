# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

total_bill, tip  = np.loadtxt('tips.csv', delimiter=',' , skiprows=1
                              , usecols=[0,1] , unpack=True )

plt.hist( tip /total_bill  , bins=50  )
plt.show()

