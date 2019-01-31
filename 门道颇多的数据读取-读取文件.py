import pandas as pd

"""
# header等于几第几行为列头
# people=pd.read_excel('C:/Temp/People.xlsx',header=2)
# header等于None设置为空列头
people = pd.read_excel('C:/Temp/People.xlsx', header=None)

# 查看表格多少行多少列
print(people.shape)
# 查看表格的列名
print(people.columns)
# 查看列表前几行
print(people.head(3))
print('=======================================================')
# 查看列表后几行
print(people.tail(3))

"""

"""
people = pd.read_excel('C:/Temp/People.xlsx', header=None)
# 设置列头
people.columns = ['ID', 'Type', 'Title', 'FistName', 'MiddleName', 'LastName']
people.set_index("ID",inplace=True)
print(people.columns)
people.to_excel('C:/Temp/output.xlsx')
print("Done!")
"""

# 打开文件时设定index列
df = pd.read_excel("C:/Temp/output.xlsx",index_col="ID")
df.to_excel("C:/Temp/output2.xlsx")
print("Done!")
