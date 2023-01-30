from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from w3lib.url import url_query_cleaner

def process_links(links):
    for link in links:
        link.url = url_query_cleaner(link.url)
        yield link

class ImdbCrawler(CrawlSpider):
    name = 'cfx'
    allowed_domains = ['forum.cfx.re']
    start_urls = ['https://forum.cfx.re']
    rules = (Rule(LinkExtractor()),)