# -*- coding:utf-8 -*-  
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from gitbook.items import GitbookItem

class GitBookSpider(scrapy.Spider):
	name = "gitbook"
	allowed_domains = ["gitbook.com"]
	start_urls = ["https://www.gitbook.com/explore/"]
	#解析页面内容并组成对象
	def parse_item(self,response):
		sel = Selector(response)
		books=[]
		bookdivs = sel.xpath('//div[@class="book col-xs-6 col-sm-3 col-md-3 col-lg-3"]')
		for index, link in enumerate(bookdivs):
			book = GitbookItem();
			book['rbookName']=link.xpath('.//a[@class="book-cover"]/@href').extract()
			book['rabookName']=link.xpath('.//div[@class="mask-inner"]/h3//text()').extract()
			book['readCount']=link.xpath('.//div[@class="book-infos"]/p//text()').extract()
			book['coverAddress']=link.xpath('.//img/@src').extract()
			books.append(book)
		return books

	def parse(self, response):
		#获取最后一页页码
		lastNum = response.xpath('//ul[@class="pagination pagination-pages"]//li[5]//text()').extract()
		validurls = []
		#添加首页
		validurls.append("https://www.gitbook.com/explore")
		#设置递归访问页面
		for i in range(1, int(lastNum[0])):
			validurls.append('https://www.gitbook.com/explore?page='+str(i))
		for url in validurls:
			#依次抓取内容
			yield Request(url, callback=self.parse_item)

