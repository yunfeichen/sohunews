# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class SohunewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    cname = scrapy.Field()       #名称
    curl = scrapy.Field()        #URL
    cdate = scrapy.Field()       #发布时间
    csourcename = scrapy.Field() #来源
    csourceurl = scrapy.Field()  #来源URL
    pass
