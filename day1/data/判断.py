#if:
#xxx
#else:
#xxx
#比较运算符
#== 等于
#>大于
#< 小于
#>=
#<=
#!=

#第一种：
# username ="admin"
# password ="12345"
# u = input("请输入用户名：")
# if u==username:
#     print("你是damin用户")
# else: print("用户不正确")
#第四种：
# username ="admin"
# password ="12345"
# username2 ="kun"
# u =input("请输入用户名：")
# p =input("请输入密码：")
#
# if (u==username or u==username2) and p==password:
#     print("登录成功，欢迎%s登录 " %username)
# else: print("账号/密码错误！")
#第五种,嵌套法
# username ="admin"
# password ="kun"
# username2="admin2"
# u = input("请输入用户名：")
# p = input("请输入密码：")
# if u == username or u == username2:
#     if p == password:
#         print("登录成功")
#     else:
#         print("mimacuowu")
# else:
#        print ("用户错误")
#in在...里面
#第一种用上面学习的判断方法
# sex = input("请输入性别：")
# if sex=="nan" or sex =="nv":
#     print("hefa")
# else:
#     print("nibusdiqren")
#第二种：定义一个字符串
# sex = input("请输入性别：")
# sex_str ="男女"#定义一个字符串
# if sex in sex_str:
#     print("合法")
# else:
#     print("不对")
# 第三种：定义一个字符串、加取长度,in在sex_str里面
#print(len(sex))#取长度
# sex= input("请输入性别：")
# sex_str = "男女"  # 定义一个字符串
# if sex in sex_str and len(sex) == 1:
#     print("合法")
# else:
#     print("不对")

# 第三种：定义一个字符串、加取长度,not in不在sex_str里面
sex= input("请输入性别：")
sex_str = "男女"
if sex not in sex_str:
    print("不合法")
elif len(sex)!= 1:
    print("不合法")
else:
    print("合法")
