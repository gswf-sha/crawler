# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FiveeightItem(scrapy.Item):
    # define the fields for your item here like:
    # Primary Fields:
    xm = scrapy.Field()
    phone = scrapy.Field()
    service = scrapy.Field()
    title = scrapy.Field()

    # Housekeeping Fields:
    url = scrapy.Field()
    project = scrapy.Field()
    spider = scrapy.Field()
    server = scrapy.Field()
    date = scrapy.Field()
    pass
