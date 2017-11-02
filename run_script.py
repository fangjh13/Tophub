#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from tophub.spiders.github_spider import GitHubSpider
from tophub.spiders.juejin_spider import JueJinSpider
from tophub.spiders.douban_spider import DouBanSpiderFiction, \
    DouBanSpiderNonFiction
from tophub.spiders.reddit_spider import RedditSpider
from tophub.spiders.segmentfault_spider import SegmentFaultSpider


configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
runner = CrawlerRunner(get_project_settings())
runner.crawl(GitHubSpider)
runner.crawl(JueJinSpider)
runner.crawl(DouBanSpiderFiction)
runner.crawl(DouBanSpiderNonFiction)
runner.crawl(RedditSpider)
runner.crawl(SegmentFaultSpider)
d = runner.join()
d.addBoth(lambda _: reactor.stop())

reactor.run()
