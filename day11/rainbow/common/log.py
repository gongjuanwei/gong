from loguru import logger
from conf import config


class Log:
    logger.add(config.log_path,level=config.log_level,encoding='utf-8',enqueue=True, rotation='1 day',retention='5 days')
    debug = logger.debug
    info = logger.info
    warning = logger.warning
    error = logger.error