member_url = "https://qun.qq.com/cgi-bin/qun_mgr/search_group_members"
image_url = "https://q4.qlogo.cn/g?b=qq&nk=%s&s=140"

news_url = "https://api.apiopen.top/getWangYiNews"
ddurl = "https://oapi.dingtalk.com/robot/send"

redis_info = {
    "host":"118.24.3.40",
    "port":6379,
    "db":0,
    "password":"HK139bc&*"
}
news_limit =  2
news_list_key = "news_nhy"
news_index_key = "new_index_nhy" #存取到第几条
news_page_key = "new_page_nhy"  #存该去第几页
error_user_id_key = "error_users_nhy" #存放错误的userid


username = "511402865@qq.com"
password = "hcapwuhzhzvhcaia"
host = "smtp.qq.com"  # qq

to = ["1018934314@qq.com", "1054114694@qq.com","511402865@qq.com"]
cc = ["1490768397@qq.com", "1164019076@qq.com"]


mysql_info = {
 "host": "118.24.3.40",
  "user": "jxz",
  "password": "123456",
  "port": 3306,
  "db": "jxz",
  "autocommit": True,
  "charset": "utf8"
}