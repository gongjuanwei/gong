import faker
f=faker.Faker(locale="zh-CN")
class Student:
    def __init__(self,name,age,_class,addr,email,country="china"):
        self.name=name
        self.age=age
        self.__class=_class
        self.addr=addr
        self.email=email
        self.country=country

# student_list=[]
# for i in range(10):
#     sj=Student(f.name(),,"飞马","北京","111@163.com")
#     student_list.append(sj)
# print(student_list)

# 直接实例化，修改数据
sj=Student(f.name(),18,"飞马","北京","111@163.com")
print(sj.addr)
print(sj.__dict__)
sj.addr  = "上海"
print(sj.addr)

stu ={'name': '李建华', 'age': 18, '_Student__class': '飞马', 'addr': '北京', 'email': '111@163.com', 'country': 'china'}






