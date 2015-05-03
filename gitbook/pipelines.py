# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
import MySQLdb
import hashlib
from scrapy.exceptions import DropItem
from scrapy.http import Request

class GitbookPipeline(object):
	def __init__(self):
		self.conn = MySQLdb.connect(user='gitbook', db='gitbook', passwd='yangyang', host='localhost', charset="utf8", use_unicode=True)
		self.cursor = self.conn.cursor()

	def process_item(self, item, spider):    
		try:
			self.cursor.execute("""INSERT INTO books (rbookname,rabookname,indate,coveraddress,readcount)  
            VALUES (%s, %s, %s, %s,%s)""", 
            (item['rbookName'][0].encode('utf-8'),item['rabookName'][0].encode('utf-8'),'curdate()',item['coverAddress'][0].encode('utf-8'),item['readCount'][0].encode('utf-8')))
			self.conn.commit()
		except MySQLdb.Error, e:
			 print "Error %d: %s" % (e.args[0], e.args[1])
		return item
