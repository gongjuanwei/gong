import time

#时间戳，计算机诞生那一天到现在过了多少秒  1621063294
#格式化好的时间

#2021515  --50天后的时间
# print(int(time.time()))#获取当前的时间戳
# print(time.strftime('%Y-%m-%d %H:%M:%S'))#获取当前格式化好的时间
# print(time.strftime('%y-%m-%d %H:%M:%S'))#获取当前格式化好的时间
# print(time.strftime('%Y-%m-%d '))#获取当前格式化好的时间
# print(time.strftime('%H:%M'))#获取当前格式化好的时间


#时间元组
#时间戳转格式化好的时间
# # time_tuple =time.gmtime(1621762357)#gmtime取的是标准时区的时间
# time_tuple1 =time.localtime(1621762488)#gmtime取的是当前时区的时间
# #时间戳转时间元组
# # time.strftime('%Y-%m-%d %H:%M:%S',time_tuple)
# # time.strftime('%Y-%m-%d %H:%M:%S',time_tuple1)
# # print(time.strftime('%Y-%m-%d %H:%M:%S',time_tuple))
# print(time.strftime('%Y-%m-%d %H:%M:%S',time_tuple1))
#
# #格式化好的时间转时间戳
# time_tuple2 =time.strptime('2021-05-15 17:14:51','%Y-%m-%d %H:%M:%S')#gmtime取的是标准时区的时间
# print(time_tuple2)
# print(int(time.mktime(time_tuple2)))



def str_to_timestamp(s=None,format='%Y-%m-%d %H:%M:%S'):
    '''
       :param s: 格式化好的时间，比如2021-5-16 17:06:32
       :param format: 时间格式 %Y-%m-%d %H:%M:%S
       :return: 返回的是一个时间戳，如果不传s，默认返回当前时间戳
       '''
    if s:
        time_tuple = time.strptime(s,format)
        return int(time.mktime(time_tuple))
    return int (time.time())

def timestamp_to_str(timestame=None,format="%Y-%m-%d %H:%M:%S"):
    '''
    :param  timestame: 时间戳
    :param  format: 时间格式 %Y-%m-%d %H:%M:%S
    :return: 返回的是格式化好的时间，如果不传时间戳，那么返回当前的时间
    '''
    if timestame:
        time_tuple = time.localtime(timestame)
        return time.strftime(format,time_tuple)
    return time.strftime(format)





