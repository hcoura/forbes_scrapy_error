# -*- coding: utf-8 -*-
import scrapy


class ForbesExampleSpider(scrapy.Spider):
    name = 'forbes_example'
    allowed_domains = ['www.forbes.com']
    start_urls = ['https://www.forbes.com/sites/brucejapsen/2017/05/24/how-trumps-budget-hurts-value-based-care-and-population-health/']

    def parse(self, response):
        pass
