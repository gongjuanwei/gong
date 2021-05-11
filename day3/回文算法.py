# 需求：给定一个字符串，验证它是否是回文，只考虑字母和数字资字符，可以忽略字母大小写
#     输入："A man,a plan,a canal:Panama"
#     输出：true
# 思路：
# 1、回文，字符串反转之后和之前的字符串一模一样
# 2、循环字符串，挨个判断字符串是否为字母、数字:isalnum
# 3、如果是字母/数字，保存在一个list里面:join
# 4、list转成一个字符串，然后都变成小写:lower()
# 5、判断这个字符串和它反转后是否一致

s =input("s:").strip()#输入字符串，忽略空格
s_list=[]#定义一个list,用来保存输入的字符串
for i in s:#循环字符串
    if i.isalnum():#判断字符串是否为数字或者字母
        s_list.append(i)#把输入字符串新增到s_list里面
print('新增到s_list中',s_list)
new_s = ''.join(s_list)#把字符串连接起来
new_s = new_s.lower()#吧字符串变成小写

if new_s == new_s[::-1]:#开头到结尾，从最后开始反转
    print("是回文")
else:
    print("不是回文")



