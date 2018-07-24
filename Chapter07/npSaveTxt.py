# -*- coding: utf-8 -*-

import numpy as np
np.random.seed(1)
arr = np.random.randn(3,4)
print( arr )

np.savetxt('test1.txt', arr ,delimiter=',' , fmt="%0.8f" )






