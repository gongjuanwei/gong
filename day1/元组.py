#tuple和list区别，创建后不能修改元素
l =[1,2,3]#list数组
t =(1,2,3)#元组
print(t[0])
for i in t:
    print(i)
    info =("192.168.1.1","root","123456","8080")#把数据库ip地址，登录名，密码，端口号，定义在元组不可修改/list数组里面，可修改
    print(info.count("root"))#只有方法count
    print(info.index("root"))#只有方法下标查找
    # info =("192.1.168.1.1","root1","123456","8080")
    # print(info)