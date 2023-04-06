import logging

# create logger
module_logger = logging.getLogger('spam_application.auxiliary')


class Auxiliary:
    def __init__(self):
        self.logger = logging.getLogger('spam_application.auxiliary.Auxiliary')
        self.logger.info('正在创建一个 Auxiliary 实例（auxiliary_module模块里）')

    def do_something(self):
        self.logger.info('doing something（auxiliary_module模块里）')
        a = 1 + 1
        self.logger.info('done doing something（auxiliary_module模块里）')


def some_function():
    module_logger.info('received a call to "some_function" （auxiliary_module模块里）')