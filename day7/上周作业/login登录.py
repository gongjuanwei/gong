import tools
import string

# for i in range(3):
#     username = input("username:").strip().lower()
#     password = input("password:").strip()
#     if len(username) == 0 or len(password) == 0:
#         print("账号/密码不能为空")
#     elif len(username) < 5 or len(username) > 10:
#         print("用户名长度在5-10之间")
#     elif len(password) not in range(6, 13):  # 6 7 8 9 10 11 12
#         print("密码的长度要在6-12直接")
#     elif not (set(password) & set(string.digits) and set(password) & \
#               set(string.ascii_uppercase) and set(password) & set(string.ascii_lowercase) \
#               and set(password) & set(string.punctuation)):
#         print("密码复杂度不对")
#     else:
#         query_user_sql = "select * from nhy_user where username='%s';" % username
#         user_info = tools.op_mysql(query_user_sql, all=False, data_type=2)
#         if not user_info:
#             print("用户不存在")
#         elif user_info.get("error_count") > 4:
#             print("错误次数过多")
#         elif user_info.get("password") == tools.my_md5(password):
#             print("登录成功！")
#             break
#         else:
#             update_user_error_count = "update nhy_user set error_count=error_count+1 where username='%s';" % username
#             tools.op_mysql(update_user_error_count)
#             print("密码错误！")
# else:
#     print("错误次数达到上限！")


def check_data(username, password):
    if len(username) == 0 or len(password) == 0:
        print("账号/密码不能为空")
    elif len(username) < 5 or len(username) > 10:
        print("用户名长度在5-10之间")
    elif len(password) not in range(6, 13):  # 6 7 8 9 10 11 12
        print("密码的长度要在6-12之间")
    elif not (set(password) & set(string.digits) and set(password) & \
              set(string.ascii_uppercase) and set(password) & set(string.ascii_lowercase) \
              and set(password) & set(string.punctuation)):
        print("密码复杂度不对")
    else:
        return True

def check_db(username, password):
    query_user_sql = "select * from nhy_user where username='%s';" % username
    user_info = tools.op_mysql(query_user_sql, all=False, data_type=2)
    if not user_info:
        print("用户不存在")
    elif user_info.get("error_count") > 4:
        print("错误次数过多")
    elif user_info.get("password") == tools.my_md5(password):
        print("登录成功！")
        return True
    else:
        update_user_error_count = "update nhy_user set error_count=error_count+1 where username='%s';" % username
        tools.op_mysql(update_user_error_count)
        print("密码错误！")



def main():
    for i in range(5):
        username = input("username:").strip().lower()
        password = input("password:").strip()
        if not check_data(username, password):
            continue
        if check_db(username, password):
            break
    else:
        print("错误次数过多")


if __name__ == '__main__':
    main()