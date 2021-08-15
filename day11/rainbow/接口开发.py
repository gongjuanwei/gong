import flask
import json
#通过ip地址访问   http://192.168.31.224:8002/user/login
server = flask.Flask("abc")

@server.route('/user/login',methods=['post','get'])
def login():

    username=flask.request.values.get("username")
    age=flask.request.values.get("age")
    # print(flask.request.josn)#获取json的参数
    # print(flask.request.headers)#获取请求头数据
    # print(flask.request.cookies)#获取cookies内容

    print('username',username)
    print(age)

    data = {"code":0,"msg":"登录成功"}
    return json.dumps(data,ensure_ascii=False)


@server.route('/user/logout',methods=['post'])
def logout():
    data = {"code":0,"msg":"退出成功"}
    return json.dumps(data,ensure_ascii=False)


server.run(debug=True,port=8002,host='0.0.0.0')