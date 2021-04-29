# 1、第一个
# usernames = ["admin","test","dev"]
# password = ["111","222","333"]
# input("username:")
# input("password:")
# 1、最多输入3次，超过3次提示错误次数过多
# 2、输入账号/密码正确，提示欢迎xxx登录，今天的日期是xxx，程序结束
# 3、如果输入为空要提示，输入不能为空 （查一下字符串方法），算错误一次
# 4、如果输入账号不存在，要提示，算错误一次
# 5、密码输入错误也算一次
# 2、第二个
# 功能和第一个一模一样
# user_info =
# {
#     "admin": "111",
#     "test": "222",
#     "dev": "333"
# }
# 1、最多输入3次，超过3次提示错误次数过多
# 2、输入账号 / 密码正确，提示欢迎xxx登录，今天的日期是xxx，程序结束
# 3、如果输入为空要提示，输入不能为空 （查一下字符串方法），算错误一次
# 4、如果输入账号不存在，要提示，算错误一次
# 5、密码输入错误也算一次



# import datetime
# count=0
# while count<3:
#     usernames =input("usernames:")
#     password =input("password:")
import datetime

today=datetime.datetime.today()
username=str(input('请输入账户：'))
passwd1=str(input('请输入密码：'))
count = 0
while count < 3:
    if len(username) == 0 or len(passwd1) == 0:
        print('账户和密码不能为空，请重新输入账户和密码！')
    count = count + 1
else:
    break
else:
print("    else:
    break
    else:
    print('你已经输错三次！请稍后再试！')


