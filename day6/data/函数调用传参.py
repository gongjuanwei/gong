def add(a,b):
    return a+b
# d={"a":1,"b":2}
# print(add(**d))#a=1,b=2



l=[1,4]
add(*l)#1,2
print(add(*l))



# index = 0
# for i in l:
#     print("%s->%s" % (index,i))
#     index+=1

# print(list(enumerate(l)))

# for index,i in enumerate(l):
#     print(index,i)