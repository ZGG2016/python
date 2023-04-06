按照教程，会爬取不到结果。原因及方案如下：

### 原因

在parse函数开头部分加入这两句，然后运行程序。
```
html_str = response.body.decode()
print(html_str)
```
![scrapy07](https://s1.ax1x.com/2020/06/15/NPnAmR.png)

看到整个response就拿到了这些东西，说明页面是动态生成的。为什么浏览器就

可以看到正常的页面？为什么response得到的源码与浏览器里刚才看到的不一

样？其实浏览器中得到的源码跟我们的response得到的是一样的，我们在浏览器

中点击鼠标右键，然后点击“查看网页源代码”。如下图

![scrapy08](https://s1.ax1x.com/2020/06/15/NPnPl4.png)

看到结果完全一样，这么点东西怎么显示出的那么多内容的页面？这个怎么跟开

发者工具中看到的不一样啊？这就是动态加载，scrapy中的Request是无法加载js

代码的，它只能拿到js代码，但是无法像浏览器一样把这些代码解读加载出来给我

们。

### 解决方法

（1）使用Selenium+chromedriver来加载这些js。

（2）使用requests新出的requests-html。

（3）继续分析网站，找到真实接口，拿到json数据

采用第三种

![scrapy09](https://s1.ax1x.com/2020/06/15/NPni6J.png)

通过抓包工具我们看到数据在这个请求下面，点击headers，查看真正的url地址。

![scrapy10](https://s1.ax1x.com/2020/06/15/NPnE01.png)

简化url地址

原地址：

https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1569985950697&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=2&pageSize=10&language=zh-cn&area=cn

简化后的地址：

https://careers.tencent.com/tencentcareer/api/post/Query?pageIndex=2&pageSize=10

把简化后的url地址输入到浏览器中测试一下是否可以获取到数据。

![scrapy11](https://s1.ax1x.com/2020/06/15/NPnFX9.png)

拿到了数据，可以看到已经获取到了第2页的json数据，翻页只需要更换

&pageIndex=后面的数据即可。

来源：[scrapy爬取腾讯招聘信息出现的坑](https://blog.csdn.net/qq_44739762/article/details/101856412)
