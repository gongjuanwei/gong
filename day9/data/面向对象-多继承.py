class A:
    # def eat(self):
    #     print("A eat")
       pass

class B(A):
    # def eat(self):
    #     print("B eat")
    pass


class C(A):
    def eat(self):
        print("C eat")
    pass

class D(B,C):
    pass



d =D()
d.eat()
