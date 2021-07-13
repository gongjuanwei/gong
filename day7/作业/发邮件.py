import yamail
#邮箱
#pasword

username = "511402865@qq.com"
password = "hcapwuhzhzvhcaia"
host = "smtp.qq.com" #qq
# host = "smtp.163.com" #163
# host = "smtp.126.com" #qq

smtp = yamail.SMTP(host=host,user=username,password=password)
# smtp.send(to="1018934314@qq.com")
smtp.send(
    to=["1018934314@qq.com","1054114694@qq.com"],
    cc=["1490768397@qq.com","1164019076@qq.com"],
    subject="课后好好学习",
    contents="下课之后先吃饭，吃完饭明天好好学习。",
    attachments=["a.jpg","a.xls"]
)