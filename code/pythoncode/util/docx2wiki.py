# -----------------------------------------------------
# Name: docx2wiki
# Description: 使用 PANDOC 批量转换 WORD 文档，
#              然后批量导入 MEDIAWIKI 系统。
#              【DOCX -> WIKI页面 -> MEDIAWIKI系统】
# Date: 2023.10.12
# ------------------------------------------------------
import os
import sys


def main():
    # 检查输入参数
    if len(sys.argv) < 2:
        raise Exception("请检查输入命令，正确格式： python docx2wiki.py /input /output /media")

    # 检查目录是否存在
    if not os.path.exists(sys.argv[1]):
        raise Exception("输入目录不存在！")

    in_dir = sys.argv[1]
    out_dir = sys.argv[2]
    media_dir = sys.argv[3]
    reference_doc = "data/twocolumns.docx"

    if not os.path.exists(out_dir):
        os.mkdir(out_dir)

    if not os.path.exists(media_dir):
        os.mkdir(media_dir)

    docxs = os.listdir(in_dir)
    print("=================== 转换开始 ===================")
    for docx in docxs:
        print(f"----------- 开始转换 {docx} -----------")

        file_name = docx.split(".")[0]
        # pandoc -V mainfont="SimSun" --reference-doc twocolumns.docx
        #        --extract-media=C:\Users\zgg\Desktop -o test.wiki .\test.docx
        print(f"pandoc -V mainfont='SimSun' --reference-doc {reference_doc} --extract-media={media_dir}\\{file_name} -o {out_dir}\\{file_name}.wiki {in_dir}\\{docx}")
        os.system(
            f"pandoc -V mainfont='SimSun' --reference-doc {reference_doc} --extract-media={media_dir}\\{file_name} -o {out_dir}\\{file_name}.wiki {in_dir}\\{docx}")

        print(f"----------- 完成转换 {docx} -----------")
    print("=================== 转换完成 ===================")

    print("=================== 导入开始 ===================")

    items = os.listdir(out_dir)
    # 检查输入
    if len(items) == 0:
        raise Exception("请检查 output 目录是否有文件")
    for item in items:
        if item.split(".")[-1] != "wiki":
            raise Exception(f"output 目录下的 {item} 文件不是 wiki 文件")

    os.system(f"php maintenance/importTextFiles.php --overwrite --use-timestamp {out_dir}\\*.wiki")

    print("=================== 导入完成 ===================")


if __name__ == "__main__":
    main()
