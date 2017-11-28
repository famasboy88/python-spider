from twisted.internet import task
from twisted.internet import reactor
from zywie_pinoy_scraper.spiders.firebasetest import FirebasetestSpider
from scrapy.crawler import CrawlerRunner


def run_crawl():
    runner = CrawlerRunner({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    })
    deferred = runner.crawl(FirebasetestSpider)
    return deferred

taskcall = task.LoopingCall(run_crawl)
taskcall.start(3)  # call every second

# l.stop() will stop the looping calls
reactor.run()
