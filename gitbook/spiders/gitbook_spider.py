# -*- coding:utf-8 -*-  
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from gitbook.items import GitbookItem

class GitBookSpider(scrapy.Spider):
	name = "gitbook"
	allowed_domains = ["gitbook.com"]
	start_urls = ["https://www.gitbook.com/explore/"]
	def parse_item(self,response):
		sel = Selector(response)
		books=[]
		bookdivs = sel.xpath('//div[@class="book col-xs-6 col-sm-3 col-md-3 col-lg-3"]')
		for index, link in enumerate(bookdivs):
			book = GitbookItem();
			book['rbookName']=link.xpath('.//a[@class="book-cover"]/@href').extract()
			book['rabookName']=link.xpath('.//div[@class="mask-inner"]/h3').extract()
			book['readCount']=link.xpath('.//div[@class="book-infos"]/p').extract()
			book['coverAddress']=link.xpath('.//img/@src').extract()
			books.append(book)
		return books



	def parse(self, response):
		bookdivs = response.xpath('//div[@class="book col-xs-6 col-sm-3 col-md-3 col-lg-3"]')
		books = [];
		validurls = []
		#设置递归访问页面,页面范围稍后改为从起始页面读取
		for i in range(1, 234):
			validurls.append('https://www.gitbook.com/explore?page='+str(i))
		for index, link in enumerate(bookdivs):
			book = GitbookItem();
			book['rbookName']=link.xpath('.//a[@class="book-cover"]/@href').extract()
			book['rabookName']=link.xpath('.//div[@class="mask-inner"]/h3').extract()
			book['readCount']=link.xpath('.//div[@class="book-infos"]/p').extract()
			book['coverAddress']=link.xpath('.//img/@src').extract()
			yield book
		for url in validurls:
			yield Request(url, callback=self.parse_item)


#print link.xpath('.//a[@class="book-infos"]/p').extract()
#link = sel.xpath('a/@href').extract()
#desc = sel.xpath('text()').extract()
#print title, link, desc
