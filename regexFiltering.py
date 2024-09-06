import pandas as pd

excelData1 = pd.read_excel('../input_files/testFiles.xlsx', sheet_name='File_A')
specialNames1=excelData1.loc[excelData1['Student Name'].str.contains(r'[^\w\s,]', regex=True)]
print(specialNames1)
excelData2 = pd.read_excel('../input_files/testFiles.xlsx', sheet_name='File_B')
specialNames2=excelData2.loc[excelData2['Student Name'].str.contains(r'[^\w\s,]', regex=True)]
print(specialNames2)