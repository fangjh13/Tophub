# -*- coding: utf-8 -*-


import scrapy
from ..items import JueJinItem


class JueJinSpider(scrapy.Spider):
    ''' crawl juejin rank '''
    name = 'juejin'
    start_urls = ['https://juejin.im/explore/all?sort=popular']

    def parse(self, response):
        for item in response.xpath('//div[contains(@class, "info-box")]'):
            rs = JueJinItem()
            tags = item.xpath('..//li[contains(@class, "item tag")]/a/text()'
                              ).extract()
            if tags:
                rs['tag'] = '/'.join(tags)
            else:
                rs['tag'] = None
            rs['title'] = item.xpath(
                './/div[contains(@class, "title-row")]/a/text()'
            ).extract_first()
            link_suffix = item.xpath(
                './/div[contains(@class, "title-row")]/a/@href'
            ).extract_first()
            rs['link'] = 'https://juejin.im' + link_suffix
            rs['collections'] = item.css(
                'li.like span.count::text').extract_first()

            yield rs
