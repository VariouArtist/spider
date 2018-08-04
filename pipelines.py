# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import pymysql
from openpyxl import Workbook
import urllib

class MyspiderPipeline(object):
    #excel初始化
    wb = Workbook()
    ws = wb.active
    ws.append(['书名','作者','类型'])

    #保存
    def process_item(self, item, spider):
        
        #保存为json格式
        jsonInfo = json.dumps(dict(item),ensure_ascii = False)
        with open('novel.json','a',encoding = 'utf-8') as wrStream:
            wrStream.write(jsonInfo + "\n")
        
        #保存到数据库
        name = item['name']
        author = item['author']
        classify = item['classify']
        db = pymysql.connect("localhost","root","root","novel")
        cursor = db.cursor()
        sql = """INSERT INTO novelInfo(novelName,novelAuthor,novelClassify)
                 VALUES ('%s','%s','%s')""" % (name,author,classify)
        try:
            cursor.execute(sql)
            db.commit()
        except: 
            db.rollback()
        db.close()

        #保存到excel
        line = [item['name'],item['author'],item['classify']]
        self.ws.append(line)
        self.wb.save('F:\\novel.xlsx')

        #保存图片
        with open('F:\\novelImage\\'+name+'.jpg','wb') as photo:
            link = "http:" +  item['image']
            response = urllib.request.urlopen(link)
            photo.write(response.read())
    
        return item
