from urllib import parse,request

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action="
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 Edg/83.0.478.44",
}
# 变化的参数
formdata = {
        "start":"0",  
        "limit":"20"
    }

data = parse.urlencode(formdata).encode("utf-8")
req = request.Request(url, data = data, headers = headers)
response = request.urlopen(req)
print(response.read().decode())