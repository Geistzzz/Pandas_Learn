# -*- coding = utf-8 -*-
# @Time : 2024/3/2 2:22 下午
# @Author : 张驰
# @File ： 6_Pandas_groupby高级用法.py
# @Software: PyCharm

import pandas as pd
import numpy as np

df = pd.DataFrame(
    {'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'bar'],
     'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
     'C': np.random.randint(8),
     'D': np.random.randint(8), },
    # dtype={'A':np.str, 'B': np.str}
)
print(df.dtypes)
print('A那一列中的DISTINCT变成了索引')
print(df.groupby('A').sum())  # A那一列中的DISTINCT变成了索引
print(df.groupby(['A', 'B']).mean())  # 双层索引
print(df.groupby(['A', 'B'], as_index=False).mean())  # 没有索引，降为平庸
print(df.groupby(['A', 'B']).agg(['sum', 'mean', 'std']))
print(df.groupby(['A', 'B']).agg(['sum', 'mean', 'std']))
print(df.groupby(['A', 'B']).agg(['sum', 'mean', 'std'])['C'])
"""
重要*****
"""
print(df.groupby('A').agg({'B': 'sum', 'C': 'mean', 'D': 'std'}))
print()
#  遍历group分组
g = df.groupby('A')
g = df.groupby(['A', 'B'])
for name, group in g:
    print(name, group)

print(g.get_group(('bar', 'three'))['C'])
