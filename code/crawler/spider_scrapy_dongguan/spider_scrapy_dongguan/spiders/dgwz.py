# -*- coding: utf-8 -*-
import scrapy
from spider_scrapy_dongguan.items import SpiderScrapyDongguanItem

class DgwzSpider(scrapy.Spider):
    name = 'dgwz'
    allowed_domains = ['wz.sun0769.com']
    url = 'http://wz.sun0769.com/political/index/politicsNewest?id=1&page='
    offset = 1
    start_urls = [url + str(offset)]

    def parse(self,response):
        # 每一页里的所有帖子的链接集合
        links = response.xpath('//span[@class="state3"]/a/@href').extract()
        for link in links:
            #print(link)
            # 提取列表里每个帖子的链接，发送请求放到请求队列里,并调用self.parse_item来处理
            yield scrapy.Request('http://wz.sun0769.com' + link, callback = self.parse_item)
        # 页面终止条件成立前，会一直自增offset的值，并发送新的页面请求，调用parse方法处理
        if self.offset <= 3:
            self.offset += 1
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)

    # 处理每个帖子的response内容
    def parse_item(self,response):
        print(response.url)

        item = SpiderScrapyDongguanItem()
        # id = scrapy.Field()
        # title = scrapy.Field()
        # url = scrapy.Field()
        # content = scrapy.Field()

        item['id'] = response.xpath('//div[@class="focus-date clear focus-date-list"]/span[4]/text()').extract()[0]
        item['title'] = response.xpath('//div[@class="mr-three"]/p/text()').extract()[0]
        item['url'] = response.url
        item['content'] = response.xpath('//div[@class="details-box"]/pre/text()').extract()[0]

        # 交给管道
        yield item
