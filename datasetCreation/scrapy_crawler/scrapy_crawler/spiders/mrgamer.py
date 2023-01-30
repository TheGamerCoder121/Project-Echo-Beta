import scrapy


class MrgamerSpider(scrapy.Spider):
    name = 'mrgamer'
    allowed_domains = ['mrgamer.xyz']
    start_urls = ['http://mrgamer.xyz/']

    def parse(self, response):
        pass
