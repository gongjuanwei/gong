import xpinyin

# name ="曾瑞"
# p = xpinyin.Pinyin()
# pyin =p.get_pinyin(name,'')
#
# print(pyin)


#有一批名单，需要生成成账号，但是名字里面有名字拼音相同的，如果有重复的拼音，那么就名字依次+1
s = """周秀华
周建军
江玉
陈利
植勇
阚玉梅
牛畅
卢柳
钟婷婷
何浩
陈建
王帅
刘雪
王荣
魏颖
韩宁
张小红
单磊
张秀梅
黄东
罗平
侯伟
包英
郭秀华
刘燕
王洋
谢丽
王华
潘强
李婷
郑丽华
耿桂芳
李博
马浩
张静
韦坤
高杨
吕想
杨敏
毛金凤
杨波
李玉珍
刘杰
徐成
郑龙
李秀荣
王玉梅
萧慧
刘建
罗阳
吴艳
张雪梅
常静
王建国
李欢
纪玉英
朱桂荣
黄秀芳
陈斌
鲁洋
庞东
邵桂兰
徐金凤
杨岩
刘想
沈倩
陈瑞
王小红
覃桂芳
萧瑜
乔淑珍
张佳
鲁丽娟
李博
方佳
李华
李萍
孙秀兰
张雪
李颖
侯龙
刘静
龙涛
李建平
黄春梅
胡浩
冯玉梅
王云
杜淑珍
赵坤
刘荣
潘红
章畅
朱桂兰
张浩
卓彬
姚瑜
林凤兰
郑岩
梁平"""
name_pinyin_list=[]#存的不重复名字拼音
d ={}#存在重复的名字和出现的次数
all_name_list =s.split()#拿到名单转成list数组

p=xpinyin.Pinyin()
for name in all_name_list:
    name_pinyin =p.get_pinyin(name,'')
    if  name_pinyin not in name_pinyin_list:#
        name_pinyin_list.append(name_pinyin)
    # else:
    #     n ="%s1" % name_pinyin
    #     name_pinyin_list.append(n)

    else:
        if name_pinyin not in d:
            d[name_pinyin]=1
        else:
            d[name_pinyin]+=1

for name ,count in d.items():
    for i in range(1,count+1):
        new_name ="%s%s"%(name,i)
        name_pinyin_list.append(new_name)


print(name_pinyin_list)
print(len(name_pinyin_list))


