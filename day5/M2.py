# import M1
# M1.op_file()

# import sys
# print(sys.path)
# import M3
# print(M3.test)



# import sys
# sys.path.append(r"C:\Users\Administrator\PycharmProjects\gong\day4")
# import m4
# import 函数方法练习 as f
# print(m4.is_f(1.3))
# print(f.is_f(1.2))



#导入文件夹
#方法一：
import toos2 #导入一个文件夹，然后用该目录下的文件
print(toos2.M5.ADD)#需要在 init_.py  ,import m5才能使用

#方法二：
from toos2 import M5  #直接from 引用M5
print(M5.ADD)


import  toos
from toos import M5
print(M5.ADD)



#