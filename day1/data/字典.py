#存蔡徐坤  18 180  150 北京


student=[["蔡徐坤","18","180","150","北京"],
        ["蔡徐坤","18","180","150","北京"],
        ["蔡徐坤","18","180","150","北京"],
        ["蔡徐坤","18","180","150","北京"]
]
#存字典
stu ={
    "tizhong":150,
    "name":"蔡徐坤",
    "age":18,
    "high":180,
    "addr":"北京"
}
print(stu)

#新增字典
# stu["money"] = 30000
#stu.setdefault("car","bmw")
#如果是已存在的key，setdefault不会修改已有的值
#stu.setdefault("age",20)
#print(stu)

#修改字典
#stu["age"] =19

#取值
# #法一：中括号[]
# print(stu["name"])
# print(stu["age"])
# #法二：get
# print(stu.get("addr"))
# print(stu.get("tizhong"))
# print(stu)
#get如果取值不存在的值,会返回null；中括号如果取值不存在的值，会报错
#print(stu["name1"])
print(stu.get("name1"))


#删除
#stu.pop("age")方法一
# del stu["age"]#方法二
#print(stu)

#随机删除一个字典
#stu.popitem()#删除最后一个元素
#print(stu)


#其他方法
#stu.clear()#清空
    # d ={"phone":110}
    # stu.update(d)#合并两个字典
    # print(stu.values())#查找所以values值
    # print(stu.keys())#查找所有keys值
    # print(stu.items())#查找所有keys和values值
#
#stu.has_key("name")在Python2里面有，Python3里面没有

#想判断name在不在stu里面
# print("name" in stu.keys())
# print ("name" in stu)#直接用in判断的话，就是判断这个keys是否存在
# print(stu)

#直接循环字典，每次取得字典是keys,比较高效的方式
# for key in  stu:
#     value =stu[key]
#     value2=stu.get(key)
#     print("%s" "%s"(key,value))
#     print("%s" "%s"(key,value2))
#     print(key)


print(stu.items())
for key,value in stu.items():
    print("%s"  "%s" %(key,value))
    
