import requests
import traceback
from loguru import logger

class MyDict(dict):
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


class MyRequest:
    def __init__(self,url,params=None,data=None,headers=None,files=None,json=None,timeout=5):
        self.url = url
        self.params = params
        self.data = data
        self.headers = headers
        self.files = files
        self.json = json
        self.timeout = timeout
    def __get_response(self):
        try:
            ret = self.response.json()
        except:
            logger.warning("接口返回的不是json！无法转成字典！response：{}", self.response.content)
            return MyDict()
        logger.debug("接口返回数据:{}", ret)
        return MyDict(ret)

    def __request(self,method):
        logger.debug("url:{},params:{},data:{},json:{},files:{},headers:{}",self.url,self.params,self.data,self.json,self.files,self.headers)
        try:
            self.response = requests.request(method,url=self.url,params=self.params,data=self.data,
                             json=self.json,headers=self.headers,files=self.files,verify=False,timeout=self.timeout)
        except:
            logger.error("接口不通，请求出错,错误信息是:{}",traceback.format_exc())
            return MyDict()

        return self.__get_response()

    def get(self):
        return self.__request("get")
    def post(self):
        return self.__request("post")
    def put(self):
        return self.__request("put")
    def delete(self):
        return self.__request("delete")


if __name__ == '__main__':
    data = {"file":open("myDict.py",'rb')}
    r = MyRequest("http://118.24.3.41/api/file/file_uploa",files=data)
    # result = r.get()
    ret1 = r.post()