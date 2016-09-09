# -*- coding: utf-8 -*-
import datetime,urlparse,socket
from scrapy.linkextractors import LinkExtractor
from scrapy.loader.processors import MapCompose, Join
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
import unicodecsv

from fifty8.items import FiveeightItem

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

clink=read_csv('citylinks.csv')
keyword =u'jiancai/?key=墙纸施工&cmcskey=墙纸施工'
url_list=[]
for item in clink:
    url=urlparse.urljoin(item['links'],keyword)
    url_list.append(url)

class EasySpider(CrawlSpider):
    name = 'easy'
    allowed_domains = ['58.com']
    start_urls = url_list

    rules = (
        Rule(LinkExtractor(restrict_xpaths = '//*[contains(@class,"next")]')),
        Rule(LinkExtractor(restrict_xpaths='//*[@class="t"]'),
            callback='parse_item')
    )

    def parse_item(self, response):
        """This function parses 58 site.
        @url http://sh.58.com/jiancai/26649465495107x.shtml
        @return items 1
        @scrapes firm link
        @scrapes url project spider server date
        """
        # self.log("name: %s" % response.xpath('//p[@class="seller"]/a/text()').extract())
        l = ItemLoader(item=FiveeightItem(),response=response)
        # l.add_xpath('firm', '//p[@class="seller"][1]/a/text()',
        #             MapCompose(lambda i:i.replace(',', '')))
        l.add_xpath('xm', '//*[@class="su_con mg_l_7"]/a/text()')
        l.add_xpath('phone','//span[@class="l_phone"]/text()')
        l.add_xpath('service','//h1/text()')

        # Housekeeping
        l.add_value('url', response.url)
        l.add_value('project', self.settings.get('BOT_NAME'))
        l.add_value('spider', self.name)
        l.add_value('server', socket.gethostname())
        l.add_value('date', datetime.datetime.now())

        # item['name'] = response.xpath('//p[@class="seller"]/a/text()').extract()
        # item['url'] = response.xpath('//p[@class="seller"]/a/@href').extract()
        return l.load_item()
