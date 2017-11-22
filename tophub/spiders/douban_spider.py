# -*- coding: utf-8 -*-

import scrapy
from ..items import DouBanItem


class DouBanSpiderNonFiction(scrapy.Spider):
    ''' crawl douban book rank '''
    name = 'douban_book_non_fiction'
    start_urls = ['https://book.douban.com/chart?subcat=I']

    def parse(self, response):
        item = DouBanItem()
        for book in response.xpath('//li[contains(@class, "media clearfix")]'):
            book_image = book.xpath(
                './/div[contains(@class, "media__img")]/a/img/@src'
            ).extract_first()
            item['image'] = book_image.replace('/spic/', '/lpic/') \
                if book_image else book_image
            item['title'] = book.xpath(
                './/h2[@class="clearfix"]/a/text()').extract_first()
            item['link'] = book.xpath(
                './/h2[@class="clearfix"]/a/@href').extract_first()
            item['author'] = book.xpath(
                './/p[contains(@class, "color-gray")]/text()'
            ).extract_first().split('/')[0].strip()

            yield item


class DouBanSpiderFiction(scrapy.Spider):
    name = 'douban_book_fiction'
    start_urls = ['https://book.douban.com/chart?subcat=F']

    def parse(self, response):
        item = DouBanItem()
        for book in response.xpath('//li[contains(@class, "media clearfix")]'):
            book_image = book.xpath(
                './/div[contains(@class, "media__img")]/a/img/@src'
            ).extract_first()
            item['image'] = book_image.replace('/spic/', '/lpic/') \
                if book_image else book_image
            item['title'] = book.xpath(
                './/h2[@class="clearfix"]/a/text()').extract_first()
            item['link'] = book.xpath(
                './/h2[@class="clearfix"]/a/@href').extract_first()
            item['author'] = book.xpath(
                './/p[contains(@class, "color-gray")]/text()'
            ).extract_first().split('/')[0].strip()

            yield item
