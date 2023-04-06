import logging
import sys


def log_file():
    """
    自己指定日志等级：
        - 程序中写死
        - 命令行中指定
    :return:
    """
    # 命令行中指定：从命令行取到日志等级
    # loglevel = sys.argv[1]
    # numeric_level = getattr(logging, loglevel.upper(), None)
    # if not isinstance(numeric_level, int):
    #     raise ValueError('Invalid log level: %s' % loglevel)

    # logging.basicConfig(filename="20220414.log",level=logging.DEBUG)  # 追加写
    # logging.basicConfig(filename="20220414.log",filemode="w",level=logging.DEBUG) # 覆盖写
    logging.basicConfig(
        filename="otherfiles/20220414.log",
        filemode="w",
        # 【更改显示消息的格式】 时间、代码所在文件名、代码行号、日志级别名字、日志信息
        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        # 【更改日期/时间的格式】
        # format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
        # 控制日期/时间的格式
        datefmt='%Y:%m:%d %H:%M:%S',
        # 程序中写死
        level=logging.DEBUG)
    # 命令行中指定
    # level=numeric_level)

    logging.debug("this is a logging debug")
    logging.info("this is a logging info")
    logging.warning("this is a logging warning")
    logging.error("this is a logging error")


if __name__ == "__main__":
    log_file()

# 也可以在命令行指定，如  python 01-日志常用指引-01-将日志事件记录到文件.py INFO
