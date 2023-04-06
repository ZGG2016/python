from scrapy import cmdline
cmdline.execute("scrapy crawl sina".split())

# 没跑通

# 爬取新浪网导航页所有下所有大类、小类、小类里的子链接，以及子链接页面的新闻内容。