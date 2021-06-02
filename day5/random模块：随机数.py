import random
random.randint(1,100)  #
print(random.randint(1,100))#随机整数
print(random.uniform(1,100))#随机小数
print(random.randint(100000,999999))#随机验证码

a='12345'
h =[2,22,23,26,77,88]
print(random.choice(a))#随机选择一个
print(random.choice(h))#随机选择一个
print(random.sample(h,2))#随机选择2个

random.shuffle(h)#洗牌，这个函数没有返回值，他会改变原来list的值（）
print(h)




