# -*- coding: utf-8 -*-
import scrapy
from tutorial.utils import util
from tutorial.items import DoubanLpsItem
from scrapy.selector import Selector


class DoubanlpsSpider(scrapy.Spider):
    name = 'doubanlps'
    allowed_domains = ['movie.douban.com']
    # start_urls = ['http://movie.douban.com/']
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

    def start_requests(self):
        for i in range(0,3):
            yield scrapy.Request(url='https://movie.douban.com/subject/27060077/comments?start='+str(i*20)+'&limit=20&sort=new_score&status=P',headers = self.headers,callback=self.parse)
        
    def parse(self, response):
        comments = response.xpath('//div[@class="comment"]').extract()
        for item in comments:
            obj = DoubanLpsItem()
            selector = Selector(text = item)
            obj['comment'] = selector.xpath('//span[@class="short"]/text()').extract_first()
            obj['watcher'] = selector.xpath('//span[@class="comment-info"]/a/text()').extract_first()
            obj['commentTime'] = selector.xpath('normalize-space(//span[@class="comment-info"]/span[@class="comment-time "]/text())').extract_first()
            obj['votes'] = selector.xpath('//span[@class="votes"]/text()').extract_first()
            yield obj

