#for 循环
#循环7次结束
# for i in range(7):
#     print(i)
# else:
#     print("循环结束")

# import random
# number =random.randint(1, 100)
# for i in range(7):
#     guess = input("请输入一个数字：")
#     guess =int (guess)
#     if guess ==number:
#         print("恭喜你猜对了！数字是%s" %number)
#         break
#     elif guess <number:
#         print("猜小了")
#         continue#可写可不写
#     elif guess >number:
#         print("猜大了")
#         continue#可写可不写

import random
number =random.randint(1, 100)
print(number)
for i in range (7):
            guess = input("请输入一个数字：")
            guess =int (guess)
            #循环一次减1
            if guess ==number:
                print("恭喜你猜对了！数字是%s" %number)
                break
            elif guess <number:
                print("猜小了,剩余%s次" % i)
                continue#可写可不写
            elif guess >number:
                print("猜大了,剩余%s次" % i)
                continue#可写可不写
                #continue如果不写，则count += 1 可写到后面
else:
    print("游戏结束，次数达到上限")