# -*- coding: utf-8 -*-
import scrapy


class BasicSpider(scrapy.Spider):
    name = "basic"
    allowed_domains = ["51job"]
    start_urls = (
        'http://www.51job/',
    )

    def parse(self, response):
        pass
