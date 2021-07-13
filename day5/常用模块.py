#os都是和操作系统相关的

import  os




# os.mkdir('test')#创建文件夹
# os.makedirs('test1')#创建文件夹
#car/bmw
# os.mkdir('car/bmw')#创建文件夹,父目录不存在的时候不能创建
# os.makedirs('car/bmw')#创建文件夹，父目录不存在，会创建父目录
# os.mkdir('car/benz')#创建文件夹，父目录存在，会创建子目录



# os.rename('yuanwenjian.py'，'newwenjian.py') #重命名
# os.remove()#删除文件，不能删除文件夹
# os.rmdir('test')#删除空文件夹的



# os.listdir()
# print(os.listdir()) #获取当前某个目录下的内容
# print(os.listdir(r"C:\\Users\\Administrator\\.PyCharm2017.2\\gong\\day4")) #获取绝对路径下的内容
# print(os.listdir(r"..\\day4")) #获取相对路径下的内容


# print(os.sep)#当前系统路径的分隔符



command ='ipconfig'
# os.system(command)#执行操作系统命令,返回的只是命令是否执行成功：0代表成功，乱码展示
# result= os.system(command)#执行操作命令后不会返回获取的结果，只会返回命令执行成功
# print(result)
#
# result= os.popen(command).read()#执行操作系统命令后，返回获取到的结果
# print(result)


# print(os.environ)#os.environ取系统的环境变量
# print(os.name)#os.name当前操作系统的名称
# print(os.getcwd())#获取当前绝对路径



# os.chdir('../day4')#进入到某个目录
# print(os.getcwd())#获取当前绝对路径
# open('HH','w')#进入的目录中，创建文件




# print(os.path.isfile('day5'))#判断是不是文件夹
# print(os.path.isdir('M1.py'))#判断是不是文件
# print(os.path.exists('M2.py'))#是否存在
# print(os.path.getsize('M2.py'))#获取文件大小，单位是字节

# print(os.path.abspath(('M2.py')))#获取绝对路径
# print(os.path.abspath((__file__)))#获取当前文件的绝对路径

# p= "C:/Users/Administrator/.PyCharm2017.2/gong/day5/常用模块.py"
# print(os.path.dirname(p))#取父目录，取上一级目录的



# print(os.path.getctime(('M2.py')))#获取文件创建时间
# print(os.path.getatime(('M2.py')))#获取文件最后一次访问时间
# print(os.path.getmtime(('M2.py')))#获取文件的修改时间

#
# print(os.path.join('e:','moives','sdy.mp4'))#拼接路径
#
# p="e:moives\sdy.mp4"
# print(os.path.split(p))#分隔路径


# #获取某个目录下面的内容：cur_path=当前目录、dirs当前目录文件夹、files当前目录文件   C:\Users\Administrator\PycharmProjects\gong
for cur_path,dirs,files in os.walk(r"C:\Users\Administrator\PycharmProjects\gong"):
    print(cur_path,dirs,files)





