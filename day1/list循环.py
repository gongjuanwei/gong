import os
#定义一个数组
l=['蔡li', '蔡7', '蔡8', '最后新增元素9', '泡泡元素9']
#取list、元素
print(len(l))
#请给l组的人创建一个文件夹
#方法一：麻烦方式
# index=0#下标从0开始
# while index<len(l):#判断第一次
#     name =l [index] # index是0
#     os.mkdir(name)#创建文件夹
#     index =index +1 #第二次，下标加1
#     print(name)

#方法二：麻烦方法
# for index in range(len(l)):
#     print(l[index])
for name in l:#直接循环list,就是取list里面的每个元素
    print(name)


