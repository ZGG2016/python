# 结合位置参数和可选参数

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square",  # 位置参数
                    help="display a square of a given number",
                    type=int)

parser.add_argument("--verbose",  # 可选参数
                    help="increase output verbosity",
                    action="store_true")

args = parser.parse_args()
answer = args.square**2

if args.verbose:
    print("{0} 的平方是 {1}".format(args.square,answer))
else:
    print(answer)


'''
PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse> python .\05_prog.py
usage: 05_prog.py [-h] [--verbose VERBOSE] square
05_prog.py: error: the following arguments are required: square

PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse> python .\05_prog.py 2 --verbose
2 的平方是 4

# 顺序无关紧要
PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse> python .\05_prog.py --verbose 2
2 的平方是 4


PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse> python .\05_prog.py 2
4
'''