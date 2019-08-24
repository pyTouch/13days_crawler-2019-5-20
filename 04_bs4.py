"""
  @Time: 2019/8/23
  @Author: pyTouch
  @Topic: bs4

"""

from bs4 import BeautifulSoup 


str = '''
    <title>尚学堂</title>
    <div class='info' float='left'>Welcome to SXT</div>
    <div class='info' float='right'>
         <span>Good Study</span>
         <a href='www.bjsxt.cn'></a>
         <strong><!--no way--></strong>
'''

soup = BeautifulSoup(str, 'lxml')
print(soup.title)
print(soup.title.text)
print(soup.div)
print(soup.div.attrs)
print(soup.div['class'])
print(soup.div.text)



html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>

<p class="title"><!--北京尚学堂--></p>

"""
soup = BeautifulSoup(html_doc,'lxml')

"""
一、基本使用

"""
# print(soup.prettify()) 获取文档的树状结构
# print(soup.title.text) 获取title标签的文本内容
# print(soup.p.text) 获取第一个节点p的文本内容
# print(soup.get_text()) 获取文档的所有文本内容
# print(soup.a.attrs) 获取a节点的所有属性
# print(soup.find_all('a')) 获取所有a节点的内容


"""
二、对象解析

"""
# Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构
# 每个节点都是Python对象
# 所有对象可以归纳为4种: Tag,NavigableString,BeautifulSoup,Comment  

print('-------NavigableString对象-------')
print(type(soup.title.string))

print('-------Tab对象-------')
print(type(soup.head))

        
"""
三、CSS选择器（select）

"""

print('--------select选择器---------')
print(soup.select(".title")) # 获取所有class="title"的节点
print(soup.select("#link1")) # 获取id="link1"的节点
print(soup.select("p a")) # 获取p标签下的所有a节点
print(soup.select(".title")[0].text) # 获取类属性为class="title"的第一个节点的文本内容



