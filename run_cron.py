# from twisted.internet import reactor
# import scrapy
# from scrapy.crawler import CrawlerRunner
# from scrapy.utils.log import configure_logging
# from zywie_pinoy_scraper.spiders.firebasetest import FirebasetestSpider
# from apscheduler.schedulers.blocking import BlockingScheduler
#
#
#
# sched = BlockingScheduler()
#
#
# @sched.scheduled_job('cron', year='*', month='*', day="*", week='*', day_of_week='*', hour='*', minute="*", second="*/20")
# def scheduled_job():
#     configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
#     runner = CrawlerRunner()
#     d = runner.crawl(FirebasetestSpider)
#     d.addBoth(lambda _: reactor.stop())
#
#
# reactor.run()  # the script will block here until the crawling is finished
#
#
# sched.start()
#
# # in the main thread:
# reactor.stop()
#
# # in a non-main thread:
# reactor.callFromThread(reactor.stop)
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from zywie_pinoy_scraper.spiders.firebasetest import FirebasetestSpider
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()


# configure_logging()
# runner = CrawlerRunner()



# @defer.inlineCallbacks
# def crawl():
#     runner.crawl(FirebasetestSpider)
#     reactor.stop()

@sched.scheduled_job('cron', year='*', month='*', day="*", week='*', day_of_week='*', hour='*', minute="*", second="*/20")
def scheduled_job():
    # crawl()
    # reactor.run() # the script will block here until the last crawl call is finished
    print("Hi There");

sched.start()
