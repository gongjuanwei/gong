from loguru import logger
def log_filter(log_object):
    return log_object.get('level').name == "INFO"

class Log:
    file_name = "fmz"

    logger.add('%s-error.log' % file_name, level='ERROR', encoding='utf-8',
               enqueue=True, rotation='1 day',  # rotation多久产生一个日志文件
               retention='10 days')  # 写在日志文件里面
    logger.add('%s-info.log' % file_name, level='INFO', encoding='utf-8',
               enqueue=True, rotation='1 day',  # rotation多久产生一个日志文件
               retention='10 days', filter=lambda log_obj:log_obj.get('level').name == "INFO")  # 写在日志文件里面
    logger.add('%s-debug.log' % file_name, level='DEBUG', encoding='utf-8',
               enqueue=True, rotation='1 day',  # rotation多久产生一个日志文件
               retention='10 days')  # 写在日志文件里面

    debug = logger.debug
    info = logger.info
    warning = logger.warning
    error = logger.error

if __name__ == '__main__':

    Log.debug("hhhhh")