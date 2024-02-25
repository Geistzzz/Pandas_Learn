# -*- coding = utf-8 -*-
# @Time : 2024/2/25 10:38 下午
# @Author : 张驰
# @File ： 03_read_files.py
# @Software: PyCharm
import numpy as np
import pandas as pd

# pandas存储
data = np.random.randint(0, 100, (100, 3))
df = pd.DataFrame(data, columns=['Chinese', 'Math', 'English'])
df.to_csv('output.csv', index=False)
df.to_excel('output.xlsx', index=False) #
df.to_json('ouput.json', orient="records")

# pandas读取
# df = pd.read_csv('output.csv')
df = pd.read_json('ouput.json', orient='records')

print(df)