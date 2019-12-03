# -*- coding: utf-8 -*-
# @time: 2019/12/3
# @content: scrapy+splash爬取京东python图书名称和价格

import scrapy 
from scrapy import Request
from scrapy_splash import SplashRequest


"""
调用方法为 element.scrollIntoView() 参数默认为true。
参数为true时调用该函数，页面（或容器）发生滚动，使element的顶部与视图（容器）顶部对齐；
参数为false时，使element的底部与视图（容器）底部对齐

每个页面有60本书，页面打开时首先只加载30本书，通过滚动条的下拉，会动态加载后面的30本书。
所以我们要执行一下JavaScript代码使页面滚动到页面底部把剩余的30本书加载出来。

"""
lua_script = '''
function main(splash)
  splash.images_enabled = false
  splash:go(splash.args.url)
  splash:wait(2)
  splash:runjs("document.getElementsByClassName('page')[0].scrollIntoView(true)")
  splash:wait(2)
  return splash:html()
end
'''


class JingdongSpider(scrapy.Spider):
    name = 'jingdong'
    allowed_domains = ['search.jd.com']
    base_url = 'https://search.jd.com/Search?keyword=python&enc=utf-8&wq=python'
    
    def start_requests(self):       
        yield Request(self.base_url, callback=self.parse_urls, dont_filter=True)
        

    def parse_urls(self, response):
            pageNum = response.xpath('//span[@class="fp-text"]/i/text()').extract_first()
            for i in range(int(pageNum)):
                url = '%s&page=%s' % (self.base_url, 2 * i + 1)
                yield SplashRequest(url,
                   callback=self.parse,
                   endpoint='execute',
                   args={'lua_source': lua_script},
                   cache_args=['lua_source'])


    def parse(self, response):
        
        # 获取一个页面中每本书的名字和价格
        for sel in response.css('ul.gl-warp.clearfix > li.gl-item'):
            #num = sel.xpath('//span[@class="fp-text"]/b/text()').extract()
            #print(num)
            yield {
               'name': sel.css('div.p-name').xpath('string(.//em)').extract_first(),
               'price': sel.css('div.p-price i::text').extract_first(),
            }
