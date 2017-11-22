# -*- coding: utf-8 -*-

import scrapy
from ..items import GitHubItem


class GitHubSpider(scrapy.Spider):
    ''' craw github trending '''
    name = 'github'
    start_urls = ['https://github.com/trending']

    def parse(self, response):
        def handle_none(result):
            if result:
                return result.strip()
            else:
                return result

        for p in response.xpath('//li[contains(@class, "col-12")]'):
            item = GitHubItem()
            item['project'] = p.xpath('.//h3/a/text()').extract()[-1].strip()
            item['link'] = 'https://github.com' \
                + p.xpath('.//h3/a/@href').extract_first().strip()
            item['remark'] = handle_none(
                p.xpath('.//div[@class="py-1"]/p/text()').extract_first())
            item['language'] = handle_none(p.xpath(
                './/span[@itemprop="programmingLanguage"]/text()'
            ).extract_first())
            item['stars'] = handle_none(p.xpath(
                './/a[contains(@class, "mr-3")][1]/text()[last()]'
            ).extract_first())

            yield item
