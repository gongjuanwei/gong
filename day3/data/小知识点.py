
# age=17
# age2=''
# #原来方法
# if age>=18:
#     age2="成年"
# else:
#     age2="未成年"
# #三元表达式：
#     a3 = "成年" if age>18 else "未成年"
#     print(a3)


# 其它方法
# w = range(1,11)#1-11的list
# L2=[]
# for i in w:
#     if i % 2==0:#i除以2，余数等于0的话为偶数
#         L2.append(i)#是偶数的话吧i加进来
# print(L2)
 #列表生成式：
# w3 =[str(i)for i in w ]
# print(w3)
# w4 =[i for i in w if i %2==0 ]#有if条件的话就不用加str,i for 中的i,是用来存在list中的
# print(w4)
#其它方法，引入第三方变量temp
a =1
b=2
# temp =None
# temp=b
# b=a
# a=temp
# print(a,b)
#变量交换
a,b =b,a
print(a,b)
#在把上面的结果交换回来
a=a+b
b=a-b
a=a-b
print(a,b)
