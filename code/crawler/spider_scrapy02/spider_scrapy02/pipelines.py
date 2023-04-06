# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# class SpiderScrapy01Pipeline:
#     def process_item(self, item, crawler):
#         return item
import json

# pipeline将所有(从所有'crawler'中)爬取到的item，存储到一个独立地items.json 文件，
# 每行包含一个序列化为'JSON'格式的'item':
class ItcastjsonPipelins(object):

    def __init__(self):
        self.file = open('teachers.json','wb')

    def process_item(self,item,spider):
        content = json.dumps(dict(item),ensure_ascii=False) +"\n"
        self.file.write(content.encode("utf-8"))
        return item

    def close_spider(self,spider):
        self.file.close()

