from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from w3lib.url import url_query_cleaner

def process_links(links):
    for link in links:
        link.url = url_query_cleaner(link.url)
        yield link

class ImdbCrawler(CrawlSpider):
    name = '5mods'
    allowed_domains = ['forums.gta5-mods.com']
    start_urls = ['https://forums.gta5-mods.com']
    rules = (
        Rule(
            LinkExtractor(),
            process_links=process_links,
            callback='parse_item',
            follow=True
        ),
    )
    def parse_item(self, response):
        return {
            'url': response.url,
            'metadata': extruct.extract(
                response.text,
                response.url,
                syntaxes=['opengraph', 'json-nl']
            ),
        }