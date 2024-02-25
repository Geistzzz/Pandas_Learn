# -*- coding = utf-8 -*-
# @Time : 2024/2/25 11:04 下午
# @Author : 张驰
# @File ： 04_multi_to_excel.py
# @Software: PyCharm

# 第三种方式：
import pandas as pd

data1 = {"Name": ['Alice', 'Bob', 'Charlie'],
         "Age": [25, 30, 35],
         "City": ['New York', 'Lodon', 'Paris']}

df1 = pd.DataFrame(data1)

data2 = {"Product": ['A', 'B', 'C'],
         "Price": [10, 20, 30],
         "Quantity": ['100', '200', '300']}
df2 = pd.DataFrame(data2)

with pd.ExcelWriter('duobiao.xlsx', engine='openpyxl') as ew:
    df1.to_excel(ew, sheet_name='sheet1', index=False)
    df2.to_excel(ew, sheet_name='sheet2', index=False)
