import argparse

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('integers',
                    metavar='N',
                    type=int,
                    nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum',
                    dest='accumulate',
                    action='store_const',
                    const=sum,
                    default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))

'''
PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse\argparse --- 命令行选项、参数和子命令解析器> python .\01_示例.py -h
usage: 01_示例.py [-h] [--sum] N [N ...]

Process some integers.

positional arguments:
  N           an integer for the accumulator

optional arguments:
  -h, --help  show this help message and exit
  --sum       sum the integers (default: find the max)

PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse\argparse --- 命令行选项、参数和子命令解析器> python .\01_示例.py 1 2 3 4
4

PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse\argparse --- 命令行选项、参数和子命令解析器> python .\01_示例.py 1 2 3 4 --sum
10

PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse\argparse --- 命令行选项、参数和子命令解析器> python .\01_示例.py a b c d
usage: 01_示例.py [-h] [--sum] N [N ...]
01_示例.py: error: argument N: invalid int value: 'a'

'''