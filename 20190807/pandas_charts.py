import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ts = pd.Series(np.random.randn(10), index=pd.date_range('1/1/2000', periods=10))
# print(ts)
# print("=================================")
# ts = ts.cumsum()
# print(ts)
# ts.plot()
# plt.show()


ts = pd.Series(np.random.randn(100), index=pd.date_range('1/1/2000', periods=100))
df = pd.DataFrame(np.random.randn(100, 4), index=ts.index, columns=['A', 'B', 'C', 'D'])
df = df.cumsum()
df.plot()
plt.show()