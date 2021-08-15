import tools
import xlwt
import time

# 获取表的信息
def get_table_field(table_name):
    query_table_info_sql = "select COLUMN_NAME from " \
                           "information_schema.COLUMNS where table_name = '%s';" % table_name
    table_field = tools.op_mysql(query_table_info_sql)
    title = [ table[0] for table in table_field]
    return title

# 值写入excel
def write_excel(data,excel_name):
    book = xlwt.Workbook()
    sheet = book.add_sheet("sheet1")
    for row,row_data in enumerate(data):
        for col,col_data in enumerate(row_data):
            sheet.write(row,col,col_data)
    book.save(excel_name)

# 判断表存不存在,存在插入数据
def main(table_name):
    title = get_table_field(table_name)
    if not title:
        print("表不存在！")
        return
    query_data_sql = "select * from %s;" % table_name
    result = list(tools.op_mysql(query_data_sql))
    result.insert(0,title)
    excel_name = "%s_%s.xls" % (time.strftime("%Y%m%d%H%M%S"),table_name)
    write_excel(result,excel_name)


# if __name__ == '__main__':
#     main("nhy_user")
#     main("hym")
#     main("user_ljq")