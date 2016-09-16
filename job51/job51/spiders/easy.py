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

    # def parse(self, response):
    #     # l = ItemLoader(item=Job51Item(),response=response)
    #     for sel in response.xpath('//div[@class="detlist gbox"]/div[@class="e"]'):
    #         item = Job51Item()
    #         item['title'] = sel.xpath('./p[1]/span[@class="title"]/a/text()').extract()
    #         item['company'] = sel.xpath('./p[1]/a/text()').extract()
    #         item['location'] = sel.xpath('./p[1]/span[@class="location name"]/text()').extract()
    #         item['salary'] = sel.xpath('./p[1]/span[@class="location"]/text()').extract()
    #         item['job_description'] = sel.xpath('./p[@class="text"]/text()').extract()
    #         item['info'] = sel.xpath('./p[@class="order"]/text()').extract()
    #         # House keeping
    #         item['url'] = response.url
    #         item['project']= self.settings.get('BOT_NAME')
    #         item['spider'] = self.name
    #         item['server']= socket.gethostname()
    #         item['date'] = datetime.datetime.now()

    #         yield item
    def parse_item(self, response):
        # l = ItemLoader(item=Job51Item(),response=response)
        for sel in response.xpath('//div[@class="detlist gbox"]/div[@class="e"]'):
            item = Job51Item()
            item['title'] = sel.xpath('./p[1]/span[@class="title"]/a/text()').extract()
            item['company'] = sel.xpath('./p[1]/a/text()').extract()
            item['location'] = sel.xpath('./p[1]/span[@class="location name"]/text()').extract()
            item['salary'] = sel.xpath('./p[1]/span[@class="location"]/text()').extract()
            item['job_description'] = sel.xpath('./p[@class="text"]/text()').extract()
            item['info'] = sel.xpath('./p[@class="order"]/text()').extract()
            # House keeping
            item['url'] = response.url
            item['project']= self.settings.get('BOT_NAME')
            item['spider'] = self.name
            item['server']= socket.gethostname()
            item['date'] = datetime.datetime.now()

            yield item