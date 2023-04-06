import argparse

parser = argparse.ArgumentParser()
# parser.add_argument("echo")   # 指定程序能够接受哪些命令行选项
parser.add_argument("echo", help="echo the string you use here")
args = parser.parse_args()

print(args.echo)


'''
PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse> python .\02_prog.py
usage: 02_prog.py [-h] echo
02_prog.py: error: the following arguments are required: echo

PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse> python .\02_prog.py --help
usage: 02_prog.py [-h] echo

positional arguments:
  echo

optional arguments:
  -h, --help  show this help message and exit
  
PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse> python .\02_prog.py echo
echo
PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse> python .\02_prog.py foo
foo

'''


'''
PS F:\CODE\pythoncode\basic\website\Python 标准库\argparse> python .\02_prog.py --help
usage: 02_prog.py [-h] echo

positional arguments:
  echo        echo the string you use here

optional arguments:
  -h, --help  show this help message and exit

'''