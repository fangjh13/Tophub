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


class JueJinItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    collections = scrapy.Field()
    tag = scrapy.Field()


class DouBanItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    author = scrapy.Field()
    image = scrapy.Field()


class SegmentFaultItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    collections = scrapy.Field()
    tag = scrapy.Field()
