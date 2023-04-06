#-------------------------------------------------------------------------------
# Name:         opt_excel
# Description:  使用python操作excel
# Date:         2022.03.28
#-------------------------------------------------------------------------------


import time
import xlwt,xlrd
from xlutils.copy import copy

INPUT_PATH = "data/in.xls"

in_workbook = xlrd.open_workbook(INPUT_PATH)

print("--------------------------- 操作sheet ---------------------------")

# sheet1 = in_data.sheet_by_index(0)
# sheet1 = in_data.sheets()[0]
sheet1 = in_workbook.sheet_by_name("basci_info")

all_sheets_names = in_workbook.sheet_names()
print("in.xls 中所有的sheet 名为：%s " % all_sheets_names)
# in.xls 中所有的sheet 名为：['basci_info', 'address']

flag = in_workbook.sheet_loaded("basci_info")
print("载入 basci_info --> %s " % flag)
# 载入 basci_info --> True

print("--------------------------- 操作行 ---------------------------")

nrows = sheet1.nrows
print("sheet1 的总行数为：%d" %nrows)
# sheet1 的总行数为：8

print("第二行的所有单元格的内容为： %s " % sheet1.row(1))  # 索引从0开始
# 第二行的所有单元格的内容为 [text:'A', text:'male', number:15.0, text:'student']

print("第二行的第一列到第二列单元格的内容为： %s " % sheet1.row_slice(1,start_colx = 0,end_colx = 2))
# 第二行的第一列到第三列单元格的内容为 [text:'A', text:'male']

print("第二行的第一列到第二列单元格的类型为： %s " % sheet1.row_types(1,start_colx = 0,end_colx = 2))
# 第二行的第一列到第二列单元格的类型为： array('B', [1, 1])

print("第二行的第一列到第二列单元格的值为： %s " % sheet1.row_values(1,start_colx = 0,end_colx = 2))
# 第二行的第一列到第二列单元格的值为： ['A', 'male']

print("第二行共有 %d 个单元格 " % sheet1.row_len(1))
# 第二行共有 4 个单元格

print("--------------------------- 操作列 ---------------------------")

ncols = sheet1.ncols
print("sheet1 的总列数为：%d" %ncols)
# sheet1 的总列数为：4

print("第一列的第一行到第二行的单元格的内容为： %s " % sheet1.col(0, start_rowx=0, end_rowx=2))  # 索引从0开始
# 第一列的第一行到第二行的单元格的内容为： [text:'name', text:'A']

print("第一列的第一行到第二行的单元格的内容为： %s " % sheet1.col_slice(0, start_rowx=0, end_rowx=2))
# 第一列的第一行到第二行的单元格的内容为： [text:'name', text:'A']

print("第一列的第一行到第二行的单元格的类型为： %s " % sheet1.col_types(0, start_rowx=0, end_rowx=2))
# 第一列的第一行到第二行的单元格的类型为： [1, 1]

print("第一列的第一行到第二行的单元格的值为： %s " % sheet1.col_values(0, start_rowx=0, end_rowx=2))
# 第一列的第一行到第二行的单元格的值为： ['name', 'A']


print("--------------------------- 操作单元格 ---------------------------")


print("单元格(1,0)的内容为 %s " % sheet1.cell(1,0))

print("单元格(1,0)的类型为 %s " % sheet1.cell_type(1,0))

print("单元格(1,0)的值为 %s " % sheet1.cell_value(1,0))

print("--------------------------- 追加写入 ---------------------------")

# nt = copy(in_data)
# worksheet = nt.get_sheet(0)
# worksheet.write(8,0,"H")
# print("追加写入成功....")
# nt.save('resource/out_append.xls')

"""
nt = copy(Sheet1)

报错：AttributeError: 'Sheet' object has no attribute 'datemode'
copy的参数，是对应的workbook，而不是xls的filename。
"""

print("--------------------------- 列转换成行 ---------------------------")

workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('Sheet1')
# for col in range(0, ncols):
#     i = 0
#     for item in sheet1.col_values(col):
#         worksheet.write(col, i, item)
#         i += 1
# workbook.save("resource/out.xls")
# print("列转换成行成功....")

print("--------------------------- 写入公式 ---------------------------")

worksheet2 = workbook.add_sheet('Sheet2')
worksheet2.write(0,0, 4)
worksheet2.write(0,1, 5)
worksheet2.write(1,0,xlwt.Formula('A1*B1'))
worksheet2.write(1,1,xlwt.Formula('A1+B1'))
workbook.save("resource/out.xls")
print("公式写入成功....")

print("--------------------------- 其他写入属性 ---------------------------")


def write_property_function():
    i = 0
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('sheet1', cell_overwrite_ok=True)
    # 如果出现报错：Exception: Attempt to overwrite cell: sheetname='sheet1' rowx=0 colx=0
    # 需要加上：cell_overwrite_ok=True)
    # 这是因为重复操作一个单元格导致的

    while i < 64:
        # 为样式创建字体
        font = xlwt.Font()

        # 字体类型
        font.name = 'name Times New Roman'
        # 字体颜色
        font.colour_index = i
        # 字体大小，11为字号，20为衡量单位
        font.height = 20 * 11
        # 字体加粗
        font.bold = False
        # 下划线
        font.underline = True
        # 斜体字
        font.italic = True

        # 设置单元格对齐方式
        alignment = xlwt.Alignment()
        # 0x01(左端对齐)、0x02(水平方向上居中对齐)、0x03(右端对齐)
        alignment.horz = 0x02
        # 0x00(上端对齐)、 0x01(垂直方向上居中对齐)、0x02(底端对齐)
        alignment.vert = 0x01

        # 设置自动换行
        alignment.wrap = 1

        # 设置边框
        borders = xlwt.Borders()
        # 细实线:1，小粗实线:2，细虚线:3，中细虚线:4，大粗实线:5，双线:6，细点虚线:7
        # 大粗虚线:8，细点划线:9，粗点划线:10，细双点划线:11，粗双点划线:12，斜点划线:13
        borders.left = 1
        borders.right = 2
        borders.top = 3
        borders.bottom = 4
        borders.left_colour = i
        borders.right_colour = i
        borders.top_colour = i
        borders.bottom_colour = i

        # 设置列宽，一个中文等于两个英文等于两个字符，11为字符数，256为衡量单位
        sheet.col(1).width = 11 * 256

        # 设置背景颜色
        pattern = xlwt.Pattern()
        # 设置背景颜色的模式
        pattern.pattern = xlwt.Pattern.SOLID_PATTERN
        # 背景颜色
        pattern.pattern_fore_colour = i

        # 初始化样式
        style0 = xlwt.XFStyle()
        style0.font = font

        style1 = xlwt.XFStyle()
        style1.pattern = pattern

        style2 = xlwt.XFStyle()
        style2.alignment = alignment

        style3 = xlwt.XFStyle()
        style3.borders = borders

        # 设置文字模式
        font.num_format_str = '#,##0.00'

        sheet.write(i, 0, u'字体', style0)
        sheet.write(i, 1, u'背景', style1)
        sheet.write(i, 2, u'对齐方式', style2)
        sheet.write(i, 3, u'边框', style3)

        # 合并单元格，合并第2行到第4行的第4列到第5列
        sheet.write_merge(2, 4, 4, 5, u'合并')
        i = i + 1

    book.save('test_file' + time.strftime("%Y%m%d%H%M%S") + '.xls')