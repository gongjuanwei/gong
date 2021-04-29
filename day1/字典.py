stu ={
    "tizhong":150,
    "name":"蔡徐坤",
    "age":18,
    "high":180,
    "addr":"北京"
}
print(stu)

#新增
# stu["money"] = 30000
# stu.setdefault("car","bmw")
# #如果是已存在的key，setdefault不会修改已有的值
# stu.setdefault("age",19)
# print(stu)

#修改
stu["age"] =19

#取值
# #法一：中括号[]
# print(stu["name"])
# print(stu["age"])
# #法二：get
# print(stu.get("addr"))
# print(stu.get("tizhong"))
# print(stu)
#get如果取值不存在的值,会返回null；中括号如果取值不存在的值，会报错
print(stu.get("age1"))


#删除
#stu.pop("age")方法一
# del stu["age"]#方法二
stu.popitem()#随机删除一个元素
stu.popitem()#随机删除一个元素
print(stu)

