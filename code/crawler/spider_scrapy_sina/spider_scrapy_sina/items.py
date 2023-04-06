# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class SpiderScrapySinaItem(scrapy.Item):
# 爬取新浪网导航页所有下所有大类、小类、小类里的子链接，以及子链接页面的新闻内容。
    # 大类的标题 和 url
    parentTitle = scrapy.Field()
    parentUrls = scrapy.Field()

    # 小类的标题 和 子url
    subTitle = scrapy.Field()
    subUrls = scrapy.Field()

    # 小类目录存储路径
    subFilename = scrapy.Field()

    # 小类下的子链接
    sonUrls = scrapy.Field()

    # 文章标题和内容
    head = scrapy.Field()
    content = scrapy.Field()
