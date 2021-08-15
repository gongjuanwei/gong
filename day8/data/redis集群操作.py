import rediscluster
startup_nodes = [
    {"host":"118.24.3.40","port":6379,"password":"HK139bc&*"},
    {"host":"118.24.3.41","port":6379,"password":"HK139bc&*"}
]
r = rediscluster.RedisCluster(startup_nodes=startup_nodes,decode_responses=True)
print(r.keys())