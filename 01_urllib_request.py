"""
	time: 2019/5/20
	author: pyTouch
	topic: the Request module in the urllib

"""

from urllib.request import Request
from urllib.request import urlopen

url = "http://www.baidu.com"

headers = {
	"Use_Agert": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:66.0) Gecko/20100101 Firefox/66.0"
}

request = Request(url, headers = headers)

response = urlopen(request)

# read() 方法读取文件里的全部内容，返回bytes类型
info = response.read()  
#print(info.decode()) 

# 打印状态码   
print(response.getcode())

# 打印真实url
print(response.geturl())

# 打印响应头
print(response.info())