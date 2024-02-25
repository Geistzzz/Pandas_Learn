# -*- coding = utf-8 -*-
# @Time : 2024/2/25 11:16 下午
# @Author : 张驰
# @File ： 05_DateFrame如何创建多层索引.py
# @Software: PyCharm

# 创建一个元组列表作为多层索引的标签
import numpy as np
import pandas as pd

index_labels = [('李四', '期中'), ('张三', '期中'), ('李四', '期中'), ('张三', '期中')]

# 使用pd.MultiIndex.from_tuples创建多层索引
multi_index = pd.MultiIndex.from_tuples(index_labels, name=['Name', 'Grades'])

# 创建DataFrame()
data = {
    "Chinese": np.random.randint(80, 90, 4),
    'Math': np.random.randint(80, 100, 4)
}
df = pd.DataFrame(data, index=multi_index)
print(df)
