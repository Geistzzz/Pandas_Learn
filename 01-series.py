# -*- coding = utf-8 -*-
# @Time : 2024/2/25 1:01 上午
# @Author : 张驰
# @File ： 01-series.py
# @Software: PyCharm
import random

import pandas as pd
import numpy as np

# # 什么是Series
# S = pd.Series(data=np.random.randint(10, 20, 3), index=list('ABC'), name='age')
# print(S)

# # Series如何索引
# data = [10, 20, 30, 40, 50]
# index = list('abcde')
# S2 = pd.Series(data, index)
# # 位置索引
# print(S2[0])
# print(S2.iloc[0])
# # 标签索引
# print(S2['a'])
# print(S2.loc['a'])

# # 切片
# # 位置切片
# print("位置切片")
# print(S2[0:3])
# print(S2.iloc[0:3])
# # 标签切片
# print("索引切片")
# print(S2['a':'e'])
# print(S2.loc['a':'e'])

# Series有哪些属性
# S = pd.Series(np.random.randint(0, 150, 2000), name='Grades')
# print(S)
# print('序列的名字是：', S.name)
# print(S.dtype)
# print(S.ndim)
# print(S.shape)
# print(S.size)
# print(S.index)
# print(S.values)

# Series如何转变成dataframe？
data = [10, 20, 30, 40, 50]
index = list('abcde')
S = pd.Series(data=data, index=index)
print(S)

# 第一种方法
print(pd.DataFrame(S))
a = pd.DataFrame(S)

# 第二种方法

b = S.to_frame(name='python')
print(b)
