# -*- coding: utf-8 -*-
import os
import urllib
import urllib2
import scrapy
import re

from scrapy import Selector, Request

from sohunews.items import SohunewsItem


class sohunewsSpider(scrapy.Spider):
    name = "sohunews"
    host = "http://hr.tencent.com"
    # 这个例子中只指定了一个页面作为爬取的起始url
    # 当然从数据库或者文件或者什么其他地方读取起始url也是可以的
    start_urls = [
        "http://hr.tencent.com/position.php?@start=0&start=0#a",
    ]

    # 爬虫的入口，可以在此进行一些初始化工作，比如从某个文件或者数据库读入起始url
    def start_requests(self):
        for url in self.start_urls:
            # 此处将起始url加入scrapy的待爬取队列，并指定解析函数
            # scrapy会自行调度，并访问该url然后把内容拿回来
            yield Request(url=url, callback=self.parse_url)

    # 版面解析函数，解析一个版面上的帖子的标题和地址
    def parse_url(self, response):
        selector = Selector(response)
        contents = selector.xpath("//div[@class='news']/p/a")
        for content in contents:
            cname = content.xpath('text()').extract()[0]
            curl = content.xpath('@href').extract()[0]
            item = SohunewsItem()
            item['cname'] = cname
            item['curl'] = curl
            yield Request(url=curl, callback=self.parse_content,meta={'item': item})

    def parse_content(self, response):
        item = response.meta['item']
        selector = Selector(response)
        cdate = selector.xpath("//div[@class='time-source']/div[@class='time']/text()").extract()[0]
        csourcename = selector.xpath("//span[@itemprop='name']/text()").extract()[0]
        csourceurl = selector.xpath("//span[@id='isBasedOnUrl']/text()").extract()[0]
        item['cdate'] = cdate
        item['csourcename'] = csourcename
        item['csourceurl'] = csourceurl
        print item['cdate']
        print item['csourcename']
        print item['csourceurl']

        yield item



