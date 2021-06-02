import json
import  pprint
#json是一个字符串


#python的数据类型字典转成json串
# d={"code":0,"msg":"操作成功","token":"xxxxx"}
# print(d)
# json_str =json.dumps(d,ensure_ascii=False)#dumps吧字典转成字符串
# print(json_str)
# pprint.pprint(json_str)# ensure_ascii=False不加次字段，就会吧中文转成unicode




#json转成Python的数据类型字典
# json_str='{"code": 0, "msg": "操作成功", "token": "xxxxx"}'#json串
# dic =json.loads(json_str)
# pprint.pprint(dic)



#直接读到文件内容
# with open("student.txt",encoding="utf-8") as f:
#     dic =json.loads(f.read())#把字符串转成字典
# pprint.pprint(dic)


#打开一个文件，写进字典
d={"code":0,"msg":"操作成功","token":"xxxxx","addr":"xxxx"}
# with open("student2.txt",'w',encoding="utf-8") as f:#打开一个文件
#        json_str=json.dumps(d,ensure_ascii=False,indent=4)#吧字典转成了一个字符串
#        f.write(json_str)


# json.load()#吧字符串转成字典，自动帮你读
with open("student2.json",encoding="utf-8") as f:
    result =json.load(f)
    print(result)

# json.dump()#吧字典转成字符串，自动帮你写
with open("student2.json",'w',encoding="utf-8") as f:
    json.dump(d,f,ensure_ascii=False,indent=4)