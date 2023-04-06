
import scrapy
from spider_scrapy01 import items

class ItcastSpider(scrapy.Spider):
    # 爬虫名
    name = 'itcast'

    # 允许爬虫作用的范围
    allowed_domains = ['itcast.cn']

    # 爬虫url
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):

        # 通过scrapy自带的xpath匹配出所有老师的根节点列表集合
        teacher_list = response.xpath('//div[@class="li_txt"]')
        # 所有老师信息的列表集合
        teacherItem = []

        for each in teacher_list:
            # Item对象用来保存数据的
            item = items.SpiderScrapy01Item()
            # name, extract() 将匹配出来的结果转换为Unicode字符串
            # 不加extract() 结果为xpath匹配对象
            name = each.xpath('./h3/text()').extract()
            # title
            title = each.xpath('./h4/text()').extract()
            # info
            info = each.xpath('./p/text()').extract()

            # print(name[0])
            # print(title[0])
            # print(info[0])

            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]

            #yield item

            teacherItem.append(item)


        return teacherItem