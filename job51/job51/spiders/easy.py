# -*- coding: utf-8 -*-
import datetime,urlparse,socket
from scrapy.linkextractors import LinkExtractor
from scrapy.loader.processors import MapCompose, Join
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader

from job51.items import Job51Item

class EasySpider(CrawlSpider):
    name = 'easy'
    allowed_domains = ['51job.com']
    start_urls = ['http://jobs.51job.com/all/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths = '//*[contains(@class,"bk")][2]'),
            callback='parse_item',follow = True),
    )

    def parse_item(self, response):
        l = ItemLoader(item=Job51Item(),response=response)
        for sel in response.xpath('//*[@class="e"]'):
            item = Job51Item()
            item['title'] = sel.xpath('./p[1]/span/a/text()').extract()
            yield item
