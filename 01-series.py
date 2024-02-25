# -*- coding = utf-8 -*-
# @Time : 2024/2/25 1:01 上午
# @Author : 张驰
# @File ： 01-series.py
# @Software: PyCharm
import random

import pandas as pd
import numpy as np

# 什么是Series
S = pd.Series(data=np.random.randint(10, 20, 3), index=list('ABC'), name='age')
print(S)

# Series如何索引
data = [10, 20, 30, 40, 50]
index = list('abcde')
S2 = pd.Series(data, index)
# 位置索引
print(S2[0])
print(S2.iloc[0])
# 标签索引
print(S2['a'])
print(S2.loc['a'])