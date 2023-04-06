import json

import scrapy
from spider_scrapy_tencent import items

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['careers.tencent.com']
    url = "https://careers.tencent.com/tencentcareer/api/post/Query?pageSize=10&pageIndex="
    offset = 1
    start_urls = [url + str(offset)]

    def parse(self, response):

        content = json.loads(response.body.decode())
        jobs = content["Data"]["Posts"]
        for job in jobs:
            item = items.SpiderScrapyTencentItem()
            item['positionName'] = job['RecruitPostName']
            item['workLocation'] = job['CountryName'] +" "+ job['LocationName']
            item['positionApartment'] = job['BGName']
            item['positionType'] = job['CategoryName']
            item['positionContent'] = job['Responsibility']
            item['publishTime'] = job['LastUpdateTime']

            yield item

        # 页码加1
        if self.offset < 600:
            self.offset += 1

        # 每次处理完一页的数据之后，重新发送下一页页面请求
        # self.offset自增10，同时拼接为新的url，并调用回调函数self.parse处理Response
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)


