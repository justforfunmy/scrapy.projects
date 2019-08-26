# -*- coding: utf-8 -*-
import scrapy
from tutorial.utils import util


class ZhihuofoSpider(scrapy.Spider):
    name = 'zhihuofo'
    allowed_domains = ['zhihu.com']
    # start_urls = ['http://zhihu.com/']
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
    cookies = util.parseCookies('_zap=96c15127-f312-4c97-9418-1bd51e063fde; d_c0="ADAnuG_V_A2PTrWELRWUivNWrh0gpqMiJcU=|1533085684"; _xsrf=FOJPLMhv3A4rnkYOlflCHZ4XXgqVBvrT; tst=r; __utmv=51854390.100--|2=registration_date=20161011=1^3=entry_date=20161011=1; capsion_ticket="2|1:0|10:1564367968|14:capsion_ticket|44:MDU3ZmQzY2YzYjExNGQ4M2EyNzllZjYzYmY2ZTAxZGM=|24b9fae66a2b78629997397cb374f16c6a8183de2649398b360a0db5ece38179"; z_c0="2|1:0|10:1564367970|4:z_c0|92:Mi4xZHlDUEF3QUFBQUFBTUNlNGI5WDhEU1lBQUFCZ0FsVk5ZcW9yWGdDVk9NWE1MWVhRTWxIMllXMVJaeGJBbkxOSXhn|f74d9bed7ecb6f580e2c7abd3fd34368c0012b3e23739293d461543b759b5f29"; q_c1=fc683aa08ad745cd832b821254df6d50|1564383243000|1533085897000; __utma=51854390.1289208248.1561715983.1561715983.1566178474.2; __utmz=51854390.1566178474.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; tgw_l7_route=a37704a413efa26cf3f23813004f1a3b')

    def start_request(self):
        yield scrapy.FormRequest(url = 'http://www.zhihu.com/api/v4/answers/749783688/root_comments?order=normal&limit=20&offset=0&status=open',headers = self.headers,cookies=self.cookies,callback=self.parse)

    def parse(self, response):
        pass
