import pymysql
# 数据库ip地址：132.145.93.63
# 用户名：jxz
# 密码：123456

ip="132.145.93.63"
user="jxz"
password ="123456"#密码必须是字符串
db="jxz"
port=3306#端口号必须写int类型

connect = pymysql.connect(host=ip,user=user,
                          password=password,db=db,port=port,autocommit=True) #连数据库,加上autocommit=True会自己提交，不需要在加commit
cursor=connect.cursor()# 建立游标

# sql = "show tables;"#新建表
# sql = "create table fmz (id int primary  key auto_increment,name varchar(50) not null,sex int default 0, phone varchar(11) unique );"

cursor.execute(sql)#执行sql语句
sql="selct * form fmz;"
sql='insert into fmz(name,phone) value ("小笑"," 13567888888 ");'
sql='update fmz set sex=11 where id=3;'
sql ='delete from fmz where id =3;'

result= cursor.fetchall()#始终返回的是一个二维数组，获取sql执行的结果
# connect.commit()#提交
# connect.rollback()#回滚

# result= cursor.fetchone()#只获取一条数据
# result= cursor.fetchmany((5))#获取n条数据
print(result)
cursor.close()#关闭游标
connect.close()#关闭sql


