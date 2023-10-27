# -----------------------------------------------------
# Name: docx2wiki
# Description: 使用 PANDOC 批量转换 WORD 文档，
#              然后批量导入 MEDIAWIKI 系统。
#              【DOCX -> WIKI页面 -> MEDIAWIKI系统】
# Date: 2023.10.12
# ------------------------------------------------------
import os
import sys

import requests
import pandas as pd
from mediawiki.mediawiki_api import get_all_categories, create_or_edit_page
from mediawiki.utils import backup_dirs, create_dirs


def docx2wiki(in_dir, out_dir, media_dir):
    """
    使用 pandoc 将 word 文件批量转换成 wiki 文件
    :param in_dir: 输入word文件目录
    :param out_dir: 输出wiki文件目录
    :param media_dir: 输出图片目录
    :return:
    """
    reference_doc = "./data/custom-reference.docx"
    docxs = os.listdir(in_dir)

    for docx in docxs:
        print(f"开始转换 ===》 {docx}")
        file_name = "".join(docx.split(".")[:-1])

        # pandoc -V mainfont="SimSun" --reference-doc twocolumns.docx
        #        --extract-media=C:\Users\zgg\Desktop -o test.wiki .\test.docx
        # print(f"pandoc -V mainfont='SimSun' --reference-doc {reference_doc}
        # --extract-media={media_dir}\\{file_name} -o {out_dir}\\{file_name}.wiki {in_dir}\\{docx}")
        os.system(
            f"pandoc -V mainfont='SimSun' --reference-doc {reference_doc} --extract-media={media_dir}\\{file_name} -o {out_dir}\\{file_name}.wiki {in_dir}\\{docx}")

        print(f"完成转换 ===》 {docx}")


def update_categories(session, api_url, user, passwd, wiki_category):
    """
    更新系统的分类页面
    :param session: 会话
    :param api_url: 系统接口
    :param user: 用户名
    :param passwd: 密码
    :param wiki_category: 包含分类及其内容的EXCEL文件
    :return:
    """
    # 读取系统已有的分类
    categories = get_all_categories(session, api_url, user, passwd)
    # print(categories)
    # 读取并判断新分类及其内容，并新建新分类
    todo_categories = pd.read_excel(wiki_category, sheet_name="分类")
    for index, row in todo_categories.iterrows():
        if row['分类名'] in categories: continue
        title = "Category:" + row['分类名']
        content = row['分类页面内容']
        res = create_or_edit_page(session, title, content, api_url, user, passwd)
        info = "{0} 分类页面更新结果 ===》 {1}".format(title, res)
        if res != "Success":
            raise Exception(info)
        print(info)


def add_categories_for_files(wiki, title, wiki_category):
    """
    在每个wiki文件最后，添加 [[Category:Name]] 字样，以 为页面分类
    :param wiki: 要分类的wiki页面
    :param title: 要分类的wiki页面的文件名
    :param wiki_category: 包含分类及其内容的EXCEL文件
    :return:
    """
    # 为每个wiki文件添加分类
    files_categories = pd.read_excel(wiki_category, sheet_name="页面分类")
    with open(wiki, encoding="utf-8", mode="a") as f1:
        for index, row in files_categories.iterrows():
            if row['文件名'] != title: continue
            for category in row[1:]:
                if pd.isnull(category): continue
                f1.write("\n")
                # print(f"[[Category:{category}]]")
                f1.write(f"[[Category:{category}]]")


def load(session, api_url, user, passwd, out_dir, wiki_category):
    """
    批量导入 MEDIAWIKI 系统
    :param session: 会话
    :param api_url: 系统接口
    :param user: 用户名
    :param passwd: 密码
    :param out_dir: 包含导入系统wiki文件的目录
    :param wiki_category: 包含分类及其内容的EXCEL文件
    :return:
    """

    items = os.listdir(out_dir)
    # 检查输入
    if len(items) == 0:
        raise Exception("请检查 output 目录是否有文件")

    for item in items:
        if item.split(".")[-1] != "wiki":
            raise Exception(f"output 目录下的 {item} 文件不是 wiki 文件")

        wiki_file = out_dir + "\\" + item
        # 防止文件名中含有点号 .
        title = "".join(item.split(".")[:-1])

        # 在每个wiki文件最后，添加 [[Category:Name]] 字样，以 为页面分类
        add_categories_for_files(wiki_file, title, wiki_category)

        with open(wiki_file, encoding="utf-8", mode="r") as f2:
            content = f2.read()
            res = create_or_edit_page(session, title, content, api_url, user, passwd)
            info = "{0} 分类页面更新结果 ===》 {1}".format(title, res)
            if res != "Success":
                raise Exception(info)
            print(info)

    # os.system(f"php maintenance/importTextFiles.php --overwrite --use-timestamp {out_dir}\\*.wiki")


def main():
    # 检查输入参数
    if len(sys.argv) !=7 :
        raise Exception("请检查输入命令，正确格式： python docx2wiki.py /input /output /media url user passwd")

    # 检查输入目录是否存在
    if not os.path.exists(sys.argv[1]):
        raise Exception("输入目录不存在！")

    in_dir = sys.argv[1]
    out_dir = sys.argv[2]
    media_dir = sys.argv[3]
    api_url = sys.argv[4]
    user = sys.argv[5]
    passwd = sys.argv[6]

    wiki_category = "./data/wiki_category.xlsx"

    session = requests.Session()

    # 分别移动out_dir和media_dir目录下的内容到备份目录，并清空当前目录
    backup_dirs([out_dir, media_dir])
    # 目录不存在，就新建
    create_dirs([out_dir, media_dir])

    print("=================== 开始转换 docx->wiki  ===================")
    docx2wiki(in_dir, out_dir, media_dir)
    print("=================== 完成转换 docx->wiki  ===================")

    print("=================== 开始更新分类页面 ===================")
    update_categories(session, api_url, user, passwd, wiki_category)
    print("=================== 完成更新分类页面 ===================")

    print("=================== 开始导入页面 ===================")
    load(session, api_url, user, passwd, out_dir, wiki_category)
    print("=================== 完成导入页面 ===================")


if __name__ == "__main__":
    main()
