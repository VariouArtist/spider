基于Scrapy爬虫框架实现起点小说大数据采集

Scrapy组件介绍:
1.Scrapy Engine：引擎负责控制数据流在系统中所有组件中流动，并在相应动作发生时触发事件。
2.调度器(Scheduler)：调度器从引擎接受request并将他们入队，以便之后引擎请求他们时提供给引擎。
3.下载器(Downloader)：下载器负责获取页面数据并提供给引擎，而后提供给spider。
4.Spiders：Spider是Scrapy用户编写用于分析response并提取item(即获取到的item)或额外跟进的URL的类。 每个spider负责处理一个特定(或一些)网站。
5.Item Pipeline：Item Pipeline负责处理被spider提取出来的item。

实现：
1.数据保存为json格式。
2.数据保存在excel文件。
3.数据保存在数据库。
4.小说图片的下载及保存。
5.配置403反爬虫。
6.配置日志系统
7.自动爬取下一页及url去重。
8.对爬取到的数据进行简单的分析。
