import time, hmac, base64, urllib, hashlib
import requests
import yamail
import traceback
from conf import config
from config_parse import YamlConfig
from log import Log


class DING:

    def __init__(self, tag):
        if tag not in config.dingding:
            Log.error("配置文件中钉钉的节点不存在，节点是{}", tag)
            raise KeyError("配置文件中钉钉的节点不存在")
        self.secret = config.dingding.get(tag).get("secret")
        self.access_token = config.dingding.get(tag).get("access_token")

    def get_dd_sign(self):
        timestamp = str(round(time.time() * 1000))
        secret_enc = self.secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, self.secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        return timestamp, sign

    def send_dd_msg(self, msg, at=None, at_all=False):
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
        timestamp, sign = self.get_dd_sign()
        params = {
            "access_token": self.access_token,
            "timestamp": timestamp,
            "sign": sign
        }
        try:
            r = requests.post(config.dd_url, json=data, params=params)
        except:
            Log.warning("钉钉发送消息没有成功！")
        else:
            if r.json().get("errcode") == 0:
                return True
            else:
                Log.warning("钉钉消息没有发送成功，错误信息 %s" % r.text)

    @classmethod
    def send_more_group(cls, msg, *args, at=None, at_all=False):
        for tag in args:
            dd_obj = cls(tag)
            dd_obj.send_dd_msg(msg, at, at_all)


def send_mail(subject, msg, files=None):
    email_info = YamlConfig.get_rainbow_config("email")
    try:
        smtp = yamail.SMTP(host=email_info.host, user=email_info.username, password=email_info.password)
        smtp.send(
            to=email_info.to,
            cc=email_info.cc,
            subject=subject,
            contents=msg,
            attachments=files
        )
    except:
        Log.error("发送邮件出错！{}", traceback.format_exc())


if __name__ == '__main__':
    # DING.send_more_group("这个是新写的函数！！","qa","dev",at_all=True)
    send_mail("你好呀，一会去吃饭", "你好呀，一会去吃饭")
