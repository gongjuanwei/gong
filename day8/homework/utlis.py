import requests
import yamail
import time
import hmac
import hashlib
import base64
import urllib.parse
import redis
import pymysql
from day8.homework import const

def get_dd_sign():
    timestamp = str(round(time.time() * 1000))
    secret = 'SEC16003eafa395e73ddacece95ee6aa72f3eb22ff667a88197ff7c0533053e1225'
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    return timestamp,sign

def send_dd_msg(msg,at=None,at_all=False):

    data = {
        "msgtype": "text",
        "text": {
            "content": msg
        },
        "at": {
            "atMobiles": at,
            "isAtAll": at_all
        }
    }
    timestamp,sign = get_dd_sign()
    params = {
        "access_token":"02ba6dbc04ebc825bc6fede96941d42beb45c4e57120db41b824d2161a9e3a76",
        "timestamp":timestamp,
        "sign":sign
    }
    try:
        r = requests.post(const.ddurl,json=data,params=params)
    except:
        print("钉钉消息没有发送成功")
    else:
        if r.json().get("errcode")==0:
            return True
        else:
            print("钉钉消息没有发送成功，错误信息 %s" % r.text)


def send_mail(subject,msg,files=None):
    smtp = yamail.SMTP(host=const.host, user=const.username, password=const.password)
    smtp.send(
        to=const.to,
        cc=const.cc,
        subject=subject,
        contents=msg,
        attachments=files
    )



def get_redis():
    return redis.Redis(**const.redis_info,decode_responses=True)

def op_mysql(sql: str,all=True,data_type=1):
    #data_type是1的话，返回的是list，其他的返回字典
    connect = pymysql.connect(**const.mysql_info)
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