import logging
import auxiliary_module

# 注意输出的 logger 名称

# 创建一个名为 spam_application 的 logger
logger = logging.getLogger('spam_application')
# 设置这个 logger 的日志等级为 DEBUG
# logger中设置的级别确定将传递给其处理程序的消息的严重性
logger.setLevel(logging.DEBUG)

# 创建一个文件 handler 来记录 debug 消息
fh = logging.FileHandler('otherfiles/spam.log')
# handler 中设置的级别确定处理程序将发送哪些消息
fh.setLevel(logging.DEBUG)

# # 创建一个控制台 handler 来记录 error 消息 (更高级别)
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# 创建 formatter，并添加给 handlers
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter = logging.Formatter('{asctime} - {name} - {levelname} - {message}', datefmt='%m/%d/%Y %I:%M:%S %p', style='{')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 将 handlers 添加给 logger
logger.addHandler(fh)
logger.addHandler(ch)

logger.info('正在创建一个 auxiliary_module.Auxiliary 实例')
a = auxiliary_module.Auxiliary()
logger.info('创建完成 auxiliary_module.Auxiliary 实例')

logger.info('正在调用 auxiliary_module.Auxiliary 的 do_something 方法')
a.do_something()
logger.info('完成 auxiliary_module.Auxiliary 的 do_something 方法')

logger.info('正在调用 auxiliary_module 的 some_function 方法')
auxiliary_module.some_function()
logger.info('完成 auxiliary_module 的 some_function 方法')