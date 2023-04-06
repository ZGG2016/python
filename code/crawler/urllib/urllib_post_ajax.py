from urllib import parse,request
# AJAX一般返回的是JSON,直接对AJAX地址进行post或get，就返回JSON数据了。

url = "https://sichuan.scol.com.cn/scolpage3/index_data.html"
# 变动的是这两个参数
formdata = {
    "pageNum":"1",  # 2\3\4\5
    "pageSize":	"5"
}

headers = {
    "accept": "text/html, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 Edg/83.0.478.44",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest"
}

data = parse.urlencode(formdata).encode("utf-8")
req = request.Request(url, data = data, headers = headers)
response = request.urlopen(req)
print(response.read().decode())