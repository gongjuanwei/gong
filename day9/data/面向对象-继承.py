# 父类1
class LW:
    country ="中国"
    money=50000

    def __fly(self): # 私有的不可以继承
        print("fly")

    def make_money(self):
        print("挣钱")
        return 50000

    def eat(self):
        print("吃饭ll")
# 父类2
class Ll:
    country = "韩国"
    def paocai(self):
        print("泡菜")

    def eat(self):
        print("吃饭la")


# 继承父类
class Xw(LW,Ll):

    def huaqian(self):
        print("花钱")

    def make_money(self):
        print("挣钱")


# 继承父类
class Xxx(LW):

    def dubo(self):
        print("赌博")

    def make_money(self):
        f_money = super().make_money()
        cur_money = f_money+1000
        print("挣钱，每天挣 %s" % cur_money)


# xx = Xxx()
# xx.make_money()

print(Xw.mro()) # 广度优先、深度优先的
xw = Xw()
xw.eat() # mro





# xm=Xw()
# xm.money()
# xm.eat()
#
# print(Xw.money)
# print(Xw.country)