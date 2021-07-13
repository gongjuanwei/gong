#1、获取群里所有人的信息
#2、判断是否有群昵称，当作下载图片的名称
#3、下载qq头像
# https://qun.qq.com/cgi-bin/qun_mgr/search_group_members
# gc:1078641913
# st:0
# end:40
# sort:0
# bkn:1251707812
# cookie: RK=eQZhxBp/Yw; ptcz=74711de1d1efdb2e31eda884cee42e9c08a8be4d89fae2663bd9055ce7fd8262; pgv_pvid=4966592960; uin=o0511402865; skey=@W8Opc4q5t; p_uin=o0511402865; pt4_token=uFWlyRQ7Flj*YFXk-XP6quUMAKHJ7-UZPs4XMLr7DEY_; p_skey=mSNrvzOwIwJamRU*6G-j5ptMGDcQ2VvUsZUNHsAGuS8_; traceid=d071397d63
# https://q4.qlogo.cn/g?b=qq&nk=549313033&s=140

import requests,os
from day8.homework import const
BKN = "1251707812"
HEADERS = {"cookie":"RK=eQZhxBp/Yw; ptcz=74711de1d1efdb2e31eda884cee42e9c08a8be4d89fae2663bd9055ce7fd8262; pgv_pvid=4966592960; uin=o0511402865; skey=@W8Opc4q5t; p_uin=o0511402865; pt4_token=uFWlyRQ7Flj*YFXk-XP6quUMAKHJ7-UZPs4XMLr7DEY_; p_skey=mSNrvzOwIwJamRU*6G-j5ptMGDcQ2VvUsZUNHsAGuS8_; traceid=d071397d63"}

def get_members(gc,):
    all_members = {} #存放所有qq号和昵称
    st = 0
    end = 20
    while True:
        data = {"st":st,"end":end,"sort":0,"bkn":BKN,"gc":gc}
        req = requests.post(const.member_url,data,headers = HEADERS)
        members = req.json().get("mems")
        if members:
            for mem in members:
                qq = mem.get("uin")
                nick = mem.get("card") if mem.get("card") else mem.get("nick")
                all_members[qq] = nick
        else:
            return all_members
        st = st+40+1
        end = st+40

print(get_members(964880167))



def down_load_file(url,file_name):
    try:
        req = requests.get(url)
    except:
        print("下载出错，url：%s" % url)
    else:
        with open(file_name,"wb") as fw:
            print("%s 下载完成" % file_name)
            fw.write(req.content)




def main(gc):
    gc = str(gc)
    all_members = get_members(gc)
    if not os.path.exists(gc):
        os.mkdir(gc)
    os.chdir(gc)
    for qq,file_name  in all_members.items():
        url = const.image_url % qq
        file_name = file_name + ".jpg"
        down_load_file(url,file_name)
        print("下载完成")



print(main(964880167))

#
#
#1790211397
# if __name__ == '__main__':
#     main(964880167)
