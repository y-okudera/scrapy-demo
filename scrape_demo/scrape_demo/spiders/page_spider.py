import scrapy


class PageSpiderSpider(scrapy.Spider):
    name = 'page_spider'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        pass
