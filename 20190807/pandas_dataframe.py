"""
数据帧(DataFrame)是二维数据结构，即数据以行和列的表格方式排列
"""
import pandas as pd
import numpy as np


print("创建一个空DataFrame")
df = pd.DataFrame()
print(df)
print("=" * 80)


print("从列表创建DataFrame")
data = [1, 2, 3, 4, 5]
df = pd.DataFrame(data)
print(df)
print("=" * 80)


print("从列表创建DataFrame, 指定列名")
data = [['Alex', 10],['Bob', 12],['Clarke', 13]]
df = pd.DataFrame(data, columns=['Name', 'Age'])
print(df)
print("=" * 80)


print("从ndarrays/Lists的字典来创建DataFrame")
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
print(df)
print("=" * 80)

print("从ndarrays/Lists的字典来创建DataFrame， 指定index")
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print(df)
print("=" * 80)


print("字典列表可作为输入数据传递以用来创建数据帧(DataFrame)，字典键默认为列名")
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print(df)
print("=" * 80)


print("如何使用字典，行索引和列索引列表创建数据帧(DataFrame)")
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])
print(df)
print("=" * 80)

print("列添加")
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df)

# Adding a new column to an existing DataFrame object with column label by passing new series

print("Adding a new column by passing as Series:")
df['three']=pd.Series([10,20,30],index=['a','b','c'])
print(df)

print("Adding a new column using the existing columns in DataFrame:")
df['four']= df['one']+df['three']
print(df)
print("=" * 80)


print("列删除")
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
del df['one']
print(df)


df = pd.DataFrame(d)
df.pop('two')
print(df)
print("=" * 80)



print("按标签选择")
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df)
print("选择某一行的数据")
print(df.loc['b'])
print(df.iloc[1])
print("=" * 80)
















