import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(100, 4), index=pd.date_range('1/1/2000', periods=100), columns=['A', 'B', 'C', 'D'])
df.to_csv('foo.csv')

df.to_excel('foo.xlsx', sheet_name='Sheet1')

ret = pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA'])
print(ret)
