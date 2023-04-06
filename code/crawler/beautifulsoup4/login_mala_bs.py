import requests
from bs4 import BeautifulSoup

"""
模拟登录  麻辣社区
1、抓包：登录网站时，分析往服务器发送了什么字段，哪些是变量，哪些是常量
2、解析html，获取变量，构建data
3、发送post请求，模拟登录
"""
#

def malaLogin():

    url = "https://www.mala.cn/member.php?mod=logging&action=login"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 Edg/83.0.478.44"
    }
    # 构建一个Session对象，可以保存页面Cookie
    sess = requests.Session()
    # 首先获取登录页面，找到需要POST的数据，同时会记录当前网页的Cookie值
    html = sess.get(url,headers = headers).text

    # 调用lxml解析库
    bs = BeautifulSoup(html,'lxml')
    #<input type="hidden" name="formhash" value="789221d8">
    # 找到name属性值为 formhash 的input标签，再取出value 的值
    formhash = bs.find('input',attrs={"name":"formhash"}).get("value")
    #print(formhash)
    data = {
        'action':'login',
        'ajaxdata':'json',
        'donewAjax':'1',
        'formhash':formhash,
        'inajax':'1',
        'loginsubmit':'yes',
        'password':'zgg_test_1111',
        'referer':'https://www.mala.cn/',
        'username':'zgg_test'
    }

    # 发送登录需要的POST数据，获取登录后的Cookie(保存在sess里)
    # response = sess.post("https://www.mala.cn/member.php?mod=logging",data = data,headers = headers)
    # print(response.text)

    # 用已有登录状态的Cookie发送请求，获取目标页面源码
    response = sess.get("https://www.mala.cn/home.php?mod=space&uid=7708368", headers=headers)
    with open("mala.html", "wb") as f:
        f.write(response.content)


if __name__ == "__main__":
    malaLogin()


# https://www.cnblogs.com/hum0ro/p/9536033.html
# https://blog.csdn.net/kingyuan666/article/details/81214954

# 手输验证码处理：分析验证码图片的url
#     def captcha(captcha_data):
#         with open("captcha.jpg", "wb") as f:
#             f.write(captcha_data)
#         text = raw_input("请输入验证码：")
#         # 返回用户输入的验证码
#         return text
#
# # 根据UNIX时间戳，匹配出验证码的URL地址
#     captcha_url = "https://www.zhihu.com/captcha.gif?r=%d&type=login" % (time.time() * 1000)
#     # 发送图片的请求，获取图片数据流，
#     captcha_data = sess.get(captcha_url, headers = headers).content
#     # 获取验证码里的文字，需要手动输入
#     text = captcha(captcha_data)