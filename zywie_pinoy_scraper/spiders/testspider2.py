# -*- coding: utf-8 -*-
import scrapy
from time import sleep
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class Testspider2Spider(scrapy.Spider):
    name = 'testspider2'
    allowed_domains = ['www.chowhound.com']
    start_urls = ['https://www.chowhound.com/recipes']

    def parse(self, response):
        for x in range(20):
            sleep(1)
            db.reference().child('test2').push({
                'link': response.url
            })
