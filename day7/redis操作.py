import redis
import json
r=redis.Redis(host="118.24.3.40",password="HK139bc&*",port=6379,db=4)
# r2=redis.Redis(host="118.24.3.40",password="HK139bc&*",port=6379,db=4,decode_responses=True)
# #decode_responses=True  自动转成字符串

# 字符串 string
# 哈希 hash 大字典{"student"：{"xiaohei":"xxx","xiaobai":"xxx"}}
#list

# r.set("gjw_jsion","sdffgjhjku",60)
## r.set("gjw_jsion","sdfsfsfsfsd")

# print(r.get("gjw_jsion"))
# r.delete("gjw_jsion")

#
# print(r.ttl("key_gjw_jsion"))#获取key的失效时间

# print(r.keys())#获取当前数据库里面所有的key
# print(r.keys("*_*"))#获取可以加条件
# print(r.exists("fmz_111"))#f返回0代表不存在，返回1代表存在
# print(r.type("fmz_111"))#查看这个key的类型
# r.expire("gjw_jsion",60)#设置key的失效时间
#
# hash类型
# r.hset("students","xiaohei",'{"id":7,"score":99}')
# r.hset("students","xiaobai",'{"id":8,"score":99}')

# c = {"gjw":33,"gjw":"999"}
# r.hmset("students",c)

print(r.hget("students","xiaobai"))##获取制定的key，查出来的数据都是：bytes类型
# print(r.hgetall("students"))##吧key里面的数据获取到
#
#
xb_info=r.hget("students","xiaobai")#获取指定的key
ret=r.hget("students","xiaobai")##吧d大key里面的数据都获取到
# print(ret)
# print(r.hgetall("students"))#吧d大key里面的数据都获取到

# r.hdel("students","xiaobai")#删除指定的小key
# r.delete("students")
# r.hexists("students","xiaobai")#判断里面的小key是否存在
# print(xb_info.decode())


# new_ret = {}
# for k,v in ret.items():
#     k = k.decode()
#     v = v.decode()
#     new_ret[k] = v
# print(new_ret)



# l = ['2', '1', '3']
# r.lpush("black_list",*l)#
r.lpush("black_list",'1')#从左边插入
# r.rpush("black_list","3")#从右边插入

print(r.lrange("gjw_jsion",0,-1))
print(r.lindex("news_nhy",0))
# r.lpush("black_list","2")
# r.delete("new_index_nhy")


# print(r.lrange("black_list",0,1))
# r.lpop("black_list") #从左边删
# r.rpop("black_list")#从右边删

# r.lset("black_list",11,"haaaaaa")#指定位置修改
# print(r.llen("black_list")) #取这个list的长度
# print(r.ltrim("black_list",0,8)) #删除列表里面的数据，除了你指定的范围
print(r.lrem("black_list",2,"1")) #删除指定的元素，key,次数，元素

#[1,1]

