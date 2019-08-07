"""
系列(Series)是能够保存任何类型的数据(整数，字符串，浮点数，Python对象等)的一维标记数组
"""
import pandas as pd
import numpy as np


print("创建一个空系列")
s = pd.Series()
print(s)
print("=" * 80)



print("从ndarray创建一个系列, 默认索引为0到len(data)-1")
data = np.array(['a','b','c','d'])
s = pd.Series(data)
print(s)
print("=" * 80)



print("从ndarray创建一个系列, 指定索引")
data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,101,102,103])
print(s)
print("=" * 80)


print("从字典创建一个系列")
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data)
print(s)
print("=" * 80)


print("从字典创建一个系列, 指定索引")
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data,index=['b','c','d','a'])
print(s)
print("=" * 80)


print("从标量创建一个系列, 根据索引长度重复该标量")
s = pd.Series(5, index=[0, 1, 2, 3])
print(s)
print("=" * 80)


print("从标量创建一个系列, 根据索引长度重复该标量")
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print(f"输出第一个元素\ns[0]={s[0]}")
print(f"s[a]={s['a']}")
print(f"输出前三个元素\n{s[:3]}")
print(f"输出多个元素\n{s[['a','c','d']]}")
print("=" * 80)









