# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient


class LogindomePipeline(object):
    # 将数据存入mongodb数据库
    def open_spider(self, spider):
        self.client = MongoClient()

    def process_item(self, item, spider):
        self.client.douban.login1.insert(item)
        return item

    def close_spider(self, spider):
        self.client.close()



