# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os


class TutorialPipeline(object):

    def open_spider(self,spider):
        name = spider.name
        if name == 'doubanlps':
            self.file = open(os.getcwd()+'/tutorial/files/lps.txt','w',encoding='utf-8',errors='ignore')

    def close_spider(self,spider):
        self.file.close()

    def process_item(self, item, spider):
        name = spider.name
        if name == 'doubanlps':
            self.file.write(str(item['watcher'])+':'+str(item['comment'])+'\n\n')
