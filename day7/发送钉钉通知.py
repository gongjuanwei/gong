import requests
url = "https://oapi.dingtalk.com/robot/send?access_token=02ba6dbc04ebc825bc6fede96941d42beb45c4e57120db41b824d2161a9e3a76"
data={
    "msgtype": "text",
    "text": {
        "content": "fmz,钉钉"
    }
}
req = requests.post(url,json=data)
print(req)
