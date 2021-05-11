#
import copy
# l =[1,1,2,3,4,5,6,7,8]
# #l2=l的话，又会出现下标错乱，导致取值错误（浅拷贝，内存地址不变）
# l2 =l.copy()#浅拷贝，内存地址改变
# l2 =copy.copy(l)#浅拷贝，内存地址改变
#l2=l[:]#浅拷贝
# print(l)
# print(l2)

L1 =[1,1,2,3,4,5,6,7,8,[1,2,3]]
l2=copy.deepcopy(L1)#深拷贝
l2 [-1][1]="zen"
print(l2)
print(L1)

# print(id(l))#查看内存地址
# print(id(l2))#查看内存地址

#循环删list
#l2=[1,1,2,3,4,5,6,7,8]
#    0,1,2,3,4,5,6,7,8
# for i in l2:
#     if i %2 !=0:#余数不等于0，则删除
#         l.remove(i)
#   正在list,删里面的元素会导致下标错乱，取值错误
# print(l)