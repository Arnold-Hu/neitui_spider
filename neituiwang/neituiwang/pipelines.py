# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
import datetime
from pymongo import MongoClient

class MySQLPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(
            db = 'test',
            user = 'root',
            passwd = 'hbc02041993',
            host = 'localhost',
            charset = 'utf8',
            use_unicode = True)
        self.cursor = self.conn.cursor()
        #清空表：
        self.cursor.execute("truncate table neitui;")
        self.conn.commit()

    def process_item(self, item, spider):
        curTime =  datetime.datetime.now()

        self.cursor.execute("""INSERT INTO neitui(page_id, person, date, work, salary, experience, company, address, name, company_link, city, homepage, company_size, company_field, company_finance, company_hope, update_time)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                        (
                            item['page_id'][0].encode('utf-8'),
                            item['person'][0].encode('utf-8'),
                            item['date'][0].encode('utf-8'),
                            item['work'][0].encode('utf-8'),
                            item['salary'][0].encode('utf-8'),
                            item['experience'][0].encode('utf-8'),
                            item['company'][0].encode('utf-8'),
                            item['address'][0].encode('utf-8'),
                            item['name'][0].encode('utf-8'),
                            item['company_link'].encode('utf-8'),
                            item['city'][0].encode('utf-8'),
                            item['homepage'][0].encode('utf-8'),
                            item['company_size'][0].encode('utf-8'),
                            item['company_field'][0].encode('utf-8'),
                            item['company_finance'][0].encode('utf-8'),
                            item['company_hope'][0].encode('utf-8'),
                            curTime,
                        )
        )

        self.conn.commit()
        return item

class MongoPipeline(object):
    def __init__(self):
        client = MongoClient('localhost',27017)
        db = client['neituiwang']
        self.collection = db['neitui']
        self.collection.remove()

    def process_item(self, item, spider):
        curTime =  datetime.datetime.now()
        data = {
        'page_id' : item['page_id'][0].encode('utf-8'),
        'person' : item['person'][0].encode('utf-8'),
        'date' : item['date'][0].encode('utf-8'),
        'work' : item['work'][0].encode('utf-8'),
        'salary' : item['salary'][0].encode('utf-8'),
        'experience' : item['experience'][0].encode('utf-8'),
        'company' : item['company'][0].encode('utf-8'),
        'address' : item['address'][0].encode('utf-8'),
        'name' : item['name'][0].encode('utf-8'),
        'company_link' : item['company_link'].encode('utf-8'),
        'city' : item['city'][0].encode('utf-8'),
        'homepage' : item['homepage'][0].encode('utf-8'),
        'company_size' : item['company_size'][0].encode('utf-8'),
        'company_field' : item['company_field'][0].encode('utf-8'),
        'company_finance' : item['company_finance'][0].encode('utf-8'),
        'company_hope' : item['company_hope'][0].encode('utf-8'),
        'update_time' : curTime
        }
        self.collection.insert(data)
        return item
