
import pandas as pd

excelData1 = pd.read_excel(r'C:\Users\user\Downloads\TestFiles.xlsx', sheet_name='File_A')



print(excelData1.loc[excelData1['Gender']=='F'])

excelData2 = pd.read_excel(r'C:\Users\user\Downloads\TestFiles.xlsx', sheet_name='File_B')
print(excelData2.loc[excelData2['Gender']=='F'])