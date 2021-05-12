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
num =["1","2","3","5"]#list
f =open("a.txt",'w',encoding='utf-8')
# for i in num:
#     f.write(i)#只能写字符串
# f.write("你好呀")#只能写字符串,循环写
#
# for i in num:
#     i=str(i)+'\n'
#     f.write(i)#把list换行写入
nums =[str(i)+'\n' for i in num]
print(nums)
f.writelines(nums)

# f.writelines(num)#可直接写list
f.close()




#读
# f =open("a.txt",'r')
# result=f.read()
# f.close()
# print(result)
#1、r模式写，2、w模式读，然后写一些新内容，观察一些文件内容
# f =open("a.txt",'w',encoding='utf-8')#
# f.write("1111123456")
# f.close()



#readlines
# f =open("a.txt",encoding='utf-8')#
# # result=f.read()#读取所有的内容，返回的是字符串
# # result=f.readlines()#读取所有的内容，返回的是list
# # print(f.readline())#读取一行的内容
# # print(f.readline())
#
# print("f.read",f.read())
# f.seek(0)#移动文件指针控制，添加后下面readlines就能读到了
# print("f.readlines",f.readlines())
#
# f.close()




