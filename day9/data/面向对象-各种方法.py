import time

class Car:
    # 类变量
    country ="China"
    # 静态方法
    @staticmethod
    def say():
        print("哈哈哈")

    # 类方法，一样可以传参数，但是不能调用实例化的方法def __init__(self,name)
    # 不需要实例化可以直接调用，通过实例也可以调用
    @classmethod
    def help(cls):
     print("清拨打客服热线99999")

    # 实例化
    def __init__(self,name):
        # 实例变量
        self.__name=name
        self .crete_time =int(time.time())-60*60*24*365*5

    # 实例方法
    def run(self):
        print("%s,run" % self.__name)

    # 属性方法（不能传参数）
    @property
    def age(self):
        car_age = int(time.time() - self.crete_time) / (60 * 60 * 24 * 365)
        print(car_age)

    def __getattr__(self, item):
        print("item", item)

qq=Car("奇瑞qq")
# qq.age()
print(qq.age)


Car.help()



# baoma=Car("宝马")
# baoma.run()
# baoma.run()
#
# benz=Car("奔驰")
# benz.name="宾士"
# benz.run()