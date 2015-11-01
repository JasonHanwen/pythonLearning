import pandas as pd
import numpy as np

xls_file = pd.ExcelFile('test.xls')
# print xls_file.head()
print xls_file.sheet_names

# Create a Pandas dataframe from the data.
data = pd.DataFrame({'Name':['Hanwen Wang', 'Xue Leng'],'ID':[1,2], 'Grade':[90,95]})

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('pandas_simplemy.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
data.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()
