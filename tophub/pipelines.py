# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import redis
import json
from datetime import datetime


class TophubPipeline(object):
    def process_item(self, item, spider):
        return item


class RedisPipeline(object):
    '''
    save data to Redis
    redis结构:
    爬取名称:timestamp ---> 爬取的时间 type为String
    爬取名称:data  ---> 数据 type为List
    '''

    def __init__(self, redis_uri, redis_port, redis_db):
        self.redis_uri = redis_uri
        self.redis_port = redis_port
        self.redis_db = redis_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            redis_uri=crawler.settings.get('REDIS_URI'),
            redis_port=crawler.settings.get('REDIS_PORT'),
            redis_db=crawler.settings.get('REDIS_DB')
        )

    def open_spider(self, spider):
        # redis module
        self.redis_client = redis.StrictRedis(
            host=self.redis_uri, port=self.redis_port, db=self.redis_db)
        # delete old keys
        self.redis_client.delete("{}:data".format(spider.name),
                                 "{}:timestamp".format(spider.name))

    def close_spider(self, spider):
        self.redis_client.set("{}:timestamp".format(spider.name),
                              datetime.utcnow().timestamp())

    def process_item(self, item, spider):
        self.redis_client.rpush("{}:data".format(spider.name),
                                json.dumps(dict(item)))
        return item
