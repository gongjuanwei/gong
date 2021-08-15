import pymysql
import traceback
from log import Log


class MySQL:  # 经典类

    def __init__(self, mysql_info, data_type=1):
        self.mysql_info = mysql_info
        self.mysql_info["autocommit"] = True
        self.data_type = data_type
        self.__connect_status = False
        self.__connect()

    def __connect(self):
        Log.debug("开始连接mysql")
        try:
            self.__conn = pymysql.connect(**self.mysql_info)
        except:
            Log.error("数据库连接出错！")
            raise Exception("数据库连接出错")
        self.__connect_status = True
        if self.data_type != 1:
            self.__cur = self.__conn.cursor(pymysql.cursors.DictCursor)
        else:
            self.__cur = self.__conn.cursor()
        Log.info("mysql连接成功！")

    def execute(self, sql):
        Log.debug("开始执行sql", sql)
        try:
            self.__cur.execute(sql)
        except:
            traceback.print_exc()
            Log.warning("sql不正确,sql语句是%s" % sql)
        else:
            Log.debug("sql执行完成！")
            return True

    def fetchone(self, sql):
        if self.execute(sql):
            return self.__cur.fetchone()

    def fetchall(self, sql):
        if self.execute(sql):
            return self.__cur.fetchall()

    def __del__(self):
        self.__close()
        Log.debug("mysql 连接关闭完成")

    def __close(self):
        if self.__connect_status:
            self.__cur.close()
            self.__conn.close()
