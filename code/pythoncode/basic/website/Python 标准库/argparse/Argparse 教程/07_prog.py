import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", 
                    help="display a square of a given number",
                    type=int)

parser.add_argument("-v", "--verbosity",
                    action="count",  # 引入了另一种动作 count，来数某一个可选参数出现了几次
                    help="increase output verbosity")

args = parser.parse_args()
answer = args.square**2

if args.verbosity == 2:
    print("the square of {} equals {}".format(args.square, answer))
elif args.verbosity == 1:
    print("{}^2 == {}".format(args.square, answer))
else:
    print(answer)

'''
# 不添加 -v 标志，这一标志的值会是 None
PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse> python .\07_prog.py 2
4

PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse> python .\07_prog.py 2 -v
2^2 == 4

PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse> python .\07_prog.py 2 -v
2^2 == 4

PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse> python .\07_prog.py 2 -vv
the square of 2 equals 4

PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse> python .\07_prog.py 2 -v -v
the square of 2 equals 4

PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse> python .\07_prog.py 2 -v -v -v
4

PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse> python .\07_prog.py 2 -v 1
usage: 07_prog.py [-h] [-v] square
07_prog.py: error: unrecognized arguments: 1

'''