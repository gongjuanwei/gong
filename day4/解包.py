msg ="admin,123456"
username = msg.split(',')[0]
password =msg.split(',')[1]
print(username)
print(password)

username,password=msg.split(',')
print(username)
print(password)

d={"username":"admin","password":"123456"}
print(d.items())
for u,p in d.items():
    print(u,p)