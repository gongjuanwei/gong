

#
# import random
# number =random.randint(1, 100)
# count = 0
# while count < 7:
#     guess = input("请输入一个数字：")
#     guess =int (guess)
#     count +=1#循环一次加1，也可以写成 count =count+1
#     if guess ==number:
#         print("恭喜你猜对了！数字是%s" %number)
#         break
#     elif guess <number:
#         print("猜小了")
#         continue#可写可不写
#     elif guess >number:
#         print("猜大了")
#         continue#可写可不写
#         #continue如果不写，则count += 1 可写到后面

# import random
# number =random.randint(1, 100)
# count = 0
# while count < 7:
#     guess = input("请输入一个数字：")
#     guess =int (guess)
#     count -=1#循环一次加1，也可以写成 count =count+1
#     if guess ==number:
#         print("恭喜你猜对了！数字是%s" %number)
#         break
#     elif guess <number:
#         print("猜小了")
#         continue#可写可不写
#     elif guess >number:
#         print("猜大了")
#         continue#可写可不写
#         #continue如果不写，则count += 1 可写到后面

# +=
# -=
# /=
# *=
#并且 and  或or
#
# import random
# number =random.randint(1, 100)
# print(number)
# count = 7
# while count > 0:
#     guess = input("请输入一个数字：")
#     guess =int (guess)
#     if guess ==number:
#         print("恭喜你猜对了！数字是%s" %number)
#         break
#     elif guess <number:
#         print("猜小了,剩余次数%s次" % count)
#         continue#可写可不写
#     elif guess >number:
#         print("猜大了,剩余次数%s次" % count)
#         continue#可写可不写
# else:
#     print("游戏结束，次数达到上限")

# for循环
# for i in range(7):
# #     print(i)


import random
number =random.randint(1,100)
for i in range(7):
    guess = input("请输入一个数字：")
    guess =int(guess)
    if guess ==number:
        print("恭喜你猜对了，数字是%s" % number)
        break
    elif guess <number:
        print("猜小了")
        continue
    elif guess >number:
        print("猜大了")












