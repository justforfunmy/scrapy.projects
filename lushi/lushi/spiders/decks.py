# -*- coding: utf-8 -*-
import scrapy
import json
from lushi.items import LushiItem


class DecksSpider(scrapy.Spider):
    name = 'decks'
    allowed_domains = ['iyingdi.com']
    # start_urls = ['http://iyingdi.com/']
    headers = {'User_Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

    def start_requests(self):
        for i in range(0,10):
            yield scrapy.FormRequest(url='https://www.iyingdi.com/hearthstone/deck/search/vertical',formdata={'page':str(i),'size':'9','total':'1','token':''},headers = self.headers,callback=self.next_req)
    
    def next_req(self,response):
        data = json.loads(response.body)
        decks = data['date']['decks']
        for item in decks:
            yield scrapy.Request(url='https://www.iyingdi.com/hearthstone/deck/%s?token=&format=json'%(str(item['id'])),headers=self.headers,callback=self.parse)
    
    def parse(self, response):
        data = json.loads(response.body)
        cards = data['cards']['主牌']['随从']
        for item in cards:
            obj = LushiItem()
            obj['cardid'] = item[1]['id']
            obj['cname'] = item[1]['cname']
            obj['seriesname'] = item[1]['seriesName']
            yield obj
