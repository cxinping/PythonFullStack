# -*- coding: utf-8 -*-

#引入numpy库
import numpy as np

#创建一维的narray对象
a1 = np.array([1,2,3,4,5])
print(a1.shape)

#创建二维的narray对象
a2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(a2.shape)

print("二维数组的行数为:{0}".format( a2.shape[0] ))
print("二维数组的列数为:{0}".format( a2.shape[1] ))

# 修改数组第4个元素的值
a1[4] = 1

# 修改数组第0行，第0列元素的值
a2[0:0] =1

#修改np数组第1行，第2列元素的值
a2[1:2] =2

# 对二维数组 a2第0行进行修改
a2[0] = (2,2,2,2,2)

a2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("二维数组arr2的和为：{0}".format(a2.sum()))

print(a2.sum(axis=1))