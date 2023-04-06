import os

from bs4 import BeautifulSoup
from selenium import webdriver

# bs 爬取斗鱼网站的用户、房间、直播类型和热度

edgedriver = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedgedriver.exe"
os.environ["webdriver.edge.driver"] = edgedriver
browser = webdriver.Edge(edgedriver)

browser.get("https://www.douyu.com/directory/all")

while True:

    bs = BeautifulSoup(browser.page_source,"lxml")

    usernames = bs.find_all("h2",{"class":"DyListCover-user"})

    rooms = bs.find_all("h3",{"class":"DyListCover-intro"})

    typees = bs.find_all("span",{"class":"DyListCover-zone"})

    numbers = bs.find_all("span",{"class":"DyListCover-hot"})

    # print(numbers[0].get_text())
    print(len(usernames))
    content = {}
    for i in range(len(usernames)):
        print("用户  %s  的房间  %s  直播  %s  的当前的热度为  %s 。"
              %(usernames[i].get_text(),rooms[i].get_text(),typees[i].get_text(),numbers[i].get_text()))

    # 如果在页面源码里找到"下一页"为隐藏的标签，就退出循环
    if browser.page_source.find("dy-Pagination-disabled dy-Pagination-next") != -1:
        break

    # 一直点击下一页
    browser.find_element_by_class_name("dy-Pagination-next").click()