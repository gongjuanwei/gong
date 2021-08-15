#1、创建8张表
#creat table user_0 like user_nhy;

#2、先从源表里面查到数据，然后取到phone,然后 % 8 计算出来在哪张表里，然后insert
#select * from user;
#[{id:1,nname:xx}]
#insert into user_0 values ()

#insert into user_0 select * from user where id =1;


from day8.homework import utlis
def create_table_more(src_table_name,number=8): #user_0 user_1
    print("开始创建表")
    for i in range(number):
        new_table_name = "%s_%s" % (src_table_name,i)
        sql = "create table if not exists %s like %s;" % (new_table_name,src_table_name)
        # sql = "drop table %s" % new_table_name
        print("创建表的sql ",sql)
        utlis.op_mysql(sql)
    print("分表创建完成")

def insert_data(src_table_name,number=8):
    sql = "select * from %s ; " % src_table_name
    all_data = utlis.op_mysql(sql,data_type=2)
    # print(all_data[0].keys())
    # return
    for data in all_data:
        table_index = int(data.get("phone")) % number
        table = "%s_%s" % (src_table_name,table_index)
        insert_sql = 'insert into %s select "",nick, gender, birthday, email, phone, password, qq, address, status, pay_status, avatar, register_time, last_login_ip, last_login_time from %s where phone = "%s"; ' % (table,src_table_name,data.get("phone"))
        utlis.op_mysql(insert_sql)
        print("数据 %s 迁移完成 " % data)
    print("所有数据迁移完成！")

if __name__ == '__main__':
    create_table_more("user_gy")
    insert_data("user_gy")