import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square",
                    help="display a square of a given number",
                    type=int)

parser.add_argument("-v", "--verbosity",
                    type=int,
                    choices=[0, 1, 2],   # 限制 verbosity 可以接收的值
                    help="increase output verbosity")

args = parser.parse_args()
answer = args.square**2

if args.verbosity in [0, 1, 2]:
    print("{0} 的平方是 {1}".format(args.square,answer))


'''
PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse> python .\06_prog.py 2 -v 0
2 的平方是 4

PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse> python .\06_prog.py 2 -v 3
usage: 06_prog.py [-h] [-v {0,1,2}] square
06_prog.py: error: argument -v/--verbosity: invalid choice: 3 (choose from 0, 1, 2)

PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse> python .\06_prog.py -h
usage: 06_prog.py [-h] [-v {0,1,2}] square

positional arguments:
  square                display a square of a given number

optional arguments:
  -h, --help            show this help message and exit
  -v {0,1,2}, --verbosity {0,1,2}
                        increase output verbosity

'''