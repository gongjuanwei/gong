# 1、获取表里面所有error_count大于等与5的，并且不在redis里面的用户id
# 2、把这一批用户的userid放到redis里面
# 3、发送钉钉
import time
from day8.homework.utlis import get_redis,op_mysql,send_dd_msg,send_mail
from day8.homework.const import error_user_id_key

def get_error_user():
    print("开始获取错误用户")
    r = get_redis()
    error_userids = tuple(r.lrange(error_user_id_key,0,-1)) #获取全部的
    if error_userids:
        sql = "select * from fmz_hym where error_count >=5 and id not in %s ; " % str(error_userids)
    else:
        sql = "select * from fmz_hym where error_count >=5 ;"
    print("sql",sql)
    data = op_mysql(sql, data_type=2)
    print("获取错误用户完成，总共%s条" % len(data))
    return data  #[ {id:1,username:xxx,} ]


def format_msg(user_list):
    all_msg = ""
    user_ids = []
    for user in user_list:
        msg = "用户id:%s,用户名：%s\n" % (user.get("id"),user.get("username"))
        all_msg+=msg
        user_ids.append(user.get("id"))
    return all_msg,user_ids


def send_error_user():
    r = get_redis()
    error_user = get_error_user()
    if not error_user: #没有错误用户的
        send_dd_msg("当前时间没有错误次数超过5次的用户")
        send_mail("登录错误用户提醒","当前时间没有错误次数超过5次的用户")
        return
    msg,userids = format_msg(error_user)
    r.lpush(error_user_id_key,*userids) #存到redis里面
    send_dd_msg("登录错误用户提醒:%s" % msg)
    send_mail("登录错误用户提醒", "登录错误用户提醒:%s" % msg)
    print("发送完成")

def clear_error_user():
    sql = "update user_hym set error_count = 0;"
    op_mysql(sql)
    r = get_redis()
    r.delete(error_user_id_key)


if __name__ == '__main__':
    while True:
        send_error_user()
        time.sleep(60*10)