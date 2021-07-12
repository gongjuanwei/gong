import faker
f=faker.Faker(locale="zh_CN")
for i in range(100):
    print(f.name())