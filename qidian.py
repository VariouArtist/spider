# -*- coding: utf-8 -*-
import scrapy
import urllib
from myspider.items import MyspiderItem
from scrapy.http import Request
from scrapy.selector import Selector

class QidianSpider(scrapy.Spider):
    name = 'qidian'
    allowed_domains = ['www.qidian.com']
    start_urls = ['https://www.qidian.com/all']

    def parse(self, response):
        list = response.xpath("//div[@class='all-book-list']/div[@class='book-img-text']/ul[@class='all-img-list cf']/li")
        print("数目:",len(list))
        for info in list:
            novelName = info.xpath("div[@class='book-mid-info']/h4/a/text()").extract()[0]
            novelAuthor = info.xpath("div[@class='book-mid-info']/p[@class='author']/a[@class='name']/text()").extract()[0]
            novelClassify = info.xpath("div[@class='book-mid-info']/p[@class='author']/a[@class='go-sub-type']/text()").extract()[0]
            novelImage = info.xpath("div[@class='book-img-box']/a/img/@src").extract()[0]
            novelItem = MyspiderItem()
            novelItem['name'] = novelName
            novelItem['author'] = novelAuthor
            novelItem['classify'] = novelClassify
            novelItem['image'] = novelImage
  
            yield novelItem

            #获取下一页url
            # next = Selector(response)
            # url = next.xpath("//div[@class='lbf-pagination']/ul[@class='lbf-pagination-item-list'/li[@class='lbf-pagination-item']/a@href").extract()
            # print(url)
            # yield Request(url, callback=self.parse)
            urls = ['https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=2','https://www.qidian.com/all?orderId=&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0&page=3']
            for url in urls:
                yield scrapy.Request(url, self.parse, dont_filter=False)
                #对于每一个url的请求，调度器都会根据请求得相关信息加密得到一个指纹信息，并且将指纹信息和set()集合中的指纹信息进行比对，如果set()集合中已经存在这个数据，就不在将这个Request放入队列中。如果set()集合中没有存在这个加密后的数据，就将这个Request对象放入队列中，等待被调度。
 


        
