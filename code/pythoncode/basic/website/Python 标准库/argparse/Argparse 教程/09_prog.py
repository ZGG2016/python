import argparse

parser = argparse.ArgumentParser(description="calculate X to the power of Y")  # 告诉你的用户这个程序的主要目标
group = parser.add_mutually_exclusive_group()  # 允许我们指定彼此相互冲突的选项， --verbose  --quiet

group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x**args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print("{} to the power {} equals {}".format(args.x, args.y, answer))
else:
    print("{}^{} == {}".format(args.x, args.y, answer))


'''
PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse> python .\09_prog.py 2 3
2^3 == 8

PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse> python .\09_prog.py 2 3 -q
8

PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse> python .\09_prog.py 2 3 -v
2 to the power 3 equals 8

PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse> python .\09_prog.py 2 3 -v -q
usage: 09_prog.py [-h] [-v | -q] x y
09_prog.py: error: argument -q/--quiet: not allowed with argument -v/--verbose

PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse> python .\09_prog.py 2 3 -v --quiet
usage: 09_prog.py [-h] [-v | -q] x y
09_prog.py: error: argument -q/--quiet: not allowed with argument -v/--verbose

PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse> python .\09_prog.py -h
usage: 09_prog.py [-h] [-v | -q] x y

calculate X to the power of Y

positional arguments:
  x              the base
  y              the exponent

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose
  -q, --quiet


'''