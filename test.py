import pandas as pd
import numpy as np
import xlwt
from openpyxl import load_workbook
df = pd.DataFrame(np.random.randn(3, 4))
print(df)

#DataFrame数据：df

#更改写入excle表的列名，将列名1，2，3更改为a，b，c
#方法一：全部列更名，必须是所有参数个数
df.columns = ['a','b','c', 'd']
#方法二：灵活更改列名
df.rename(columns={'1':'a', '2':'b', '3':'c', '4':'d'}, inplace = True)
def color_negative_red(val):
    """
    Takes a scalar and returns a string with
    the css property `'color: red'` for negative
    strings, black otherwise.
    """
    color = 'red' if val < 0 else 'black'
    return 'color: %s' % color

writer = pd.ExcelWriter('a.xls')
df.to_excel(writer ,sheet_name="Sheet1", encoding='utf-8', index=False, header=False)
book = writer.book
sheet = book.get_sheet("Sheet1")
sheet.col(0).width = 256 * 20

writer.save()







