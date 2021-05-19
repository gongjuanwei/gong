#字典排序，二维数组
# d = {'admin': 89, 'test': 100, 'dev': 61}
# print(sorted(d))

d = {'admin': 89, 'test': 100, 'dev': 61}
def x(l):
    print(l)
    return l[1]
print(d.items())#items拿到，是一个二维数组
print(sorted(d.items(),key=x))#key=函数名
print(sorted(d.items(),key=x,reverse=True))#key=函数名