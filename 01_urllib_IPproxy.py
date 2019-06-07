"""
  time: 2019/6/6
  author: pyTouch
  topic: the IP proxy（IP 代理）

"""
from urllib.request import Request, urlopen
from urllib.request import ProxyHandler, build_opener, install_opener


def get_html(url):

    headers = {"User_Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0"}

    request = Request(url, headers=headers)

    # 临时代理IP
    proxy = {"http": "39.137.107.98:80"}

    # 创建ProxyHandler
    handler = ProxyHandler(proxy)

    # 创建opener
    opener = build_opener(handler)

    临时使用创建的opener
    response = opener.open(request)

    # 安装Opener
    # install_opener(opener)
    # 使用安装的Opener
    # response = urlopen(url)

    # 读取相应信息并解码
    htmldata = response.read().decode()
   
    return htmldata


def save_html(html_data):

    htmldata = html_data.encode()

    # 保存到文件中
    with open("baidu.html", "wb") as f:
         f.write(htmldata)


def main():

    # 测试用url
    # url = "http://httpbin.org/get"

    url = "https://blog.csdn.net/lwhsyit/article/details/80583941"

    html_data = get_html(url)
    save_html(html_data)


if __name__ == '__main__':
    main()


"""
     IP代理一般步骤:
     (1)调用urlib.request.ProxyHandler()，proxies参数为一个字典。
     class urllib.request.ProxyHandler(proxies=None)

     (2)创建Opener(类似于urlopen，这个代开方式是我们自己定制的)
     urllib.request.build_opener([handler,...])

     (3)安装Opener
     urllib.request.install_opener(opener)
     使用install_opener方法之后，会将程序默认的urlopen方法替换掉，
     再次调用urlopen会使用自己创建好的opener。
     如果不想替换掉而只是想临时使用一下，可以使用opener.open(url)，这样就不会对程序默认的urlopen有影响。



"""
