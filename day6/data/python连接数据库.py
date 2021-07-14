import pymysql
# 数据库ip地址：132.145.93.63
# 用户名：jxz
# 密码：123456

# ip="118.24.3.40"
# user="jxz"
# password ="123456"#密码必须是字符串
# db="jxz"
# port=3306#端口号必须写int类型

# connect = pymysql.connect(host=ip,user=user,
#                           password=password,db=db,port=port,autocommit=True) #连数据库,加上autocommit=True会自己提交，不需要在加commit
# cursor=connect.cursor()# 建立游标
# # sql = "show tables;"#查询表
# #建一张表：
# # sql = "create table fmz_ikun (id int primary  key auto_increment,name varchar(50) not null,sex int default 0, phone varchar(11) unique );"
# sql="select * from fmz_ikun;"#查询表
# # sql="delete from ikun"#删除表
# # sql='INSERT INTO fmz_ikun(name,phone) values ("蓝玫瑰","13888888899");'#插入字段值
# # sql='update fmz_ikun set sex=11 where id=3;'#修改id为3的数据
# # sql ='delete from fmz_ikun where id =1;' #删除id为1的数据
# cursor.execute(sql)#执行sql语句
#
# result= cursor.fetchall()#始终返回的是一个二维数组，获取sql执行的结果
# # connect.commit()#提交
# # connect.rollback()#回滚
# print(result)
# print(cursor.fetchone())#只获取一条数据
# print(cursor.fetchmany((5)))#获取n条数据
#
# # for c in cursor: #直接循环游标，每次取的就是表里面的每一条数据
# #     print(c)
#
#
# cursor.close()#关闭游标
# connect.close()#关闭sql




#封装函数方法的
def op_mysql(mysql_info:dict,sql:str,all=True):
    connect =pymysql.connect(**mysql_info)
    cursor =connect.cursor()
    cursor.exectue(sql)
    result =None
    if sql.strip().lower().startswith("select"):
        if all:
            result =cursor.fetchall()
        else:
            result =cursor.fetchone()
    cursor.close()
    connect.close()
    return result

if __name__ =='__main__':

    mysql_info={"host"}
