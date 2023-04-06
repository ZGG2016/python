# -*- coding: utf-8 -*-
import json

import scrapy
from spider_scrapy_migu_app.items import SpiderScrapyMiguAppItem

class MiguSpider(scrapy.Spider):
    name = 'migu'
    allowed_domains = ['c.musicapp.migu.cn']
    offset = 1
    url = "http://c.musicapp.migu.cn/MIGUM2.0/resource/dalbum/list-by-tag/v1.0?tagIds=&page="
    start_urls = [url + str(offset)]


    def parse(self, response):
        # 返回从json里获取 data段数据集合
        data = json.loads(response.text)["data"]

        for each in data:
            item = SpiderScrapyMiguAppItem()
            item["title"] = each["title"]
            item["singer"] = each["singer"]
            item["price"] = each["price"]
            item["imgUrl"] = each["imgItem"][1]["img"]

            yield item

        if self.offset <= 1:
            self.offset += 1
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)

