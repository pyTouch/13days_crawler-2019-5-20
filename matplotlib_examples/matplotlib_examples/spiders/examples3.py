# -*- coding: utf-8 -*-
# @Editor: pyTouch
# @Time: 2019/11/9
# @Content: 下载matplotlib.org上的examples源码，并分类保存在文件夹中

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Examples2Spider(CrawlSpider):

    name = 'examples3'
    allowed_domains = ['matplotlib.org']
    start_urls = ['https://matplotlib.org/examples/index.html']
    rules = (
        Rule(LinkExtractor(restrict_xpaths=r'//li[@class="toctree-l2"]/a'), follow=True),
        Rule(LinkExtractor(restrict_xpaths=r'//a[@class="reference external"]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        url = response.url
        item['file_urls'] = [url]
        yield item
