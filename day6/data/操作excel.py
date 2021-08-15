#安装模块 ：pip install xlrd 、 xlwt 、openpyxl
import xlwt
book =xlwt.Workbook()
sheet =book.add_sheet("sheet1")
# sheet.write(0,0,"id")
# sheet.write(1,0,"1")
# book.save("test.xls")#创建excel文件，结尾用xslx的话，用office打开有问题，wps打开没问题

title =["id","name","sex","city"]
students =[
    [1,"曾","男","北京"],
    [2,"曾","男","北京"],
    [3,"曾","男","北京"]
]
row =0#行号
for student in students:#第一个循环控制行
    col=0##列号
    for value in student:##第二个循环控制列
        sheet.write(row,col,value)
        col+=1
    row+=1




# for row,student in enumerate(students):
#     for col,value in enumerate(student):
#         sheet.write(row,col,value)


book.save("test.xls")