info={
    'lgy':{
        'age':18,
        'addr':'beijng',
        'cars':['bmw','ben-c','audi']
    },
    'fd':{
        'house':{
            'bj':['海定区','昌平区','朝阳区','西城区'],
            'sh':['静安区','徐汇区']
        },
        'money':5000
    }
}

info["lgy"]["cars"].append("tesla")
print(info)
#方丹 ，海定区房卖了，卖了500万
#方法一：用index找到下标，然后用pop删掉
index = info["fd"]["house"]['bj'].index("海定区")
info["fd"]["house"]["bj"].pop(index)

#方法二：直接用remove删掉
info["fd"]["house"]['bj'].remove("海定区")
info["fd"]["money"]+=5000
print(info)