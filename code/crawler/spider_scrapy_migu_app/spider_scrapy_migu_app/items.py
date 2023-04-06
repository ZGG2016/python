# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderScrapyMiguAppItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    singer = scrapy.Field()
    price = scrapy.Field()
    imgUrl = scrapy.Field()
    imgPath = scrapy.Field() # 照片保存在本地的路径
