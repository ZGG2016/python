import argparse

# 编写用户友好的命令行接口

parser = argparse.ArgumentParser()
parser.parse_args()


'''
PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse> python .\01_prog.py -h
usage: 01_prog.py [-h]

optional arguments:
  -h, --help  show this help message and exit

PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse> python .\01_prog.py --verbose
usage: 01_prog.py [-h]
01_prog.py: error: unrecognized arguments: --verbose
'''

