import string
print(string.digits)#所有的整数
print(string.ascii_lowercase)#所有的小写字母
print(string.ascii_uppercase)#所有的大写字母
print(string.ascii_letters)#大写字母、小写字母
print(string.punctuation)#所有的符号

#转成list
print(list(string.digits))
#转成集合
print(set(string.digits))