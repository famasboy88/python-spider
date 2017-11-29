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
from scrapy.crawler import CrawlerProcess
from zywie_pinoy_scraper.spiders.firebasetest import FirebasetestSpider
from scrapy.utils.project import get_project_settings
from apscheduler.schedulers.twisted import TwistedScheduler

process = CrawlerProcess(get_project_settings())
sched = TwistedScheduler()
sched.add_job(process.crawl, 'cron', args=[FirebasetestSpider], year='*', month='*', day="*", week='*', day_of_week='*', hour='*', minute="*", second="*/59")
sched.start()
process.start(False)    # Do not stop reactor after spider closes
