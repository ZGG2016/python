from urllib import request,parse


def writeData(html,filename):
    """
    将爬取的数据写入文件
    :param html:
    :param filename:
    :return:
    """
    with open(filename,"w",encoding = 'utf8') as f:
        f.write(html)


def tiebaSpider(url,startPage,endPage):
    """
    爬取贴吧网页数据
    :param url:
    :param startPage:
    :param endPage:
    :return:
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0"
    }

    for page in range(startPage, endPage + 1):
        fullUrl = url + "&" + "pn=%s" % str((page - 1) * 50)
        req = request.Request(fullUrl, headers=headers)
        response = request.urlopen(req)
        html = response.read().decode()

        file = "out//page %s.txt" % str(page)
        writeData(html,file)


if __name__ == "__main__":
    # https://tieba.baidu.com/f?kw=%E6%88%90%E9%83%BD
    # https://tieba.baidu.com/f?kw=%E6%88%90%E9%83%BD&pn=50
    # https://tieba.baidu.com/f?kw=%E6%88%90%E9%83%BD&pn=100
    tiebaName = input("请输入贴吧名称：")
    startPage = int(input("请输入开始页码："))
    endPage = int(input("请输入结束页码："))
    name = {"kw": tiebaName}
    url = "https://tieba.baidu.com/f?" + parse.urlencode(name)

    tiebaSpider(url, startPage, endPage)

