import shutil,os,sys
# shutil.copy()
# shutil.copyfile('passwords.txt','../day5/passwords.txt')#复制到其它目录  ’传一个文件名.txt‘,'../day5/新的文件名.txt'
# shutil.copyfile('passwords.txt','passwords2.txt')  #复制到当前目录下  ，’旧名字.txt‘，新名字.txt
# # old,new,只能复制文件
#
# shutil.copy('password.txt','..day2/')#吧文件复制到一个目录xia
# shutil.copy('password.txt','../day2/password3.txt')# 复制文件，并改名字
#
#
#
# shutil.copytree("logs","logs2")#复制文件夹
# shutil.copytree("logs","../day2/logs")#复制文件夹
#
#
# shutil.rmtree('log2')#删除非空文件夹


# msg = input("input")
# if msg =="q":  #输入字，遇到q就退出
#     quit("程序退出")
# print(msg)



# print(sys.version_info)#获取当前python版本，返回的是一个元组
# print(sys.version_info[0])
# print(sys.version_info[1])
# print(sys.version)#获取当前python版本，返回的是一个字符串
# print(sys.platform)#获取当前的系统类型
# 系统类型：
# mac  darwin
# windows win 32
# linux linux

# sys.exit("系统退出")#quit




# sys.argv #用来获取运行python 文件的时候传入的参数
# print(sys.argv)

# if len(sys.argv)>1:
#     command =sys.argv[1]
#     if command =="bak":
#         print("备份数据库")
#     elif command =="clean":
#          print("开始清理xx表")
#     elif command =="create":
#         print("开始新建xxx数据库、xxx表")
#     else:
#         print("命令有误 请输入 bak/clean/create")
# else:
#     print("命令有误 请输入 bak/clean/create")


# input("num:")


# command =input("请输入选项：").strip()
# if command =="bak":
#         print("备份数据库")
# elif command =="clean":
#          print("开始清理xx表")
# elif command =="create":
#         print("开始新建xxx数据库、xxx表")
# else:
#         print("命令有误 请输入 bak/clean/create")
