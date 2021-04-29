# stu=[]#定义一个空list
stu = ["vv","cc"]
while True:
    name = input("请输入名称：")
    if name == "quit":#先判断存不存在
        print("程序退出",stu)
        break
    elif stu.count(name) == 0:#在判断输入的值在list中是否为0
        stu.append(name)#如果满足判断，则添加至list中
        print("添加成功",stu)
        continue
    else:
        print("名称已存在，请重新输入")#如果存在，则不添加，并且提示：已存在
        continue
