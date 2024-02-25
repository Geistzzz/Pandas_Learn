# -*- coding = utf-8 -*-
# @Time : 2024/2/25 9:23 下午
# @Author : 张驰
# @File ： 02_DataFrame.py
# @Software: PyCharm
# 方式一：字典
import numpy as np
import pandas as pd

data = {
    "Name": ['Alice'],
    "Age": [25],
    "City": ['NewYork']
}

df = pd.DataFrame(data)

print(df)

# 方式二：列表嵌套列表或者列表嵌套元组
data = [('Mary', 28, 'London')]

df = pd.DataFrame(data, columns=['Name', 'Age', "City"])

print(df)

# 方式三：用np里面的数据类型
data = np.random.randint(100, 150, (500, 3))
df = pd.DataFrame(data, columns=['Chinese', "Math", "English"])
print(df)
print(np.random.randint(100, 150, (500, 5)))
