import argparse

parser = argparse.ArgumentParser()
# parser.add_argument("--verbosity",  # 可选参数
#                     help="increase output verbosity")
#
# args = parser.parse_args()
#
# if args.verbosity:
#     print("verbosity turned on")

parser.add_argument("-v", "--verbose",
                    help="increase output verbosity",
                    action="store_true")  # 当这一选项存在时，为 args.verbose 赋值为 True。没有指定时则隐含地赋值为 False。
args = parser.parse_args()
if args.verbose:
    print("verbose turned on")

'''
PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse> python .\04_prog.py --verbosity 1
verbosity turned on

PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse> python .\04_prog.py --verbosity
usage: 04_prog.py [-h] [--verbosity VERBOSITY]
04_prog.py: error: argument --verbosity: expected one argument

PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse> python .\04_prog.py

PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse> python .\04_prog.py --help
usage: 04_prog.py [-h] [--verbosity VERBOSITY]

optional arguments:
  -h, --help            show this help message and exit
  --verbosity VERBOSITY
                        increase output verbosity

'''

'''
PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse> python .\04_prog.py --verbose
verbose turned on

PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse> python .\04_prog.py --verbose 1
usage: 04_prog.py [-h] [--verbose]
04_prog.py: error: unrecognized arguments: 1

PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse> python .\04_prog.py

PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse> python .\04_prog.py -v
verbose turned on

'''