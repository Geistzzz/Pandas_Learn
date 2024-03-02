# -*- coding = utf-8 -*-
# @Time : 2024/3/2 9:07 下午
# @Author : 张驰
# @File ： 7_Pandas_数据合并函数.py
# @Software: PyCharm

# merge函数
import time

import pandas as pd

#
# pd.merge(
#     "left_data",
#     "right_data",
#     left_on="左列名",
#     right_on="右列名",
#     how="inner"  # 可以有left，right，outer
#
# )
# concat函数
# import pandas as pd

df1 = pd.DataFrame(
    {
        'A': ['A0', 'A1', 'A2', 'A3'],
        'B': ['B0', 'B1', 'B2', 'B3'],
        'C': ['C0', 'C1', 'C2', 'C3'],
        'D': ['D0', 'D1', 'D2', 'D3'],
        'E': ['E0', 'E1', 'E2', 'E3']
    }
)
#
# df2 = pd.DataFrame(
#     {
#         'A': ['A4', 'A5', 'A6', 'A7'],
#         'B': ['B4', 'B5', 'B6', 'B7'],
#         'C': ['C4', 'C5', 'C6', 'C7'],
#         'D': ['D4', 'D5', 'D6', 'D7'],
#         'F': ['E4', 'E5', 'E6', 'E7']
#     }
#
# )
# # demo concat的默认参数 axis=0，join = outer，ignore_index=False(保留最大信息)
# df3 = pd.concat([df1, df2])
# df4 = pd.concat([df1, df2], ignore_index=True, join='inner')
# print(df3)
# print(df4)


# Concat添加一列Series
S1 = pd.Series(list(range(5)), name='S2')
df2 = pd.concat([df1, S1], axis=1)

# 添加多列Series
S2 = df1.apply(lambda x: x['A'] + "_GG", axis=1)
S2.name = 'S2'
df3 = pd.concat([df1, S1, S2], axis=1)  # 还是的，默认保留最大的信息
df4 = pd.concat([S1, S2], axis=1)
# concat函数是可以有混合顺序的
df5 = pd.concat([S1, df1, S2], axis=1)
print(df5)

# append函数的用法
df1 = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'))
print(df1._append(df2, ignore_index=True))

# 怎么一行一行的的给DataFrame添加数据
# 先创建一个DataFrame空的
df = pd.DataFrame(columns=['A'])

# 低版本性能
t1 = time.time()
for i in range(100):
    df = df._append({'A': i}, ignore_index=True)
t2 = time.time()
print(t2 - t1)
# 高性能版本
t1 = time.time()
df = pd.concat([pd.DataFrame([i], columns=['A']) for i in range(100)]
               , ignore_index=True)
t2 = time.time()
print(t2 - t1)
