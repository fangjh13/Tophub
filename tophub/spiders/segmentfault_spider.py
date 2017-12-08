# -*- coding: utf-8 -*-


import scrapy
from ..items import SegmentFaultItem


class SegmentFaultSpider(scrapy.Spider):
    ''' crawl SegmentFault news '''
    name = 'segmentfault'
    start_urls = ['https://segmentfault.com/news']

    def parse(self, response):
        for i in response.xpath(
                '//div[contains(@class, "news__item stream__item")]'):
            item = SegmentFaultItem()
            item['title'] = i.css('a.mr10::text').extract_first().strip()
            item['link'] = 'https://segmentfault.com' + \
                i.css('a.mr10::attr(href)').extract_first().strip()
            item['collections'] = i.css('span.stream__item-zan-number::text'
                                        ).extract_first()
            item['tag'] = i.css(
                'p.news__item-meta a.ml10::text').extract_first()

            yield item

        next_page = response.css('a[rel=next]::attr(href)').extract_first()
        if next_page:
            # next_page = response.urljoin(next_page)
            # yield scrapy.Request(next_page, callback=self.parse)
            yield response.follow(next_page, callback=self.parse)
