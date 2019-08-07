"""
介绍DataFrame常用方法
"""
import pandas as pd
import numpy as np


print("DataFrame转置")
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}
df = pd.DataFrame(d)
print(df)
print("=" * 80)


print("The transpose of the data series is:")
print(df.T)
print("=" * 80)


print("返回表示DataFrame的维度的元组")
print(df.shape)
print("=" * 80)


print("查看前N行数据")
print(df.head(3))
print("=" * 80)

print("查看后N行数据")
print(df.tail(3))
print("=" * 80)


print("sum（每一列求和方法）")
print(df.sum())
print("=" * 80)

print("mean（求平均值方法）")
print(df.mean())
print("=" * 80)


print("返回数字列的Bressel标准偏差")
print(df.std())
print("=" * 80)


print("describe()函数是用来计算有关DataFrame列的统计信息的摘要")
print(df.describe())
print("=" * 80)


print("排序by index")
print(df.sort_index(axis=1, ascending=False))
print("=" * 80)

print("排序 by value")
print(df.sort_values("Age", ascending=True))
print("=" * 80)


print("依据条件进行选择")
print(df[df.Age > 30])
print("=" * 80)


print("依据条件进行选择")
print(df[df.Name.isin(["Andres", "Lee"])])
print("=" * 80)



dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)
print("=" * 80)

print("依据条件进行选择")
df1 = df[df > 0]
print(df1)
print("=" * 80)


print("判断是否为空")
print(pd.isna(df1))
print("=" * 80)


print("缺失值")
print(df1.fillna(value=5))
print("=" * 80)


print("Apply方法运用")
print(df)
print("=" * 80)
print(df.apply(lambda x: x.max() - x.min()))
print("=" * 80)


print("value_counts方法运用，统计每个元素出现的次数")
s = pd.Series(np.random.randint(0, 7, size=10))
print(s)
print(s.value_counts())
print("=" * 80)


print("将Series里面字符串转为小写")
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
print(s)
print("=" * 80)
print(s.str.lower())
print("=" * 80)


print("合并")
df = pd.DataFrame(np.random.randn(10, 4))
print(df)
print("=" * 80)
pieces = [df[:3], df[3:7], df[7:]]
print(pd.concat(pieces))
print("=" * 80)



df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
                            'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                            'C': np.random.randn(8),
                            'D': np.random.randn(8)})
print(df)
print("=" * 80)
print("分组")
print(df.groupby('A').sum())
print("=" * 80)
print(df.groupby(['A', 'B']).sum())
print("=" * 80)








