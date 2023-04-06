# -*- coding: utf-8 -*-
import os

import scrapy
from spider_scrapy_sina.items import SpiderScrapySinaItem

# 注意掌握爬取逻辑
class SinaSpider(scrapy.Spider):
    name = 'sina'
    allowed_domains = ['sina.com.cn']
    start_urls = ['https://www.sina.com.cn/']

    def parse(self, response):
        items = []
        # 所有大类的url 和 标题
        parentUrls = response.xpath('//div[@class="clearfix"]/h3/a/@href').extract()
        parentTitle = response.xpath('//div[@class="clearfix"]/h3/a/text()').extract()

        # 所有小类的ur 和 标题
        subUrls = response.xpath('//div[@class="clearfix"]/ul//@href').extract()
        subTitle = response.xpath('//div[@class="clearfix"]/ul//a/text()').extract()

        # 爬取所有大类
        for i in range(0, len(parentTitle)):
            # 指定大类目录的路径和目录名
            parentFilename = "./Data/" + parentTitle[i]

            # 如果目录不存在，则创建目录
            if (not os.path.exists(parentFilename)):
                os.makedirs(parentFilename)

            # 爬取所有小类
            for j in range(0, len(subUrls)):
                item = SpiderScrapySinaItem()

                # 保存大类的title和urls
                item['parentTitle'] = parentTitle[i]
                item['parentUrls'] = parentUrls[i]

                # 检查小类的url是否以同类别大类url开头，如果是返回True (sports.sina.com.cn 和 sports.sina.com.cn/nba)
                if_belong = subUrls[j].startswith(item['parentUrls'])

                # 如果属于本大类，将存储目录放在本大类目录下
                if (if_belong):
                    subFilename = parentFilename + '/' + subTitle[j]
                    # 如果目录不存在，则创建目录
                    if (not os.path.exists(subFilename)):
                        os.makedirs(subFilename)

                    # 存储 小类url、title和filename字段数据
                    item['subUrls'] = subUrls[j]
                    item['subTitle'] = subTitle[j]
                    item['subFilename'] = subFilename

                    items.append(item)

#发送每个小类url的Request请求，得到Response连同包含meta数据 一同交给回调函数 second_parse 方法处理
        for item in items:
            yield scrapy.Request( url = item['subUrls'], meta={'meta_1': item}
                                  , callback=self.second_parse
                                  , headers= { "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 Edg/83.0.478.44"})

    def second_parse(self,response):
        # 提取每次Response的meta数据
        meta_1 = response.meta['meta_1']

        # 取出小类里所有子链接
        sonUrls = response.xpath('//div[@class="right-content"]//a/@href').extract()

        items = []
        for i in range(0, len(sonUrls)):
            # 检查每个链接是否以大类url开头、以.shtml结尾，如果是返回True
            if_belong = sonUrls[i].endswith('.shtml') and sonUrls[i].startswith(meta_1['parentUrls'])

            # 如果属于本大类，获取字段值放在同一个item下便于传输
            if (if_belong):
                item = SpiderScrapySinaItem()
                item['parentTitle'] = meta_1['parentTitle']
                item['parentUrls'] = meta_1['parentUrls']
                item['subUrls'] = meta_1['subUrls']
                item['subTitle'] = meta_1['subTitle']
                item['subFilename'] = meta_1['subFilename']
                item['sonUrls'] = sonUrls[i]
                items.append(item)

        # 发送每个小类下子链接url的Request请求，得到Response后连同包含meta数据 一同交给回调函数 detail_parse 方法处理
        for item in items:
            yield scrapy.Request(url=item['sonUrls'], meta={'meta_2': item}
                                 , callback=self.detail_parse
                                 , headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 Edg/83.0.478.44"})

    # 数据解析方法，获取文章标题和内容
    def detail_parse(self, response):
        item = response.meta['meta_2']
        content = ""
        head = response.xpath('//div[@class="main-content w1240"]/h1/text()')
        content_list = response.xpath('//div[@class="article"]//p[@cms-style="font-L align-Justify"]/text()').extract()

        # 将p标签里的文本内容合并到一起
        for content_one in content_list:
            content += content_one

        item['head'] = head
        item['content'] = content

        yield item