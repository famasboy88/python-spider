from scrapy.crawler import CrawlerProcess
from zywie_pinoy_scraper.spiders.testspider1 import Testspider1Spider
from zywie_pinoy_scraper.spiders.testspider2 import Testspider2Spider
from scrapy.utils.project import get_project_settings
from apscheduler.schedulers.twisted import TwistedScheduler

process = CrawlerProcess(get_project_settings())
sched = TwistedScheduler()
sched.add_job(process.crawl, 'cron', args=[Testspider1Spider], minute="*", second="59")
sched.add_job(process.crawl, 'cron', args=[Testspider2Spider], minute="*", second="59")
sched.start()
process.start(False)
