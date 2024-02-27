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

# 方式二 通过数组的形式构建

index_labels = [['张三', '张三', '李四', '李四'], ['期中', '期末', '期中', '期末']]

multi_index = pd.MultiIndex.from_arrays(index_labels, names=['Name', 'Grades'])

data = {
    "Chinese": np.random.randint(80, 90, 4),
    'Math': np.random.randint(80, 100, 4)
}
df = pd.DataFrame(data, index=multi_index)

print(df)

# 方式三 笛卡尔积

index_labels = pd.MultiIndex.from_product([['张三', '李四', '王五', '赵六'], ['期中', '期末']], names=['Name', 'Exam'])

df = pd.DataFrame(np.random.randint(80, 151, size=(8, 2)), index=index_labels, columns=['Chinese', 'Math'])

print(df)

# 列索引的多层索引
