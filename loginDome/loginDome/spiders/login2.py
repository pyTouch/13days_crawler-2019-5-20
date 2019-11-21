# -*- coding: utf-8 -*-
# @time: 2019/11/20
# @content: scrapy模拟登陆方式二：使用FormRequest


import scrapy


class Login1Spider(scrapy.Spider):
    name = 'login2'

    def start_requests(self):
        # 登陆页面
        url = 'https://github.com/login'
        # cookiejar是meta的一个特殊的key，通过cookiejar参数支持多个会话对某个网站进行爬取
        # 可以对cookiejar进行标记， 1,2,3,4...这样scrapy就维持了多个会话
        yield scrapy.Request(url=url, meta={"cookiejar": 1}, callback=self.parse)

    def parse(self, response):
        authenticity_token = response.css('div input[name="authenticity_token"]::attr(value)').extract_first()
        form_data = {
            "commit": "Sign in",
            "utf8": "✓",
            "authenticity_token": authenticity_token,
            "login": "**********",               # github账号
            "password": "*********",             # github密码
        }

        yield scrapy.FormRequest.from_response(response=response, meta={"cookiejar": response.meta["cookiejar"]}, formdata=form_data, callback=self.after_login)

    def after_login(self, response):
        # 对登陆后的open-source页面进行爬取
        url = 'https://github.blog/category/community/open-source/'
        yield scrapy.Request(url=url, meta={"cookiejar": response.meta["cookiejar"]}, callback=self.parse2)

    def parse2(self, response):

        print(response.text)


