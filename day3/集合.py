#set 集合可以去重，集合是无序的就是无下标

# s ={1,2,3,4,4}
#s2 =set()
# s.add(5)#添加元素
# print(s)
# s.update({7,8,9,10})#把另一个集合加进去
# print(s)
# s.pop()#删除第一个元素
# print(s)

#交集、并集、差集
s ={1,2,3,4,5}
s1={1,2,3,5}
s2={8,9,10}
# print(s.intersection(s1))#交集
# print(s&s1)

print(s.union(s1).union(s2))#取并集
print(s | s1 |s2)

print(s.difference(s2))#取差集,在A集合中有，在B集合中没有的
print(s - s2 )


print(s.symmetric_difference(s1))#对称差集：交集之外的
print(s^s1)


