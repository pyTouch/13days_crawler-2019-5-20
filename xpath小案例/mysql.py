import pymysql


class mysql_manager(object):

    config = {
        'host': 'localhost',
        'user': 'root',
        'password': '123456',
        'db': 'test'
    }

    def __init__(self):

        self.connection = None
        self.cursor = None

    def creat_database(self, sql):

        # 创建数据库连接
        try:
            self.connection = pymysql.connect(**mysql_manager.config)
            self.cursor = self.connection.cursor()
            self.cursor.execute(sql)
        except Exception as ex:
            print(ex)
        finally:
            self.close()

    def insert_book(self, booklist):

        # 将数据存入数据库中
        try:
            sql = "insert into book(BookName,BookAuthor,BookPrice) values('{}','{}','{}')".format(
                   booklist['name'], booklist['author'], booklist['price'])
            self.connection = pymysql.connect(**mysql_manager.config)
            self.cursor = self.connection.cursor()
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as ex:
           print("insert book:",ex)
           return
        finally:
            self.close()

    def close(self):

        """
            关闭游标和连接
        """
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()


if __name__ == '__main__':

    # 建表book,用于存储爬取到的数据
    sql = """create table book(
        BookName varchar(64) NOT NULL,
        BookAuthor varchar(256) NOT NULL,
        BookPrice float(10,2) NOT NULL)engine=InnoDB"""

    book_table = mysql_manager()
    book_table.creat_database(sql)




    
