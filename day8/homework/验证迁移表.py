#1、先从源表查到数据
#2、再从分表里面查，如果这两天条数据一样

#1、丢数据了 a存在b里面不存在
#2、这条数据，某个字段不正确

from day8.homework import utlis
table_name = "user_nhy"
sql = "select * from user_nhy;"
src_data = utlis.op_mysql(sql,data_type=2)
for data in src_data:
    phone = int(data.get("phone"))
    table_index = phone % 8
    new_table = "%s_%s" %(table_name,table_index)
    new_table_sql  = "select * from %s where phone = '%s'; " %(new_table,phone)
    # print(new_table_sql)
    new_table_data = utlis.op_mysql(new_table_sql,all=False,data_type=2)
    if new_table_data:
        new_table_data.pop("id")
        data.pop("id")
        result = data.items() ^ new_table_data.items()
        if result:
            print("错误，数据%s有误,不一样的数据%s" % (phone,result))
    else:
        print("错误！数据 %s 丢失" % data)


#redis