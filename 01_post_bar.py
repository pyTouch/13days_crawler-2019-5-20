"""
  time: 2019/6/2
  author: pyTouch
  topic: the crawler case of post bar

"""

from urllib.request import Request, urlopen
from urllib.parse import urlencode


def get_html(url):

    headers = {
            "User_Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0"        
    }
    
    request = Request(url, headers=headers)
    response = urlopen(request)
    return response.read()


def main():
    
    content = input("请输入要下载的内容：")
    number = input("请输入要下载的页数：")
    base_url = "https://tieba.baidu.com/f?ie=utf-8&{}"
    for pn in range(int(number)):
        args = {
            "kw": content,
            "pn": pn*50
        }
        args = urlencode(args)
        get_html(base_url.format(args))



if __name__ == "__main__":

    main()
