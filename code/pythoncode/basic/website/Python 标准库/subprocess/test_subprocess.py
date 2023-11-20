import sys, argparse

inp = sys.stdin.read()
print(inp) if inp else print("这是不输入参数的输出内容")

# parser = argparse.ArgumentParser(description='argparse testing')
# parser.add_argument('--name', '-n', type=str, default="bk", required=True, help="a programmer's name")
# args = parser.parse_args()
# print(args.name)
