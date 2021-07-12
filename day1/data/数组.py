#str int  float  bool  list
#数组
stu =["蔡一","蔡二","蔡三"]
print(stu)
#取元素
print(stu[0])
#新增元素
stu.append("最后新增元素")
stu.insert(0,"最前面新增元素")
stu.insert(2,"元素")
stu.append("泡泡元素")
print(stu)

#修改元素
stu[2]="蔡一"
print(stu)
# index = stu.index("元素")#找下标，如果查询不存在的元素会报错
# stu[index]= "修改元素"#修改元素的值
# print(stu)
#用for ，查询元素不存在的话怎么判断
# stus ="111"
# if stus in stu:
#     index=stu.index(stus)
#     stu[index]= "用for判断修改元素"
#     print(stu)

#删除元素
stu.append("最前面的元素")
print(stu)
#stu.pop()#删除末尾的元素
# stu.pop(0)#删除指定下标的元素
# stu.remove("蔡一")#删除指定的元素
# print("删除下标，的元素%s" % stu)
# del stu[1]
# print(stu)


# print( stu.count("蔡一") )#查找元素出现的次数
num =[90,80,70,100,2,1,3,66]
# num.sort()#排序，默认升序
# print(num)
# num.sort(reverse=True)#排序，默认是升序，会改变原来的list的值
# print(num)

# num.reverse()#反转list，会改变原来list的值
# num.clear()#清空list
num.extend(stu)#吧另一个list里面的元素加入到另一个list里面
print(num)
#



