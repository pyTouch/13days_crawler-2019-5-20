# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        le = LinkExtractor(restrict_xpaths='//h3/a')

        for link in le.extract_links(response):
            yield scrapy.Request(link.url, callback=self.parse_book)

    def parse_book(self, response):
        item = {}

        sel = response.css('div.product_main')
        item['name'] = sel.xpath('./h1/text()').extract_first()
        item['price'] = sel.css('p.price_color::text').extract_first()
        item['review_rating'] = sel.css('p.star-rating::attr(class)') \
            .re_first('star-rating ([A-Za-z]+)')

        sel = response.css('table.table.table-striped')
        item['upc'] = sel.xpath('(.//tr)[1]/td/text()').extract_first()
        item['stock'] = sel.xpath('(.//tr)[last()-1]/td/text()') \
            .re_first('\((\d+) available\)')
        item['review_num'] = sel.xpath('(.//tr)[last()]/td/text()').extract_first()

        yield item

