# -*- coding: utf-8 -*-
# @Editor: pyTouch
# @Time: 2019/11/9
# @Content: 下载image.so.com上的photography图片

import scrapy
import json


class ImagesSpider(scrapy.Spider):

    BASE_URL = 'https://image.so.com/zjl?ch=photography&sn=%s&listtype=new&temp=1'
    start_index = 0
    MAX_DOWNLOAD_NUM = 60

    name = 'images1'
    allowed_domains = ['image.so.com']
    start_urls = [BASE_URL % 0]

    def parse(self, response):

        infos = json.loads(response.body.decode('utf-8'))
        yield{
            "image_urls": [info['qhimg_url'] for info in infos['list']],
            "image_name": [info['title'] for info in infos['list']],
        }
        self.start_index += infos['count']
        if infos['count'] > 0 and self.start_index < self.MAX_DOWNLOAD_NUM:
            yield scrapy.Request(self.BASE_URL % self.start_index)


