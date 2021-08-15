# 定义一个类class  car，以及一个方法def  fly
class Car:
    wheel = 4  # 类变量，公共的
    # country = "china"

    # color ="黑色"
    # name ="金色汽车"
    def __init__(self, color, name):# 实例化的时候字段必填color, name
        # 构造函数，类在实例化的时候，自动执行的函数
        print("生产了一个汽车，直接执行__del__")
        self.color = color
        self.name = name
        self.fly()
        self.country ="china"

    def __del__(self):#析构函数
        print("汽车报废了！")
        #实例在销毁的时候自动执行的

    def fly(self):#
        # print("self...",id(self))
        print("%s fly" % self.name)

    def say(self):#汽车在说话
        print("我是一个汽车，我的名字是%s,颜色是%s" % (self.name, self.color))

#####################################################################################

fmz_car = Car("金色", "小金汽车")  # 类名+一个（），就是：类实例化

fmz_car.fly()#实例化类后才能调用方法
fmz_car.say()#实例化类后才能调用方法

# car = Car("金色", "金金汽车")
# car.fly()
# car.say()
#####################################################################################

# Car.say()#括号里没有实例化，运行时就会报错
car1 = Car("黑色","小黑汽车") #实例化
car1.say()
del car1
print("!!!!!!!!!")

# del  car1
# car1.fly() # Car.fly(car1)
# fmz_car.fly()




import requests
import logging
l =  logging.Logger("xx")
#
#
# class MyRequest:
#     def get(self):
#         log.info("url,data,get")
#
# r = MyRequest(url,data,header,json,files)
# result = r.post()  # {}
# result = r.get()  # {}