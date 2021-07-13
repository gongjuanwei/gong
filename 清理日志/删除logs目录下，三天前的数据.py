# os.path.getctime(('M2.py'))#获取文件创建时间
# os.remove()#删除文件
#获取某个目录下面的内容cur_path=当前目录、dirs文件夹、files文件
# for cur_path,dirs,files in os.walk("C:/Users/Administrator/.PyCharm2017.2/gong/day5"):
#     print(cur_path,dirs,files)
import os
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
    :param timestame: 时间戳
    :param format: 时间格式 %Y-%m-%d %H:%M:%S
    :return: 返回的是格式化好的时间，如果不传时间戳，那么返回当前的时间
    '''
    if timestame:
        time_tuple = time.localtime(timestame)
        return time.strftime(format,time_tuple)
    return time.strftime(format)


def clean_log(path):


clean_log('r"C:\\Users\\Administrator\\.PyCharm2017.2\\gong\\清理日志"')