import logging.config
from dict_logger import init_logger_dict_config

init_logger_dict_config()

logger = logging.getLogger("dict_config_demo")

# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warn message')
# logger.error('error message')
# logger.critical('critical message')


def test():
    try:
        print(1/0)
    except Exception as err:
        logger.error(str(err))


test()

