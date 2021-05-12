#需求：access.log文件中，找出每分钟超过100次的ip地址，加入黑名单
# 0、死循环
# 1、读文件，移动文件指针（第一次读的时候，文件指针是0）
# 2、先找出ip地址
# 3、记录当前文件指针的位置，并且赋值给文件指针
# 4、ip地址存起来，list或者dict存
# 5、循环字典，判断出现的次数，大于100的找出来
# 6、slepp(60)60秒后重新读

fn ='access.log'
point=0
import time
while True:
    ips={}
    f = open(fn,encoding='utf-8')
    f.seek(point)
    for line in f :
        line =line.strip()
        if line:
            ip=line.split()[0]
            if ip in ips:
                ips[ip]+=1
            else:
                ips[ip]=1
    point=f.tell()
    for ip,count in ips.items():
            if count>=50:
                print("加入黑名单的ip是%s" % ip)
    time.sleep(60)
