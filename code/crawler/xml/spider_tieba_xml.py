from urllib import request,parse

import requests
from lxml import etree

# 爬取贴吧图片

def writeImage(link):
    """
    将html内容写入到本地
    :param link:
    :return:
    """
    # 6.发送请求，获取图片的服务器响应文件
    response_image = requests.get(link)

    filename = link[-10:]
    # 写入到本地磁盘文件内
    path = "out//%s " % filename
    # 7.写入文件
    with open(path, "wb") as f:
        f.write(response_image.content)
    print("已经成功下载 " + path)

def loadLink(link):
    """
    取出每个帖子里的每个图片连接
    :param link:
    :return:
    """
    # 4.发送请求，获取帖子的链接的服务器响应文件
    response = requests.get(link)
    response.encoding = 'utf8'

    content = etree.HTML(response.text)
    # 5.分析页面，过滤出图片的链接
    link_list = content.xpath('//img[@class="BDE_Image"]/@src')
    for link in link_list:
        writeImage(link)

def loadPage(fullUrl):
    """
    根据url发送请求，获取服务器响应文件
    :param fullUrl:
    :return:
    """

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 Edg/83.0.478.44",
    }
    # 2.发送请求，网页链接的服务器响应文件
    response = requests.get(fullUrl)
    response.encoding = 'utf8'

    # 解析html 为 HTML 文档
    content = etree.HTML(response.text)
    # 3.分析页面，过滤出参数，拼接获取每个帖子的链接
    link_list = content.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')
    #link_list = content.xpath('//div[@class ="threadlist_lz clearfix"]/div/a/@href')
    #print(link_list)
    for link in link_list:
        fulllink = "http://tieba.baidu.com" + link
        #print(fulllink)
        loadLink(fulllink)

def tiebaSpider(url, startPage, endPage):
    """
        作用：贴吧爬虫调度器，负责组合处理每个页面的url
        url : 贴吧url的前部分
        startPage : 起始页
        endPage : 结束页
    """
    for page in range(startPage, endPage + 1):
        # 1.分析网页链接，发现规律
        # http://tieba.baidu.com/f?kw=%E7%BE%8E%E5%A5%B3&pn=0
        fullUrl = url + "&" + "pn=%s" % str((page - 1) * 50)
        #print(fullUrl)
        loadPage(fullUrl)
        # print html

        print("谢谢使用")


if __name__ == "__main__":

    tiebaName = input("请输入贴吧名称：")
    startPage = int(input("请输入开始页码："))
    endPage = int(input("请输入结束页码："))
    name = {"kw": tiebaName}
    url = "http://tieba.baidu.com/f?" + parse.urlencode(name)

    tiebaSpider(url, startPage, endPage)

