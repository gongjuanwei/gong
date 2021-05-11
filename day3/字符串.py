a = "abc"

#a.index()#找下标
#a.find()#找下标
# print(a.index("b1"))#如果找元素不存在，会报错
print(a.find("b1"))#如果找元素不存在，会返回-1

# b="abc1234567"
# print(b.index("b1",0,2))

# a.strip()#去掉字符串两边的空格和换行符，中间的不会
# a.lstrip()#去掉左边
# a.rstrip()#去掉右边

# a.lower()#吧字符串都变成小写
# a.upper()#吧字符串都变成大写

# a.count()#统计字符串中出现的某个字符串的个数
# a.isdigit()#判断字符串，是否为整数,是就返回true，否就返回false

# a.isalnum()#如果字符串不包含特殊符号，就返回true
# a.isalpha()#如果字母或者汉字就返回true,其它返回false


#a.format()#
# msg ="你好，{name},今天日期是{date}".format(name="xiaohei",date="2021-4-28")
# msg2="你好，{},今天日期是{}".format("xiaohei","2021-4-28")
#
# # a.format_map()#
# msg3="你好,{name},今天日期是{date}".format_map({"name":"xiaobai","date":"2021-4-28"})
# print(msg3)

# abc="123455678"
# msg4=f"你的是 {abc}"  3.6版本以上，第四种字符串格式化方法


# a.startswith()#判断字符串是否以xx开头
msg ="你好"
print(msg.startswith("你好"))
# a.endswith()#判断字符串是不是以xx结尾
file_name ="a.jpg"
print(file_name.endswith(".jpg"))




# a.zfill()#补0前面
# num ="05"
# print(num.zfill(3))#5代表总共有几位数



# a.replace()#替换
# mag = "nihao.nice to m y"
# new_mag = mag.replace("nihao",'heoll').replace(" ",'',1)
# print(new_mag)


v="are you"
# v.title()#标题
# v.capitalize()#首字母大写
print(v.title())
print(v.istitle())
print(v.capitalize())



# a.isspace()#判断是不是空格
# c =""
# print(c.isspace())



# a.isupper()#判断是否全部为大写字母
# a.islower()#判断是否全部为小写字母


# a.center()
# n ="登录"
# print(n.center(50,'*'))
# print(n.center(50,'-'))


# a.join()
# a.split()