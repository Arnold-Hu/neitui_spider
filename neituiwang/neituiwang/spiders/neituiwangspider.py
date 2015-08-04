# *-* codi
import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from neituiwang.items import NeituiwangItem

class NeituiwangSpider(CrawlSpider):
    name = "neituiwang"
    allowed_domains = ["neitui.me"]
    start_urls = ["http://www.neitui.me/neitui/type=all.html"]

    rules = [
        Rule(LinkExtractor(allow=('\?name=job&handle=detail&id=\d{6}&from=index')), follow=False, callback='parse_item'),
        Rule(LinkExtractor(allow=('/neitui/type=all&page=\d+.html',)), follow=True)
    ]

    def parse_item(self, response):
        base = response.xpath('//div[@class="cont"]')
        company_part = response.xpath('//div[@class="plate company_information"]')
        item = NeituiwangItem()
        item['page_id'] = response.xpath('//div[@class="handlerbar clearfix"]/a[1]/@href').re('\d{6}')
        item['person'] = base.xpath('div[1]/a[1]/text()').extract()  
        item['date'] = base.xpath('div[1]/text()').re('\d{2}.\d{2}.')
        item['work'] = base.xpath('div[2]/strong/text()').extract()
        item['salary'] = base.xpath('div[2]/span[1]/text()').extract()
        item['experience'] = base.xpath('div[2]/span[2]/text()').extract()
        item['company'] = base.xpath('div[3]/span[1]/text()').extract()
        item['address'] = base.xpath('div[3]/span[2]/text()').extract()
        item['tag'] = base.xpath('div[4]//ul/li/span[1]/text()').extract()
        # item['requirement'] = base.xpath('div[6]/text()').extract()
        item['name'] = company_part.xpath('div[1]/div[2]/a/text()').extract()
        item['company_link'] = "www.neitui.me" + company_part.xpath('div[1]/div[2]/a/@href').extract()[0]
        item['city'] = company_part.xpath('dl[1]/dd[1]/text()').extract()
        item['homepage'] = company_part.xpath('dl[1]/dd[2]/a/@href').extract()
        item['company_size'] = company_part.xpath('dl[2]/dd[1]/text()').extract()    
        item['company_field'] = company_part.xpath('dl[2]/dd[2]/text()').extract()
        item['company_finance'] = company_part.xpath('dl[2]/dd[3]/text()').extract()
        item['company_hope'] = company_part.xpath('dl[3]/dd/text()').extract()
        yield item
