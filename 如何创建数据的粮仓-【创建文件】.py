import pandas as pd

# 创建DataFrame对象，参数为空excel表格为空
df = pd.DataFrame({"ID": [1, 2, 3], 'Name': ['Tim', 'Victor', 'Nick']})
# 设置ID列为索引列，如果不设置表格中会多出一列索引列
df = df.set_index('ID')
# 导出文件到excel文件
df.to_excel("C:/Temp/output.xlsx")
print("Done!")
