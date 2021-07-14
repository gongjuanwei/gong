#安装模块 ：pip install xlrd 、 xlwt 、openpyxl
import xlwt
book =xlwt.Workbook()
sheet =book.add_sheet("sheet1")
sheet.write(0,0,"id")
sheet.write(0,0,"1")
book.save(test.xls)#结尾用xslx的话，用office打开有问题，wps打开没问题




