import scrapy
from gitbook.items import GitbookItem

class GitBookSpider(scrapy.Spider):
	name = "gitbook"
	allowed_domains = ["gitbook.com"]
	start_urls = ["https://www.gitbook.com/explore/"]

	def parse(self, response):
		bookdivs = response.xpath('//div[@class="book col-xs-6 col-sm-3 col-md-3 col-lg-3"]')
		for index, link in enumerate(bookdivs):
			book = GitbookItem();
			book['rbookName']=link.xpath('.//a[@class="book-cover"]/@href').extract()
			book['rabookName']=link.xpath('.//div[@class="mask-inner"]/h3').extract()
			book['readCount']=link.xpath('.//div[@class="book-infos"]/p').extract()
			book['coverAddress']=link.xpath('.//img/@src').extract()
			yield book;

#print link.xpath('.//a[@class="book-infos"]/p').extract()
#link = sel.xpath('a/@href').extract()
#desc = sel.xpath('text()').extract()
#print title, link, desc
