# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import csv


class TutorialPipeline(object):

    def open_spider(self,spider):
        name = spider.name
        if name == 'doubanlps':
            # self.file = open(os.getcwd()+'/tutorial/files/lps.txt','w',encoding='utf-8',errors='ignore')
            self.csv = open(os.getcwd()+'/tutorial/files/watcher.csv','a+',encoding='utf-8',newline='',errors='ignore')
            self.writer = csv.writer(self.csv,dialect='excel')

    def close_spider(self,spider):
        # self.file.close()
        self.csv.close()

    def process_item(self, item, spider):
        name = spider.name
        if name == 'doubanlps':
            # self.file.write(str(item['watcher'])+':'+str(item['comment'])+'\n\n')
            print(item)
            self.writer.writerow([item['watcher'],item['commentTime'],item['votes']])
