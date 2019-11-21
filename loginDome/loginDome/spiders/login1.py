# -*- coding: utf-8 -*-
# @time: 2019/11/15
# @content: scrapy模拟登陆方式一：直接携带cookies登录
# scrapy中cookie不能够放在headers中，在构造请求的时候有专门的cookies参数，能够接受字典形式的coookie
# 在setting中设置ROBOTS协议、USER_AGENT

import scrapy


class Login1Spider(scrapy.Spider):
    name = 'login1'

    def start_requests(self):
        url = 'https://www.douban.com/'  # 豆瓣
        cookies_str = 'll="118399"; bid=jk2O46q378s; push_noty_num=0; push_doumail_num=0; __utmv=30149280.20673; __yadk_uid=UYwSjC431e14VD58sTl8X1327sgCuAlw; ct=y; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1573818030%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DUY5fUDzaSKiO9HwC6MDIZ_6cxVqQ9P2S6YOf1iKMRT3%26wd%3D%26eqid%3Dee23bfe8001dfeb6000000065dce8ea9%22%5D; _pk_id.100001.8cb4=c50a8432958f55d6.1573731088.4.1573818030.1573796262.; _pk_ses.100001.8cb4=*; __utma=30149280.809334360.1573731091.1573796229.1573818032.4; __utmc=30149280; __utmz=30149280.1573818032.4.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; __utmb=30149280.1.10.1573818032; dbcl2="206730935:wCTuS9DZ4Lk"'
        # 将Cookie转换为字典
        cookies = {i.split('=')[0]: i.split('=')[1] for i in cookies_str.split(';')}
        yield scrapy.Request(url=url, cookies=cookies, callback=self.parse)

    def parse(self, response):
        # 查看是否登录成功，去寻找登录后的元素
        names = response.css('div.text a::text').extract()
        contents = response.xpath("//div[@class='content']/p/text()").extract()
        for name, content in zip(names, contents):
            yield {'name': name, 'content': content}


