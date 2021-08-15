import loguru
from loguru import logger
import sys
# loguru.logger.info("aaaa")
# loguru.logger.debug("aaaa")
# loguru.logger.warning("aaaa")
# loguru.logger.error("aaaa")

logger.remove()  # 清除它的默认设置设置
# fmt = '{time}||{level}||{file.path}:line:{line}:function_name:{function} ||msg={message}'
fmt = '{time}||msg={message}'
# level file function module time message
logger.add(sys.stdout, level='DEBUG', format=fmt)  # 咱们本地运行的时候，在控制台打印
# #  enqueue=True  异步写入日志
logger.add('fmz.log', level='DEBUG', format=fmt, encoding='utf-8',
           enqueue=True, rotation='1 day', # rotation多久产生一个日志文件
           retention='10 days')  # 写在日志文件里面

logger.info("!!!!!!")



################定义一个日志类 ，debug级别
class Log:
    logger.remove()#清除它的默认设置设置
    fmt = '[{time}][{level}][{file.path}:line:{line}:function_name:{function}] ||msg={message}'
    #level file function module time message
    logger.add(sys.stdout,level="DEBUG",format=fmt)#咱们本地运行的时候，在控制台打印
    logger.add("test.log",level="DEBUG",format=fmt,encoding='utf-8',enqueue=True,rotation='1 day',retention='10 days')#写在日志文件里面

    debug = logger.debug
    info = logger.info
    warning = logger.warning
    error = logger.error

if __name__ == '__main__':
    Log.info("xxxx")