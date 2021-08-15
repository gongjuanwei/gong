import pymysql
from day7.上周作业 import config
import hashlib

def op_mysql(sql: str,all=True,data_type=1):
    #data_type是1的话，返回的是list，其他的返回字典
    connect = pymysql.connect(**config.mysql_info)
    # cursor = connect.cursor() if data_type == 1 else connect.cursor(pymysql.cursors.DictCursor)
    if data_type==1:
        cursor = connect.cursor()
    else:
        cursor = connect.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    result = None
    if sql.strip().lower().startswith("select"):
        if all:
            result = cursor.fetchall()
        else:
            result = cursor.fetchone()
    cursor.close()
    connect.close()
    return result


def my_md5(s,salt=''):
    s = str(s)
    new_s = "%s%s" % (s,salt)
    m = hashlib.md5(new_s.encode())
    return m.hexdigest()


def create_user_table():
    sql = "create table if not exists  nhy_user (id int primary  key auto_increment,username varchar(15) not null unique," \
          "password varchar(32) not null,error_count int default 0)"
    #show tables;
    #select *
    # from information_schema.TABLES
    # where TABLE_NAME = '需要查询的数据表名';
    op_mysql(sql)

if __name__ == '__main__':
    create_user_table()
    # print(my_md5("aA_123456"))