# -*- coding: utf-8 -*-
import numpy as np
np.random.seed(1)
arr = np.random.randn(3,4)

# 保存数据到CSV文件
np.savetxt('test1.csv', arr , delimiter=',' , fmt='%0.8f', header='rand1,rand2,rand3,rand4')







