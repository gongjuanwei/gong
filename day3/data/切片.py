#切片就是list范围取值的一种方式
#顾头不顾尾
# li = [1,2,3,4,5]
#
# print(li[1:3])#从下标为1的元素开始取
# print(li[:3])#从前取到0:下标3的元素
# print(li[2:5])#从下标为2的元素开始取,取到最后
# print(li[2:])#从下标为2的元素开始取,取到最后
# print(li[:])#从开头取到最后


#生成一个1-10的list
li =range(1,10)#生成器[0-10]
for i in li:
    print(li)

li =list(range(1,11))#生成器[1-10的list]
print(li)
print(li[0:11:1])#挨着顺序取值比如：0+1=1
print(li[0:11:2])#隔2取值，比如：
#开始：结束：步长
#[1,2,3,4,5,6,7,8,9，10]
# 0,1,2,3,4,5,6,7,8，9 下标
# 1   3   5   7   9

[1,2,3,4,5,6,7,8,9,10]
print(li[-1:-11:-1])
print(li[-1:-11:-2])

s="121"
s1 =input("s:")
if s1==s[::-1]:
    print("是回文")
else:
    print("不是回文")

