import requests

url = "https://oapi.dingtalk.com/robot/send"

import time
import hmac
import hashlib
import base64
import urllib.parse

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
        r = requests.post(url,json=data,params=params)
    except:
        print("滴滴消息没有发送成功")
    else:
        if r.json().get("errcode")==0:
            return True


send_dd_msg("fmz,钉钉",at=None,at_all=False)