import xlrd

ex = xlrd.open_workbook('D:/tp-shop测试用例.xlsx',"r")
a = ex.sheet_names()
print(a)
sheet1=ex.sheet_by_name(1)
print(sheet1)