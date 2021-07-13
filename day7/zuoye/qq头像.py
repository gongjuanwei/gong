# 1、传入一个群号，把群里面所有人的头像下载到本地，放到群号的文件夹，头像的名称是群昵称/qq昵称
import requests,os
def get_qq_img(qq_number):
    url = "https://qun.qq.com/cgi-bin/qun_mgr/search_group_members"
    data = {"gc":964880167, "st": 0, "end": 20, "sort": 0, "bkn":2028428841}
    header = {"cookie": "tvfe_boss_uuid=28a318fd7d911f8e; pgv_pvid=5756845556; pac_uid=0_1edf16d3628ab; iip=0; RK=kwhcqCcrY4; ptcz=7f49c2246d7747e4faecc695280eaee9826c268cb43b6a3827eea52781301620; _qpsvr_localtk=0.2129546185515918; _tc_unionid=b8ab582e-ce47-4795-ab26-b44655e6f17c; pgv_info=ssid=s8971494512; traceid=318f4cbb07; uin=o1425900631; skey=@wfuSw5W4H; p_uin=o1425900631; pt4_token=AJE6IRIBgadsBz6VZ7eQnZNla2z5agGDizxG-bbxusw_; p_skey=bQ5SltfOF7-LITBYBBz001FyIi31TOQfq7bjaTrSfEE_"}
    mems = requests.post(url, data, verify=False, headers=header).json().get('mems')
    img_url = 'https://q4.qlogo.cn/g?b=qq&nk=%s&s=140'  # 下载图片的接口
            # https://q4.qlogo.cn/g?b=qq&nk=%s&s=140
            # https://q4.qlogo.cn/g?b=qq&nk=516902394&s=140
    if not os.path.exists(str(qq_number)):  # 文件夹的名字是字符串
           os.mkdir(str(qq_number))
    d = r'C:/Users/Think/PycharmProjects/gong/day7/zuoye/%s'%qq_number
    for mem in mems:
        qq = mem.get('uin')  # qq
        nick = mem.get('nick') if not mem.get('card') else mem.get('card')
        req = requests.get(img_url % qq)
        path = os.path.join(d, nick)
        print(path)
        f=open(path+'.jpg','wb')
        f.write(req.content)
        f.close()


get_qq_img(964880167)