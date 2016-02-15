# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NeituiwangItem(scrapy.Item):
    page_id = scrapy.Field()
    person = scrapy.Field()
    date = scrapy.Field()
    work = scrapy.Field()
    salary = scrapy.Field()
    experience = scrapy.Field()
    company = scrapy.Field()
    address = scrapy.Field()
    # tag = scrapy.Field()
    # requirement = scrapy.Field()
    name = scrapy.Field()
    company_link = scrapy.Field()
    city = scrapy.Field()
    homepage = scrapy.Field()
    company_size = scrapy.Field()
    company_field = scrapy.Field()
    company_finance = scrapy.Field()
    company_hope = scrapy.Field()

