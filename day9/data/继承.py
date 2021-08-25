
class Lw:
    country = "日本"
    money = 5000

    def __fly(self): #私有的不可以继承
        print("fly")

    def make_money(self):
        print("挣钱，500块钱")
        return 500

    def eat(self):
        print("吃饭")

class Ll:
    country = "韩国"

    def paocai(self):
        print("泡菜")

    def eat(self):
        print("老李吃饭")

class Xw(Lw,Ll):

    def make_money(self):
        print("挣钱，1000块钱")

    def huaqian(self):
        print("花钱")

class Xxx(Lw):
    def dubo(self):
        self.eat()
        print("赌博")

    def make_money(self): #1500
        f_money = super().make_money()
        cur_money = f_money+1000
        print("挣钱，每天挣 %s " % cur_money)

# print(Xw.mro()) #广度优先、深度优先的
# xw = Xw()
# xw.eat() #mro

xx= Xxx()
xx.make_money()


# xm = Xw()
# xm.make_money()
# xm.eat()
# print(Xw.money)
# print(Xw.country)
# class A: #经典类
#     pass
# class A():#新式类
#     pass
# class A(object):
#     pass