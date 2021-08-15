import redis
r=redis.Redis(host="118.24.3.40",password="HK139bc&*",port=6379,db=4,decode_responses=True)
r2=redis.Redis(host="118.24.3.40",password="HK139bc&*",port=6379,db=13,decode_responses=True)

# r.flushdb() #清空当前数据库
# r.flushall() #清空所有数据库


for k in r.keys():
    # 获取key
    k_type = r.type(k)
    #判断获取的数据是什么类型
    if k_type == "string":
        value = r.get(k)
        r2.set(k,value)
    elif k_type == "hash":
        dic = r.hgetall(k)
        r2.hmset(k,dic)
    elif k_type == "list":
        l_len = r.llen(k)
        result = r.lrange(k,0,l_len)
        r2.rpush(k,*result)



