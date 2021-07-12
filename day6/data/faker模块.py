import faker
f = faker.Faker(locale="zh_CN")
print(dir(f))#查询，可以造数的方法
print(f.name())#随机姓名
print(f.address())#随机地址
print(f.ssn())#随机身份证号
print(f.email())#随机邮箱
print(f.city())#随机城市
print(f.year())#随机年份


