#封装函数方法的
def op_mysql(mysql_info:dict,sql:str,all=True):
    connect =pymysql.connect(**mysql_info)# 调用函数的时候，如果有两个**，代表传的是一个字典 #host="xxx",user="xxx",password="xxx"

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

    mysql_info = {"host": "118.24.3.40", "user": "jxz",
                  "password": "123456", "port": 3306, "db": "jxz",
                  "autocommit": True, "charset": "utf8"}
