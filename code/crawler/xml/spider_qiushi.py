import json

from lxml import etree
import requests

# 使用xpath爬取糗事百科段子
# xpath  模糊查询

url = "https://www.qiushibaike.com/text/page/1/"

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 Edg/83.0.478.44"
    }
txt = requests.get(url,headers = headers).text

html = etree.HTML(txt)

# 返回所有段子的结点位置，contains()模糊查询方法，第一个参数是要匹配的标签，第二个参数是标签名部分内容
node_list = html.xpath('//div[contains(@id,"qiushi_tag")]')
#print(len(name_list))
info = {}

with open("out//qiushi.json","w") as f:
    for node in node_list:
        # xpath返回的列表，这个列表就这一个参数，用索引方式取出来，用户名
        username = node.xpath('./div[@class="author clearfix"]//h2')[0].text.strip("\n")
        # 年龄
        age = node.xpath('./div/div[@class]')[0].text  # [0]
        #  取出标签下的内容,段子内容
        content = node.xpath('.//div[@class="content"]/span')[0].text.strip("\n")
        # 取出标签里包含的内容，点赞
        zan = node.xpath('./div[@class="stats"]//i')[0].text
        # 评论
        comments = node.xpath('./div[@class="stats"]//i')[1].text

        info = {
             "username": username,
             "age": age,
             "content": content,
             "zan": zan,
             "comments": comments
         }
        #print(info)

        f.write(json.dumps(info,ensure_ascii=False)+"\n")