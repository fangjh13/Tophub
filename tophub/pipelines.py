# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import redis
import json


class TophubPipeline(object):
    def process_item(self, item, spider):
        return item


class RedisPipeline(object):
    ''' save data to Redis '''

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
        self.redis_client.delete(spider.name)

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.redis_client.rpush(spider.name, json.dumps(dict(item)))
        return item
