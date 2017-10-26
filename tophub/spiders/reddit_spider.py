# -*- coding: utf-8 -*-


import scrapy
from ..items import RedditItem


class RedditSpider(scrapy.Spider):
    ''' crawl reddit `programming` subreddits '''
    name = 'reddit'
    start_urls = ['https://www.reddit.com/r/programming/']

    def extract_strip(self, target, expr):
        return target.css(expr).extract_first().strip()

    def parse(self, response):
        for post in response.css(".thing"):
            item = RedditItem()
            item['title'] = self.extract_strip(post, "a.title::text")
            item['link'] = self.extract_strip(post, "a.title::attr(href)")
            item['scores'] = self.extract_strip(post, ".score.unvoted::text")
            item['comments'] = post.css("li.first a::text").re_first(r'(\d*) ')

            yield item

        next_page = response.css(
            'span.next-button a::attr(href)').extract_first()
        if next_page:
            yield response.follow(next_page, callback=self.parse)


class GitHubSpider(scrapy.Spider):
    ''' craw github trending '''
    name = 'github'
    start_urls = ['https://github.com/trending']

    def parse(self, response):
        pass