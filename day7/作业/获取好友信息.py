import requests,xlwt

url ="https://qun.qq.com/cgi-bin/qun_mgr/get_friend_list"

data = {"bkn": 184450077}
header ={"cookie":"_qpsvr_localtk=0.1816897648404261; uin=o1425900631; skey=@P8pqt4MJP;RK=C2z5x2/aQQ; ptcz=85c3ce7e57ce994b1aa66a1c5817c07d26c349146ac8256a907e2e0bab4a96d9; p_uin=o1425900631; pt4_token=BiU*UTk5T9ct8B-1queKD4PfIxG-7-sT9WMH0oaJf3s_; p_skey=1Dgn-BJzyfMjFgRBk8CnVX0I5cvej01GMfvtB*gNY5I_; traceid=937c394b6e"}

req = requests.post(url,data,headers=header)
result = req.json().get("result")

book = xlwt.Workbook()


for index,g_info in result.items():
    g_mems = g_info.get("mems") #list
    g_name = g_info.get("gname") if g_info.get("gname") else "默认分组"
    sheet = book.add_sheet(g_name)
    print("当前取的分组是===================",g_name)
    for col,mem in enumerate(g_mems):
        nick = mem.get("name")
        qq = mem.get("uin")
        sheet.write(col,0,nick)
        sheet.write(col,1,qq)
        # print("%s => %s" % (nick,qq))

book.save("qq.xls")