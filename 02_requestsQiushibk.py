"""
  @Time: 2019/6/15
  @Author: pyTouch
  @Topic: QiuShiBaiKe crawler

"""

import requests
import re


def get_one_page(url):

    """获取一页内容"""

    headers = {
        "User_Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0"
    }
    response = requests.get(url, headers=headers)
    return response.text


def parse_one_page(html):

    """解析网页内容"""
    content = re.findall(r'<div class="content">\s*<span>\s*(.+)\s*</span>', html)
    return content


def save_html(content):

    """保存解析的网页内容到文件中"""
    with open('qiushibaike.txt', 'a', encoding='utf-8') as f:
        for text in content:
            text = text.replace('<br/>', '').strip()
            f.write(text+'\n\n\n')


def main(page):

    """主函数，page为需要爬取的页数"""

    url = "https://www.qiushibaike.com/text/page/"+str(page)+"/"
    html = get_one_page(url)
    content = parse_one_page(html)
    save_html(content)


if __name__ == "__main__":

    for page in range(1, 3):
        main(page)
