import scrapy
from ..items import HackerNewsItem


class HackerNewsSpider(scrapy.Spider):
    ''' crawl Hacker News '''
    name = 'hacker_news'
    start_urls = ['https://news.ycombinator.com/']

    def parse(self, response):
        item = HackerNewsItem()
        for article in response.xpath('.//tr[@class="athing"]'):
            item['title'] = article.xpath('.//td/a/text()').extract_first()
            item['origin'] = article.xpath('.//td/a/@href').extract_first()
            item['comments'] = article.xpath(
                './/following-sibling::tr[position()=1]/td/a/text()').re_first(
                r'(\d+).+?comments')
            item['link'] = self.start_urls[0] + article.xpath(
                './/following-sibling::tr[position()=1]/td/child::a[position()=last()]/@href').extract_first()
            yield item
