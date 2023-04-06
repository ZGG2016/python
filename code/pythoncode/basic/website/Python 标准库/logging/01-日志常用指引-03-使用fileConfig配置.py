import logging.config

logging.config.fileConfig('otherfiles/logging.conf')

logger = logging.getLogger("fileconfig example")

logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')


