# -------------------------------------------------------------------------------
# Name:         util
# Description:  一些即用的工具方法
# Date:         2022.03.28
# -------------------------------------------------------------------------------

import os
import sys
import time
from string import Template

import cx_Oracle


class BatchRename(Template):
    delimiter = '%'


# 批量修改文件名称
def change_files_name(path):
    fmt = input('Enter rename file style :  ')
    # %{d}_%{n}%{f}

    ext = '.csv'
    t = BatchRename(fmt)
    date = time.strftime('%d%H%M%S')
    file_lst = os.listdir(path)
    for ind, file_name in enumerate(file_lst):
        newname = t.substitute(d=date, n=ind, f=ext)
        print('{0} --> {1}'.format(file_name, newname))
        os.rename(path + file_name, path + newname)


# 获取文件的行数
def get_row_nums(path):
    if '.csv' in path:  # 取文件
        count = 0
        with open(path, 'r') as f:
            while f.readline():
                count += 1
        print(count)
    else:  # 取目录
        count = 0
        file_lst = os.listdir(path)
        for file_name in file_lst:
            if 'rkll' not in file_name: continue

            file_path = os.path.join(path, file_name)
            with open(file_path, 'r') as f:
                while f.readline():
                    count += 1
        print(count)


# 类型检查
def displayNumType(num):
    print(num, 'is', )
    if isinstance(num, (int, float, complex)):
        print('a number of type:', type(num).__name__)
    else:
        print('not a number at all!!')


#  根据起终点取所在的区市县
def get_area(file_name):
    f2 = open("data/sichuan_city.txt", "r")
    lines = f2.readlines()
    flag = 0
    with open(file_name, "r") as f1:
        while True:
            item = f1.readline().strip()
            if not item:
                break
            for line in lines:
                lst = line.split("\t")
                if item in lst:
                    print(item.strip() + "\t" + lst[0] + "\t" + lst[2])
                    flag = 1
                    break
                else:
                    flag = 0
            if flag == 0:
                print(item)

    f2.close()


if __name__ == '__main__':
    path = sys.argv[1]

    change_files_name(path)

    # get_row_nums(path)

    # displayNumType(-69)
    # displayNumType(9999999999999999999999)
    # displayNumType(98.6)
    # displayNumType(-5.2 + 1.9j)
    # displayNumType('xxx')
