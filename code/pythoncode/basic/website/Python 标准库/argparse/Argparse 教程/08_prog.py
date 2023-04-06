import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square",
                    type=int,
                    help="display a square of a given number")

parser.add_argument("-v", "--verbosity",
                    action="count",
                    # 把它设置为 0 来让它可以与其他整数值相互比较。
                    default=0,
                    help="increase output verbosity")

args = parser.parse_args()
answer = args.square**2

if args.verbosity >= 2:
    print("the square of {} equals {}".format(args.square, answer))
elif args.verbosity >= 1:
    print("{}^2 == {}".format(args.square, answer))
elif args.verbosity == 0:
    print("=====")
else:
    print(answer)

'''
PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse> python .\08_prog.py 2
=====
PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse> python .\08_prog.py 2 -v
2^2 == 4
PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse> python .\08_prog.py 2 -v -v
the square of 2 equals 4

'''