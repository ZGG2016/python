import argparse

parser = argparse.ArgumentParser()
# parser.add_argument("square", help="display a square of a given number")  #  argparse 会把我们传递给它的选项视作为字符串
parser.add_argument("square",  # 位置参数
                    help="display a square of a given number",
                    type=int)
args = parser.parse_args()

print(args.square**2)


'''
PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse> python .\03_prog.py 2
Traceback (most recent call last):
  File ".\03_prog.py", line 8, in <module>
    print(args.square**2)
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'

PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse> python .\03_prog.py 2
4

PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse> python .\03_prog.py two
usage: 03_prog.py [-h] square
03_prog.py: error: argument square: invalid int value: 'two'
'''