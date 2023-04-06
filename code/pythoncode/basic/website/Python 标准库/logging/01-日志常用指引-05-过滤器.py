import logging

logger = logging.getLogger("simple-example")
logger.setLevel(logging.DEBUG)

sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)

f = logging.Filter(name="simple-example")
# f = logging.Filter(name="root")

fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
sh.setFormatter(fmt)

logger.addHandler(sh)
logger.addFilter(f)

logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')

logger.log(level=logging.INFO, msg='log info message')