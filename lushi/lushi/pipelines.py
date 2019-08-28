# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import csv


class LushiPipeline(object):
    def open_spider(self,spider):
        self.csv = open(os.getcwd()+'/lushi/files/decks.csv','w',encoding='utf-8',newline='',errors='ignore')
        self.writer = csv.writer(self.csv,dialect='excel')

    def close_spider(self,spider):
        self.csv.close()

    def process_item(self, item, spider):
        self.writer.writerow([item['cardid'],item['cname'],item['seriesname']])
