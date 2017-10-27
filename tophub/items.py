# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RedditItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    scores = scrapy.Field()
    comments = scrapy.Field()


class GitHubItem(scrapy.Item):
    project = scrapy.Field()
    link = scrapy.Field()
    remark = scrapy.Field()
    language = scrapy.Field()
    stars = scrapy.Field()
