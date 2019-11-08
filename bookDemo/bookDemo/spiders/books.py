# -*- coding: utf-8 -*-



import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BooksSpider(CrawlSpider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=r'//h3/a'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths=r"//li[@class ='next']/a"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):

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
