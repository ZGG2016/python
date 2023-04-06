# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderScrapyDongguanItem(scrapy.Item):
    # 爬取投诉帖子的编号、帖子的url、帖子的标题，和帖子里的内容
    id = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    content = scrapy.Field()
