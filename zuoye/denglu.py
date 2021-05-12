# 1、第一个
# input("username:")
# input("password:")
# 1、最多输入3次，超过3次提示错误次数过多
# 2、输入账号/密码正确，提示欢迎xxx登录，今天的日期是xxx，程序结束
# 3、如果输入为空要提示，输入不能为空 （查一下字符串方法），算错误一次
# 4、如果输入账号不存在，要提示，算错误一次
# 5、密码输入错误也算一次
# 2、第二个
# 功能和第一个一模一样
# 1、最多输入3次，超过3次提示错误次数过多
# 2、输入账号 / 密码正确，提示欢迎xxx登录，今天的日期是xxx，程序结束
# 3、如果输入为空要提示，输入不能为空 （查一下字符串方法），算错误一次
# 4、如果输入账号不存在，要提示，算错误一次
# 5、密码输入错误也算一次

#list方法
# import datetime
# usernames = ["admin","test","dev"]
# passwords = ["111","222","333"]
# for i in range(3):#循环3次
#     username =input("username:")#输入用户名
#     password =input("password:")#输入密码
#     if len(username)==0 or len(password)==0:#判断用户名、密码是否为空
#         print("用户名和密码不能为空")#如果为空则，提示：用户名和密码不能为空
#         elif username not in usernames:#判断输入用户名是否存在，usernames（list数组）中
#         print("账号不存在！")#如果不存在，则提示：账号不存在！
#     else:#如果上面都满足，则用输入的用户名，
#         username_index =usernames.index(username)
#         db_password=passwords[username_index]
#         if  password==db_password:
#             print("欢迎登陆%s,今天日期是%s" % (username,datetime.datetime.today()))
#             break
#         else:
#             print("密码错误！")
# else:
#     print("错误次数超过3次")

#字典方法
import datetime
user_info={
    "admin": "111",
    "test": "222",
    "dev": "333"
}
for i in range(3):
    username =input("username:")
    password =input("password:")
    if len (username) ==0 or len(password)==0:
        print("账号和密码不能为空！")
    elif username not in user_info:
        print("账号不存在！")
    else:
        db_password =user_info[username]
        if password ==db_password:
            print("欢迎登陆%s,今天日期是%s" % (username,datetime.datetime.today()))
            break
        else:
            print("密码错误！")
else:
    print("错误次数达到3次！")





