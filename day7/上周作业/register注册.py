import tools,login登录

def check_data(username,password,cpassword):

    if login登录.check_data(username,password) and password == cpassword:
        return True

def check_db(username, password):
    query_user_sql = "select * from nhy_user where username='%s';" % username
    user_info = tools.op_mysql(query_user_sql, all=False, data_type=2)
    if user_info:
        print("用户已存在")
        return
    md5_password = tools.my_md5(password)
    create_user_sql = "insert into nhy_user (username,password) values ('%s','%s');" % (username,md5_password)
    tools.op_mysql(create_user_sql)
    print("注册成功！")
    return True


def main():
    for i in range(5):
        username = input("username:").strip().lower()
        password = input("password:").strip()
        cpassword = input("cpassword:").strip()
        if not check_data(username,password,cpassword):
            continue
        if check_db(username,password):
            break
    else:
        print("错误次数过多")


if __name__ == '__main__':
    main()
