import pymysql
from day8.homework.const import mysql_info
class MySQL: #经典类

    def __init__(self,mysql_info,data_type=1):
        self.mysql_info = mysql_info
        self.data_type = data_type
        self.__connect_status = False
        self.__connect()

    def __connect(self):
        print("开始连接mysql")
        try:
            self.__conn = pymysql.connect(**self.mysql_info)
        except:
            print("数据库连接出错！" )
            raise Exception("数据库连接出错")
        self.__connect_status = True
        if self.data_type != 1:
            self.__cur = self.__conn.cursor(pymysql.cursors.DictCursor)
        else:
            self.__cur = self.__conn.cursor()
        print("mysql连接成功！")

    def execute(self,sql):
        print("开始执行sql",sql)
        try:
            self.__cur.execute(sql)
        except:
            print("sql不正确,sql语句是%s" % sql)
        else:
            print("sql执行完成！")
            return True

    def fetchone(self,sql):
        if self.execute(sql):
            return self.__cur.fetchone()

    def fetchall(self,sql):
        if self.execute(sql):
            return self.__cur.fetchall()

    def __del__(self):
        self.__close()
        print("mysql 连接关闭完成")

    def __close(self):
        if self.__connect_status:
            self.__cur.close()
            self.__conn.close()



if __name__ == '__main__':
    my = MySQL(mysql_info)
    my.execute("update user_nhy_7 set nick ='杜拉拉' where id = 3")

    ret = my.fetchone("select * from user_nhy_7 where id = 3")
    print(ret)
    ret = my.fetchall("select * from user_nhy_7")
    print(ret)


    #如果报错了，还会不会走析构函数