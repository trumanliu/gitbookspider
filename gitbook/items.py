# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GitbookItem(scrapy.Item):
#id=scrapy.Field();
	rbookName=scrapy.Field();
	rabookName=scrapy.Field();
	inDate=scrapy.Field();
	updDate=scrapy.Field();
	lincense=scrapy.Field();
	language=scrapy.Field();
	chapters=scrapy.Field();
	rate=scrapy.Field();
	readCount=scrapy.Field();
	coverAddress=scrapy.Field();
        summary=scrapy.Field();
