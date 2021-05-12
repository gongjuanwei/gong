#非空即真，非零即真
a =""
b=[]
c={}
d=0
f=None
#判断username是否为空
username=input("用户名:").strip()
# if len(username)==0:
#     print("输入不能为空")
#True:
if username:
    print("用户名为：",username)
else:
    print("username不能为空")

#false:
# if not username:
#     print("username不能为空")
# else:
#     print("用户名为", username)

#非空即真，非零即真
age =18
age =[]
if age:
    print("不为空")