import  os
# os.rename('yuanwenjian.py'，'newwenjian.py') #重命名
# os.remove()#删除文件
# os.rmdir('test')#删除空文件夹


# os.mkdir('test')#创建文件夹
# os.makedirs('test1')#创建文件夹
#car/bmw
# os.mkdir('car/bmw')#创建文件夹,父目录不存在的时候不能创建
# os.makedirs('car/bmw')#创建文件夹，父目录不存在，会创建父目录


# os.listdir()#获取某个目录下的内容
# print(os.listdir())
# print(os.listdir(r"C:\\Users\\Administrator\\.PyCharm2017.2\\gong\\day4")) #获取某个目录下的内容
# print(os.listdir(r"..\\day4")) #获取某个目录下的内容


# print(os.sep)#当前系统路径的分隔符

# command ='ipconfig'
# # os.system(command)#执行操作系统命令,返回的是命令是否执行成功，返回0代表成功
# result= os.popen(command).read()#执行操作系统命令
# print(result)


# print(os.environ)#os.environ取系统的环境变量
# print(os.name)#os.name当前操作系统的名称
# print(os.getcwd())#获取当前绝对路径

# os.chdir('../day4')#进入到某个目录
# print(os.getcwd())#获取当前绝对路径
# open('HH','w')


# os.walk()
# os.path.join()
# os.path.split()

# os.path.isfile('toos')#判断是不是文件夹
# os.path.isdir('M2.py')#判断是不是文件
# print(os.path.exists('M2.py'))#是否存在
# print(os.path.getsize('M2.py'))#获取文件大小，单位是字节

# os.path.abspath(('M2.py'))#获取绝对路径
# os.path.abspath((__file__)) #获取当前文件的绝对路径

# p= "C:/Users/Administrator/.PyCharm2017.2/gong/day5/常用模块.py"
# os.path.dirname(p)#取父目录，取上一级目录的


# os.path.getctime(('M2.py'))#获取文件创建时间
# os.path.getatime(('M2.py'))#获取文件最后一次访问时间
# os.path.getmtime(('M2.py'))#获取文件的修改时间

# print(os.path.join('e:','moives','sdy.mp4'))#拼接路径
# p="e:moives\sdy.mp4"
# print(os.path.split(p))#分隔



#获取某个目录下面的内容cur_path=当前目录、dirs文件夹、files文件
for cur_path,dirs,files in os.walk("C:/Users/Administrator/.PyCharm2017.2/gong/day5"):
    print(cur_path,dirs,files)

#e盘：mp4结尾
