class MyDict(dict):
    # 对象在没有某个属性的话，会调用它
    def __getattr__(self, item):
        value = self.get(item)
        if type(value) == dict:
            value = MyDict(value)
        if isinstance(value,list) or isinstance(value,tuple):
            value = list(value)
            for index,v in enumerate(value):
                if isinstance(v,dict):
                    value[index] = MyDict(v)
        return value
        #是这个对象在没有某个属性的话，会调用它


if __name__ == '__main__':

        #魔法方法
    d1 = {"name":"wkf","addr":"北京","info":{"city":"深圳","cars":{"name":"bmw"}},
          "phones":({"name":"huawei","price":50000},{"name":"xiaomi","price":11})
          }

    d = MyDict(d1)
    print(d.name)
    print("addr..",d.addr)
    print(d)



# print(d.info.city)
# print(d.info.cars.name)
# print(d.addr)
