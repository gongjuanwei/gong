def hello():
    print('hello')

#def定义函数
def welcome(name):#name函数的参数
    print("welcome %s"% name)

welcome("candy")#调用函数，传一个实际参数值

def welcome(name,addr,age):#name函数的参数
    print("welcome %s"% name,addr,age)

welcome("candy","中国",18)

#   函数名  形参：两个变量名，一个默认值，调用的时候就不需要写
# def hanshu(hs,ct="默认值"):
#     print("第一个参数hanshu %s,第二个参数%s" % (hs,ct))#函数体
#
# #        实参：实际参数
# hanshu("cany")
# hanshu("cany3","多个参数2")


#定义一个函数,读
# def op_file(filename,content=None):
#     with open(filename,'a+',encoding="utf-8") as f:
#         f.seek(0)
#         if content:
#             f.write(content)
#         else:
#             result =f.read()
#             return result
# #调用上面函数
# content = op_file("student2.json")
# print(content)

#函数里面定义的变量都是局部变量，只在函数内部生效

#1、没有写return 的时候，调用函数是什么结果
def hanshu1():
    print('hanshu')

#2、有return的时候，是什么结果
def hanshu(name,country="中国"):
    return name,country#函数体

# #3、只有有一个return
def test():
    return
r =hanshu1()
print('没有写return的时候',r)
print('return多个值的时候',hanshu("小鬼"))
print('return后面什么都不写',test())

