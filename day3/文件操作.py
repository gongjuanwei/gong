#flie()python2里面才有，也是打开文件
# open("a.txt")#打开文件

#打开文件不存在的话，会报错
# f =open("a.txt")#定义一个打开文件
# result =f.read()
# f.close()

#文件打开模式  9种：
# r：只读不能写，文件不存在会报错
# w：能写不能读，文件不存会创建，文件已存在会清空文件里面内容
# a：只能写不能读，文件不存在会创建，不会清空原来的文件，会在末尾添加
#
#写
# f =open("a.txt",'w',encoding='utf-8)
# f.write("你好呀")
# f.close()

#读
# f =open("a.txt",'r')
# result=f.read()
# f.close()
# print(result)
#1、r模式写，2、w模式读，然后写一些新内容，观察一些文件内容
f =open("a.txt",'a')#f =open("a.txt",encoding='utf-8')
# f.write("你好呀")
f.close()



