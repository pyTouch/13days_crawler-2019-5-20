# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from os.path import basename, dirname, join
from urllib.parse import urlparse
from scrapy.pipelines.files import FilesPipeline


class MyFilesPipeline(FilesPipeline):
    # 重写file_path
    def file_path(self, request, response=None, info=None):
        path = urlparse(request.url).path
        return join(basename(dirname(path)), basename(path))
