import datetime
import os
import logging
import logging.config

# LOGGING_DIR 日志文件存放目录
LOGGING_DIR = "otherfiles/logs/"
if not os.path.exists(LOGGING_DIR):
    os.mkdir(LOGGING_DIR)


def logger_dict_config():
    return {
        'version': 1,
        'loggers': {
            'dict_config_demo': {  # 后面导入时logging.getLogger使用的app_name
                'handlers': ['console', 'file_handler'],
                'level': 'DEBUG',
                'propagate': True,
            },
        },
        'handlers': {
            'console': {
                'level': 'ERROR',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
            'file_handler': {
                'level': 'INFO',
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': '%s/mylog.log %s' % (LOGGING_DIR, datetime.datetime.today().date()),
                'formatter': 'standard'
            }
        },
        'formatters': {
            'standard': {
                'format': '[%(levelname)s] [%(asctime)s] [%(filename)s] [%(funcName)s] [%(lineno)d] > %(message)s'
            },
            'simple': {
                'format': '[%(levelname)s] > %(message)s'
            },
        }
    }


def init_logger_dict_config():
    """
    配置日志
    """
    logging.config.dictConfig(logger_dict_config())
