# -----------------------------------------------------
# Name: docx2wiki
# Description: 使用 PANDOC 批量转换 WORD 文档，
#              然后批量导入 MEDIAWIKI 系统。
#              【DOCX -> WIKI页面 -> MEDIAWIKI系统】
# Date: 2023.10.12
# ------------------------------------------------------
import glob
import logging.config
import os
import sys

import requests
import pandas as pd
from mediawiki.mediawiki_api import get_all_categories, create_or_edit_page, upload_file
from mediawiki.utils import backup_dirs, create_dirs

logging.config.fileConfig('logging.conf')
logger = logging.getLogger("log_docx2wiki")


def log_result(title, res):
    """
    页面更新的日志记录
    :param title: 页面标题
    :param res: post返回的响应
    :return:
    """
    if "error" == list(res.keys())[0] and "articleexists" == res['error']['code']:
        logger.info(f"页面 [{title}] 已存在，此次不会再创建该页面")
        return
    info = "页面 [{0}] 更新结果 ===》 {1}".format(title, res['edit']['result'])
    if res['edit']['result'] != "Success":
        raise Exception(info)
    logger.info(info)


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
        logger.info(f"开始转换 ===》 {docx}")

        file_name = "".join(docx.split(".")[:-1])

        # pandoc -V mainfont="SimSun" --reference-doc twocolumns.docx
        #        --extract-media=C:\Users\zgg\Desktop -o test.wiki .\test.docx
        # print(f"pandoc -V mainfont='SimSun' --reference-doc {reference_doc}
        # --extract-media={media_dir}\\{file_name} -o {out_dir}\\{file_name}.wiki {in_dir}\\{docx}")
        os.system(
            f"pandoc -V mainfont='SimSun' --reference-doc {reference_doc} --extract-media={media_dir}\\{file_name} -o {out_dir}\\{file_name}.wiki {in_dir}\\{docx}")

        logger.info(f"完成转换 ===》 {docx}")


def update_categories(session, api_url, user, passwd, wiki_category):
    """
    更新系统的分类页面
    :param session: 会话
    :param api_url: 系统接口
    :param user: 用户名
    :param passwd: 密码
    :param wiki_category: 包含分类及其内容的EXCEL文件   【分类名称首字母要大写，如TransCAD】
    :return:
    """
    # 在这个函数里都是仅创建新页面
    create_only = "y"
    # 读取并判断新分类及其内容，并新建新分类
    todo_categories = pd.read_excel(wiki_category, sheet_name="分类")
    for index, row in todo_categories.iterrows():
        title = "Category:" + row['分类名']
        content = row['分类页面内容']
        res = create_or_edit_page(session, title, content, api_url, user, passwd, create_only)
        log_result(title, res)


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
                res = f1.write(f"[[Category:{category}]]")
                info = "向 [{0}.wiki] 写入的字符数 ===》 {1}".format(title, res)
                if res == 0:
                    raise Exception(info)
                logger.info(info)


def change_pics_dir_in_wiki(wiki_file):
    """
    修改页面中的图片路径
    [[File:F:\a\test\media\test2/media/image1.png|325x302px]] -> [[File:image1.jpeg|501x480px]]
    :param wiki_file:
    :return:
    """
    # F:\a\test\out\test2.wiki
    # print(wiki_file)
    filename = os.path.basename(wiki_file).split(".")[0]
    path = os.path.dirname(wiki_file)
    tmp_wiki_file = path + r"\tmp.wiki"
    with open(wiki_file, encoding="utf-8") as f, open(tmp_wiki_file, "w", encoding="utf-8") as fnew:
        for line in f:
            if "[[File:" in line:
                # 取 image1.png|325x302px 部分，再拼一个文件名
                img_info = filename + "-" + line.split("/")[-1].split("]]")[0]
                newline = "[[File:" + img_info.capitalize() + "]]"
                fnew.write(newline)
                fnew.write("\n")
            else:
                fnew.write(line)
    os.remove(wiki_file)
    os.rename(tmp_wiki_file, wiki_file)
    logger.info(f"[{wiki_file}] 图片路径已修改完成")


def load(session, api_url, user, passwd, create_only, out_dir, wiki_category):
    """
    批量导入 MEDIAWIKI 系统
    :param session: 会话
    :param api_url: 系统接口
    :param user: 用户名
    :param passwd: 密码
    :param create_only: 仅创建页面，如果页面已存在，就返回error
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

        # 修改页面中的图片路径
        change_pics_dir_in_wiki(wiki_file)

        with open(wiki_file, encoding="utf-8", mode="r") as f2:
            content = f2.read()
            res = create_or_edit_page(session, title, content, api_url, user, passwd, create_only)
            log_result(title, res)

    # os.system(f"php maintenance/importTextFiles.php --overwrite --use-timestamp {out_dir}\\*.wiki")


def upload_pics(session, api_url, user, passwd, media_dir):
    """
    将 media 目录下的图片上传到系统
    :param session:
    :param api_url:
    :param user:
    :param passwd:
    :param media_dir:
    :return:
    """
    media_path = glob.glob(media_dir + "\\*\\media")
    # ['F:\\a\\test\\media\\test2\\media']
    # print(media_path)
    for path in media_path:
        filename = path.split("\\")[-2]
        medias = os.listdir(path)
        for media in medias:
            file_path = path + "\\" + media
            # F:\a\test\media\test2\media\test.png
            # print(file_path)
            res = upload_file(session, api_url, user, passwd, file_path, filename + "-" + media)
            info = "[{0}] 图片上传结果 ===》 {1}".format(file_path, res['upload']['result'])
            if res['upload']['result'] != "Success":
                raise Exception(info)
            logger.info(info)


def main():
    # 检查输入参数
    if len(sys.argv) != 8:
        raise Exception("请检查输入命令，正确格式： python docx2wiki.py /input /output /media url user passwd y")

    # 检查输入目录是否存在
    if not os.path.exists(sys.argv[1]):
        raise Exception("输入目录不存在！")

    in_dir = sys.argv[1]
    out_dir = sys.argv[2]
    media_dir = sys.argv[3]
    api_url = sys.argv[4]
    user = sys.argv[5]
    passwd = sys.argv[6]
    # 指定为y：表示如果页面已存在，就返回error，如果不存在，就创建
    # 指定为n：表示如果页面已存在，就可以覆盖页面，不会返回error，如果不存在，就创建
    create_only = sys.argv[7]

    wiki_category = "./data/wiki_category.xlsx"

    session = requests.Session()

    # 分别移动out_dir和media_dir目录下的内容到备份目录，并清空当前目录
    backup_dirs([out_dir, media_dir])
    # 目录不存在，就新建
    create_dirs([out_dir, media_dir])

    logger.info("=================== 开始转换 docx->wiki  ===================")
    docx2wiki(in_dir, out_dir, media_dir)
    logger.info("=================== 完成转换 docx->wiki  ===================")

    logger.info("=================== 开始更新分类页面 ===================")
    update_categories(session, api_url, user, passwd, wiki_category)
    logger.info("=================== 完成更新分类页面 ===================")

    logger.info("=================== 开始上传图片 ===================")
    upload_pics(session, api_url, user, passwd, media_dir)
    logger.info("=================== 完成上传图片 ===================")

    logger.info("=================== 开始导入页面 ===================")
    load(session, api_url, user, passwd, create_only, out_dir, wiki_category)
    logger.info("=================== 完成导入页面 ===================")


if __name__ == "__main__":
    main()
