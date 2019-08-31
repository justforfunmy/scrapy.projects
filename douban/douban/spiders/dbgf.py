# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.selector import Selector
from douban.items import DoubanItem
import re


class DbgfSpider(scrapy.Spider):
    name = 'dbgf'
    allowed_domains = ['douban.com']
    # start_urls = ['http://douban.com/']
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
    }

    def start_requests(self):
        for i in range(0, 5):
            yield scrapy.Request(
                url=
                'https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=recommend&page_limit=20&page_start='
                + str(i * 20),
                headers=self.headers,
                callback=self.next_req)

    def next_req(self, response):
        data = json.loads(response.body)
        subjects = data['subjects']
        for item in subjects:
            yield scrapy.Request(url=item['url'],
                                 headers=self.headers,
                                 callback=self.parse)

    def parse(self, response):
        obj = DoubanItem()
        info = response.xpath('//div[@id="info"]').extract_first()
        infoSelector = Selector(text=info)
        obj['movieName'] = response.xpath(
            '//span[@property="v:itemreviewed"]/text()').extract_first()
        obj['rate'] = response.xpath('//strong[@property="v:average"]/text()').extract_first()
        obj['director'] = infoSelector.xpath(
            '//a[@rel="v:directedBy"]/text()').extract_first()
        actors = infoSelector.xpath('//a[@rel="v:starring"]/text()').extract()
        obj['actors'] = ','.join(actors[:3])
        # obj['genres'] = ','.join(infoSelector.xpath('//@span[@property="v:genre"]/text()').extract())
        obj['initialReleaseDate'] = infoSelector.xpath(
            '//span[@property="v:initialReleaseDate"]/text()').extract_first()
        obj['runtime'] = infoSelector.xpath(
            '//span[@property="v:runtime"]/text()').extract_first()
        # 转换成字符串用来正则匹配
        htmlstr = response.body.decode('utf-8', 'ignore')
        patG = '<span property="v:genre">(.*?)</span>'
        obj['genres'] = ','.join(re.compile(patG).findall(htmlstr))
        patC = '<span class="pl">制片国家/地区:</span> (.*?)<br/>'
        obj['country'] = re.compile(patC).findall(htmlstr)[0]
        patL = '<span class="pl">语言:</span> (.*?)<br/>'
        obj['language'] = re.compile(patL).findall(htmlstr)[0]
        patI = '<span class="pl">IMDb链接:</span> <a href="(.*?)" '
        obj['imdbLink'] = re.compile(patI).findall(htmlstr)[0]

        yield obj
