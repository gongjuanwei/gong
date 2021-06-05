from urllib.request import urlopen
from urllib.parse import  urlencode,urljoin,quote,quote_plus,unquote,unquote_plus

url ="http://api.nnzhp.cn/api/user/stu_info"
data ={"stu_name":"xiaohei","age":18}
# req = urlopen(url,urlencode(data).encode())#发post请求
req =urlopen(url+'?'+urlencode(data))#发get请求
print(req.read().decode())


host ="http://api.nnzhp.cn/"
url =urljoin(host,'/api/login')
print(url)


host = "http://api.nnzhp.cn/?stu_name=小黑"
print(quote_plus(host))
print(quote(host))

