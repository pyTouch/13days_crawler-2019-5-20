# -*- coding: utf-8 -*-
# @Editor: pyTouch
# @Time: 2019/11/9
# @Content: 下载matplotlib.org上的examples源码，并分类保存在文件夹中

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider

class Examples2Spider(CrawlSpider):

    name = 'examples2'
    allowed_domains = ['matplotlib.org']
    start_urls = ['https://matplotlib.org/examples/index.html']

    def parse(self, response):
        le = LinkExtractor(restrict_xpaths=r'//li[@class="toctree-l2"]/a')
        for link in le.extract_links(response):
            yield scrapy.Request(link.url, callback=self.parse_item)

    def parse_item(self, response):
        item = {}
        href = response.xpath(r'//a[@class="reference external"]/@href').extract_first()
        url = response.urljoin(href)
        item['file_urls'] = [url]
        yield item
