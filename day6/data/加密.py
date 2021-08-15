# md5
# 1  ->  gsggsgsgs


# import hashlib
# s= "7878787872"
# print(s.encode())
# m=hashlib.md5(s.encode())#encode 就是吧字符串变成bytes字节类型
# result =m.hexdigest()
# print(result)


# 加盐
# import hashlib
# salt = "$@%@dbfdg3523_2352322"
# s="zengruotian"
# after = salt+s
# l = list(s)
# index = len(l) // 2
# l.insert(index,salt)
# after = ''.join(l)
# print(after) #bytes 字节类型


import hashlib


def my_md5(s, salt=''):
    s = str(s)
    new_s = "%s%s" % (s, salt)
    m = hashlib.md5(new_s.encode())
    return m.hexdigest()


#
with open("xpinyin-0.7.6-py3-none-any.whl", 'rb') as f:
    m = hashlib.md5(f.read())
    print(m.hexdigest())
