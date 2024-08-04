import  pandas as pd

import os

list_file_name=[]
path=input('当前文件夹路径：')
for i in os.listdir(path):
     file_path=path+"\\"+i
     list_file_name.append(file_path)
     print(file_path)

lt = []
cols=[]
xx=1
while xx:

     r=input('结束输出请按0；\n请输出列名,回车确认:')
     if str(r)==str(0):
          xx=False
     else:
         cols.append(r)

print('注意：当目标结果与实际结果不一致时候，请检查列名是否一致！')

for x in list_file_name:

        sheet_names = pd.ExcelFile(x)
        sheet_names_list = sheet_names.sheet_names
        try:
             for i in sheet_names_list:
                 try:
                     df1 = pd.read_excel(x, sheet_name=i,header=0)[cols]
                     df1['Sheet_name']=i
                     lt.append(df1)
                     print(i)
                 except:
                     pass
         except:
              pass
              
mg = pd.concat(lt, ignore_index=True)

mg.to_excel(path+'./输出结果.xlsx')

print('完成合并')
