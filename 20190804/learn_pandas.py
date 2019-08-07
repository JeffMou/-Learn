import numpy as np
import pandas as pd

# s = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(s)

# dates = pd.date_range('20130101', periods=6)
# print(dates)
#
# df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
# print(df)

import pandas as pd
import numpy as np
data = {'a' : 0, 'b' : 1, 'c' : 2}

s = pd.Series(data)
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d, dtype=float)

df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])
df = df.append(df2)
# df = df.drop(columns='a')

d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}
df = pd.DataFrame(d)


def adder(ele1,ele2):
    return ele1+ele2

# df = pd.DataFrame(np.random.randn(4,3),columns=['col1','col2','col3'])
#
# print(df)
#
# print("*" * 100)
#
# df = df.apply(lambda x: x.max() - x.min(), axis=1)




N=20

df = pd.DataFrame({
   'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
   'x': np.linspace(0,stop=N-1,num=N),
   'y': np.random.rand(N),
   'C': np.random.choice(['Low','Medium','High'],N).tolist(),
   'D': np.random.normal(100, 10, size=(N)).tolist()
})

#print(df)

# for key, value in df.iteritems():
#     print(key, value)

# #reindex the DataFrame
# df_reindexed = df.reindex(index=[0,2,5], columns=['A', 'C', 'B'])
#
# print (df_reindexed)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.randn(10, 4), index=pd.date_range('2018/12/18',
                                                              periods=10), columns=list('ABCD'))
print(df)

df.plot()
plt.show()