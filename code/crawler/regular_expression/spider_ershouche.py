from urllib import request
import re

# 关键在于正则怎么写，才能简化后面的数据处理

class Spider:
    def __init__(self):
        # 初始化起始页位置
        self.page = 1
        # 爬取开关，如果为True继续爬取
        self.switch = True

    def startWork(self):
        """
            控制爬虫运行
            :return:
        """

        # 循环执行，直到 self.switch == False
        while self.switch:
            # 用户确定爬取的次数
            self.loadData()
            command = input("如果继续爬取，请按回车（退出输入quit)")
            if command == "no":
                # 如果停止爬取，则输入 quit
                self.switch = False
            #elif command == "yes": # 每次循环，page页码自增1
            self.page += 1
        print("谢谢使用！")

    def loadData(self):
        """
        爬取数据
        :return:
        """
        url = "http://www.che168.com/chengdu/a0_0msdgscncgpi1ltocsp" + str(self.page) + "exx0/"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 Edg/83.0.478.44",
        }
        req = request.Request(url, headers=headers)
        repsonse = request.urlopen(req)
        html = repsonse.read().decode("gbk")
        # print(html)

        pattern = re.compile('<h4 class="card-name">(.*?)</span>', re.S)
        content_list = pattern.findall(html)

        self.dealData(content_list)


    def dealData(self,content_list):
        """
        处理爬取的数据
        :param content_list:
        :return:
        """
        for item in content_list[:-1]:
            # 替换掉无用数据
            item = item.replace('<i class="tp-tags shop-blue">诚信联盟</i>', ',') \
                    .replace('</h4>', ',') \
                    .replace('</p>', ',')\
                    .replace('<div class="cards-price-box">',',')\
                    .replace('<span class="pirce"><em>',',')\
                    .replace('<p class="cards-unit">',',')\
                    .replace('</em>', ',')
            lst1 = item.split(',')
            lst1=[x for x in lst1 if not x.isspace() and x!='']

            lst2 = lst1[1].split('／')
            rlt = '品牌：%s\t里程：%s\t商家等级：%s\t价格：%s\n' % (lst1[0],lst2[0],lst2[3],lst1[2]+""+lst1[3])

            #print(rlt)
            # 处理完后，写入文件内
            self.writeData(rlt)

    def writeData(self,item):
        """
        写入文件
        :param item:
        :return:
        """
        with open("out//ershouche.txt", "a") as f:
            f.write(item)


if __name__ == "__main__":
    spider = Spider()
    spider.startWork()