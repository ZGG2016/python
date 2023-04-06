import os
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 模拟登录麻辣社区
url = "https://www.mala.cn/member.php?mod=logging&action=login"

# chromedriver = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe"
# os.environ["webdriver.chrome.driver"] = chromedriver
# browser = webdriver.Chrome(chromedriver)

edgedriver = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedgedriver.exe"
os.environ["webdriver.edge.driver"] = edgedriver
browser = webdriver.Edge(edgedriver)

browser.get(url)
#print(browser.page_source)
time.sleep(3)

# id是变化的，所以如果通过id，会查不到元素。要注意分析不同的属性
browser.find_element_by_xpath('//input[@name="username"]').send_keys("zgg_test")

browser.find_element_by_xpath('//input[@name="password"]').send_keys("zgg_test_1111")

browser.find_element_by_xpath('//button[@name="loginsubmit"]').click()

time.sleep(3)

browser.save_screenshot("mala.png")

with open("mala_selenium.html", "w",encoding='utf-8') as file:
    file.write(browser.page_source)

browser.quit()
