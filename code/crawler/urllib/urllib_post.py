from urllib import parse,request

#发送post请求

# POST请求的目标URL
# # 通过抓包的方式获取的url，并不是浏览器上显示的url
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
word = input("请输入需要翻译的单词:")
# 发送到web服务器的表单数据
# 请求数据
formdata = {
    "i":word,
    "from":"AUTO",
    "doctype":"json",
    "keyfrom":"fanyi.web",
    "action":"FY_BY_REALTlME"}

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 Edg/83.0.478.44",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
    }

data = parse.urlencode(formdata).encode("UTF-8")
req = request.Request(url, data = data, headers = headers)
response = request.urlopen(req)
print(response.read().decode())


#     1·设置URL(抓包)
#
#     2·构建表单数据，并使用urllib.prase.urlencode对数据进行编码处理 (fiddler--webforms--body)
#
#     3·创建Request对象，参数包括URL和要传递的数据
#
#     4·使用add_header()添加头信息(fiddler--raw)
#
#     5·使用urllib.request.urlopen()打开对应的Request对象，完成数据传递
#
#     6·后续处理
#
# 原文链接：https://blog.csdn.net/weixin_39741628/article/details/79509705