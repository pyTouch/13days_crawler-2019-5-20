# -*- coding: utf-8 -*-
# @Editor: pyTouch
# @Time: 2019/11/9
# @Content: 下载matplotlib.org上的examples源码，并分类保存在文件夹中

import scrapy
from scrapy.linkextractors import LinkExtractor


class ExamplesSpider(scrapy.Spider):
    name = 'examples1'
    allowed_domains = ['matplotlib.org']
    start_urls = ['https://matplotlib.org/examples/index.html']

    def parse(self, response):
        le = LinkExtractor(restrict_css='div.toctree-wrapper.compound', deny='/index.html$')
        for link in le.extract_links(response):
            yield scrapy.Request(link.url, callback=self.parse_example)

    def parse_example(self, response):
        item = {}
        href = response.css('a.reference.external::attr(href)').extract_first()
        url = response.urljoin(href)
        item['file_urls'] = [url]
        yield item

