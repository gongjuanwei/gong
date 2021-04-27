# name =  "蔡徐坤"
# print(name )

age = 10.123
# age2 = input("请输入你的年龄：") #input接收到的始终是str类型
# age2 = int (age2)
age2 = int(input("请输入你的年龄："))
# int数字类型，float小数类型，str字符串类型
print("age类型",type(age2))
print("age2类型",type(age))
age3 = age + age2
name = "aaa"
# %s(字符串什么类型变量都支持)  %d（取整数，不保留小数，写字符串会报错）  %f（取小数）
#print("新的年龄是 %s" % age3)
print("新的年龄是 %d" % age3)
#print("新的年龄是 %f" % age3)
#保留几位小数
print("新的年龄是 %.5f" % age3)
print(age3)