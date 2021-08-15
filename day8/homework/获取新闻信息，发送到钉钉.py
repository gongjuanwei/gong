#思路
#1、每次发送的时候都去查一条，记录发送的条数
#2、提前取n条，5000，
import requests,json,time
from day8.homework import const,utlis
import schedule


#1、获取5000条，存redis  获取新闻的
#2、获取一条，发送到群里，并且把这条数据，致为已发送
#3、直到5000条件都发送完，
def get_news(page,limit=const.news_limit):
    print("开始获取新闻")
    data = {"page":page,"count":limit}
    req = requests.post(const.news_url,data)
    news_list = req.json().get("result")
    print("获取新闻结束，共%s条"% len(news_list))
    return news_list

def save_news_to_redis(news_list):
    print("开始保存新闻到redis")
    r = utlis.get_redis()
    for news in news_list:
        news["status"] = 0
        news = json.dumps(news)
        r.lpush(const.news_list_key,news)
        print("%s保存完成" % news)
    print("所有新闻保存redis完成")


def format_msg(news):
    news.pop("image")
    msg = """
    新闻标题：{title}
    详情：{path}
    新闻时间：{passtime}
    """.format_map(news)
    return msg

def send_msg():
    r = utlis.get_redis()
    index = r.get(const.news_index_key) #1 5000   查询当前第几条的数据
    if not index or int(index)>const.news_limit:
        page = int(r.get(const.news_page_key)) if r.get(const.news_page_key) else 1
        index = 1
        news_list = get_news(page)
        save_news_to_redis(news_list)
        r.set(const.news_page_key,page+1)
    news = r.lindex(const.news_list_key,index)
    news = json.loads(news)
    news["status"] = 1 #把状态改成已发送
    msg = format_msg(news)
    utlis.send_dd_msg(msg)
    r.lset(const.news_list_key,index,json.dumps(news)) #修改发送状态
    r.set(const.news_index_key,int(index)+1)
    print("======",msg)
    print("消息发送完成")

if __name__ == '__main__':
    while True:
        send_msg()
        time.sleep(60*60)
