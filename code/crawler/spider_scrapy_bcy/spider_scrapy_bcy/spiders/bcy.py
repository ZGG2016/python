# -*- coding: utf-8 -*-
import scrapy
from scrapy import Selector
from scrapy.loader import ItemLoader
from spider_scrapy_bcy.items import SpiderScrapyBcyItem

# 图片下载器爬虫

class BcySpider(scrapy.Spider):
    name = 'bcy'
    allowed_domains = ['bcy.net']

    start_urls = (
        'http://bcy.net/cn125101',
        'http://bcy.net/cn126487',
        'http://bcy.net/cn126173'
    )

    def parse(self, response):
        sel = Selector(response)

        for link in sel.xpath(
                "//ul[@class='js-articles l-works']/li[@class='l-work--big']/article[@class='work work--second-created']/h2[@class='work__title']/a/@href").extract():
            link = 'http://bcy.net%s' % link
            request = scrapy.Request(link, callback=self.parse_item)
            yield request

    def parse_item(self, response):
        # Items提供保存抓取数据的容器，而Item Loder提供的是填充容器的机制。
        # 直接赋值取值的方式，会出现一下几个问题：
        # 代码量一多，各种css和xpath选择器，充斥整个代码逻辑，没有规则，可读性差、不利于维护
        # 对于一个字段的预处理，不明确，也不应该出现在主逻辑中

        l = ItemLoader(item=SpiderScrapyBcyItem(), response=response)
        l.add_xpath('name', "//h1[@class='js-post-title']/text()")
        l.add_xpath('info', "//div[@class='post__info']/div[@class='post__type post__info-group']/span/text()")
        urls = l.get_xpath('//img[@class="detail_std detail_clickable"]/@src')
        urls = [url.replace('/w650', '') for url in urls]
        l.add_value('image_urls', urls)
        l.add_value('url', response.url)

        return l.load_item()
