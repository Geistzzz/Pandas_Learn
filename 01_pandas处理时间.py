import datetime

import pandas as pd

#
# import pandas as pd
#
# # 01：Timestamp 将字符串转换成时间对象
# print('将字符串转成时间对象')
# print(pd.Timestamp('2022-09-16 9:21:35'))
# print(pd.Timestamp('Sep 16, 2022 9:21:35'))
# print(pd.Timestamp(3))
# print('')
#
# # 02：获取当前时间
# print('获取当前时间')
# print(pd.Timestamp.now())
# print(type(pd.Timestamp.now()))
# print('')
#
# # 03:获取当前日期
# print('获取当前日期')
# print(pd.Timestamp.now().date())
# print('')
#
# # 04:通过日期元素获取标准日期
# print(pd.Timestamp('2022-09-16').date())
# print(type(pd.Timestamp('2022-09-16').date()))
# # .date()只能从标准日期格式开始转换
# print('')
#
# # 05 通过日期元素获取标准时间
# print(type(pd.Timestamp('2022-09-16').time()))
#
# date_string = '2022-09-16'
# print(type(pd.to_datetime(date_string).date()))  # <class 'datetime.date'>
#
# print(type(pd.to_datetime(date_string)))  # <class 'pandas._libs.ts_libs.timestamps.Timestamp'> 还是一个时间戳
#
# print(type(datetime.datetime.now()))  # 这是一个datetime对象
# print(datetime.datetime.now())
#
# """
# 时间差数据处理
# """
# print(pd.Timedelta(weeks=3))  # 3 days 没有years
#
# now = pd.Timestamp.now().date()
# date_time = pd.Timestamp(year=2022, month=9, day=30, hour=0, minute=0, second=0, microsecond=0).date()
#
# timedelta = now > date_time
#
# print(timedelta)

# print(datetime.date(2022, 2, 2))
# import time
# import datetime
#
# # 获取当前时间戳
# timestamp = time.time()
# print("当前时间戳：", timestamp)
#
# # 将时间戳转换为时间对象
# now = datetime.datetime.fromtimestamp(timestamp)
# print("时间对象：", now)
#
#
#
# now = datetime.datetime.now()
# timestamp = now.timestamp()
# print(timestamp)

now = pd.Timestamp.now().date()
start_date = now - pd.Timedelta(days=365 * 10)
print(start_date)
