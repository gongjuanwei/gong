import requests
#发k-v请求
# url ="http://api.nnzhp.cn/api/user/stu_info"
# data ={"stu_name":"x小黑"}
# req =requests.get(url,data)

#发post请求
# url = "http://api.nnzhp.cn/api/user/login"
# data = {"username":"niuhanyang","passwd":"aA123456"}
# data2 ={"version":2}
# req =requests.post(url,params=data2,data=data)

#发json请求
# url = "http://api.nnzhp.cn/api/user/add_stu"
# data = {
#       "grade": "飞马座",
#       "phone": "15676767678",
#     "name":"json请求"
# }
# req = requests.post(url,json=data)

#吧cooke转成字典
# s="RK=XYYhgDpPfy; ptcz=a5b23b4f93bc2f304119957286b77b21be95814358d482ef0a2bf216733e57ba; pgv_pvid=5931324545; uin=o0511402865; skey=@HHempil2m; p_uin=o0511402865; pt4_token=tkeLBl-znMjpBJxIv1Chj*kLx7p0dsh4BkZfF39cpDk_; p_skey=OS7gS9Zw8*r*aIpqd5-S5BUo65EJMNWRkLLMO1Vpu5o_; traceid=5b35fe5632"

#发cookies请求
# url = "https://qun.qq.com/cgi-bin/qun_mgr/search_group_members"
# data = {
# "gc": 180208520,
# "st": "21",
# "end": "41",
# "sort": 0,
# "bkn": "1391997515"
# }
# cookie ={'RK': 'XYYhgDpPfy', 'ptcz': 'a5b23b4f93bc2f304119957286b77b21be95814358d482ef0a2bf216733e57ba', 'pgv_pvid': '5931324545', 'uin': 'o0511402865', 'skey': '@HHempil2m', 'p_uin': 'o0511402865', 'pt4_token': 'tkeLBl-znMjpBJxIv1Chj*kLx7p0dsh4BkZfF39cpDk_', 'p_skey': 'OS7gS9Zw8*r*aIpqd5-S5BUo65EJMNWRkLLMO1Vpu5o_', 'traceid': '5b35fe5632'}
# req = requests.post(url,data,cookies=cookie)


#发head请求
# url = "https://qun.qq.com/cgi-bin/qun_mgr/search_group_members"
# data = {
#     "gc": 180208520,
#     "st": "21",
#     "end": "41",
#     "sort": 0,
#     "bkn": "1391997515"
# }
# header = {"cookie":"RK=XYYhgDpPfy; ptcz=a5b23b4f93bc2f304119957286b77b21be95814358d482ef0a2bf216733e57ba; pgv_pvid=5931324545; uin=o0511402865; skey=@HHempil2m; p_uin=o0511402865; pt4_token=tkeLBl-znMjpBJxIv1Chj*kLx7p0dsh4BkZfF39cpDk_; p_skey=OS7gS9Zw8*r*aIpqd5-S5BUo65EJMNWRkLLMO1Vpu5o_; traceid=5b35fe5632"}
# req = requests.post(url,data,headers=header)

#上传文件请求
url = "http://api.nnzhp.cn/api/file/file_upload"
data = {"file":open("a.XLS", 'rb')}
req = requests.post(url,files=data)
print(req.json())  #返回字典，如果接口返回的不是json，那会报错

#下载文件请求
url = "http://aliimg.changba.com/cache/photo/941190975_200_200.jpg"



# print(req.json())  #返回字典
# print(req.text)  #返回的是字符串
# print(req.content)  #返回的是bytes
# print(req.status_code) #返回的是状态码
# print(req.cookies) #返回的是cookies
# # # print(req.beaders) #返回的是

