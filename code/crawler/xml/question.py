from urllib import request,parse

import requests
# 结果不一样？？？？
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 Edg/83.0.478.44",
    }

response = requests.get("http://tieba.baidu.com/f?kw=%E7%BE%8E%E5%A5%B3&pn=0",headers = headers)
response.encoding = 'utf8'
print(response.text.replace("<!--", ""))
print(response.text)

# req = request.Request("http://tieba.baidu.com/f?kw=%E7%BE%8E%E5%A5%B3&pn=0",headers = headers)
#
# # Request对象作为urlopen()方法的参数，发送给服务器并接收响应
# response2 = request.urlopen(req)
#
# print(response2.read().decode())