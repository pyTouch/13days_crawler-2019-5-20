"""
  @Time: 2019/8/25
  @Author: pyTouch
  @Topic: 利用xpath获取书籍名称、作者

"""
import pymysql

from lxml import etree

from mysql import mysql_manager


def get_html():

    """
        获取网页数据
    """
    with open('books_html', 'r') as f:
        file = f.read()
    books_html = bytes(bytearray(file, encoding='utf-8'))
    tree = etree.HTML(books_html)
    return tree


def get_data(tree):

    book_list = tree.xpath('//bookstore/book/title/text()')
    price_list = tree.xpath('//bookstore/book/price/text()')
    author_list = []

    # 一本书的作者可能不只是一个人
    for i in range(len(book_list)):
       book_au = tree.xpath(("//bookstore/book['{}'+1]/author/text()").format(i))
       author_list.append(book_au)

    booksql = mysql_manager()

    booklist = {}

    for i in range(len(book_list)):
        booklist['name'] = book_list[i]
        booklist['price'] = price_list[i]

        if len(author_list[i]) == 1:
            booklist['author'] = author_list[i][0]

        else:
            # 利用字符串的拼接函数join()          
            str = ', '
            booklist['author'] = str.join(author_list[i])
        booksql.insert_book(booklist)


def main():

    tree = get_html()
    get_data(tree)


if __name__ == '__main__':
    main()
