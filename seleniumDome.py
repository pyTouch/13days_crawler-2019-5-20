# -*- coding: utf-8 -*-
# @time: 2019/11/24
# @content: selenium模拟登陆豆瓣并爬取电影《一出好戏》短评

from selenium import webdriver
from pymongo import MongoClient
import time


class douban_spider(object):

    def __init__(self):

        self.login_url = "https://accounts.douban.com/passport/login"

        # options = webdriver.ChromeOptions()
        # 添加无界面参数
        # options.add_argument('--headless')

        chromedriver = 'I:\Program Files (x86)\chromedriver.exe'

        browser = webdriver.Chrome(executable_path=chromedriver)

        self.getInfo(browser)

    def getInfo(self, browser):

        browser = browser
        browser.get(self.login_url)

        # 点击"密码登录"
        bottom1 = browser.find_element_by_xpath('//ul[@class="tab-start"]/li[2]')
        bottom1.click()

        # # 输入密码账号
        input1 = browser.find_element_by_xpath('//*[@id="username"]')
        input1.clear()
        input1.send_keys("13337638901")

        input2 = browser.find_element_by_xpath('//*[@id="password"]')
        input2.clear()
        input2.send_keys("pengyefei")

        # 登录
        bottom = browser.find_element_by_class_name('account-form-field-submit ')
        bottom.click()

        time.sleep(2)

        url = 'https://movie.douban.com/subject/26985127/comments?start=0&limit=20&sort=new_score&status=P'
        browser.get(url)
        search_window = browser.current_window_handle
        # pageSource = browser.page_source
        # print(pageSource)

        self.getComment(browser)

    def getComment(self, browser):
        # short_list = []
        browser = browser
        save_to_mongo = Mongodemo()
        save_to_mongo.open_mongo()
        page = 1
        while page < 10:
            for i in range(1, 21):
                short = {}
                short["name"] = browser.find_element_by_xpath('//*[@id="comments"]/div[{}]/div[2]/h3/span[2]/a'.format(str(i))).text
                short["comment"] = browser.find_element_by_xpath('//*[@id="comments"]/div[{}]/div[2]/p/span'.format(str(i))).text
                short["start"] = browser.find_element_by_xpath('//*[@id="comments"]/div[{}]/div[2]/h3/span[2]/span[2]'.format(str(i))).get_attribute('title')
                # short_list.append(short)
                save_to_mongo.save_mongo(short)
            if page == 1:
                nextPage = browser.find_element_by_xpath('//*[@id="paginator"]/a[1]').get_attribute('href')
                browser.get(nextPage)
            else:
                nextPage = browser.find_element_by_xpath('//*[@id="paginator"]/a[3]').get_attribute('href')
                browser.get(nextPage)

            time.sleep(2)
            search_window = browser.current_window_handle
            page += 1

        # print(short_list)
        save_to_mongo.close_mongo()


class Mongodemo(object):

        # 将数据保存到mongodb数据库
        def open_mongo(self):
            self.client = MongoClient()

        def save_mongo(self, item):
            self.client.douban.YiChuHaoXi.insert_one(item)
            return item

        def close_mongo(self):
            self.client.close()


if __name__ == '__main__':

    douban = douban_spider()

