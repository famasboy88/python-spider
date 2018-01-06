# -*- coding: utf-8 -*-
import scrapy
from time import sleep
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class Testspider1Spider(scrapy.Spider):
    name = 'testspider1'
    allowed_domains = ['allrecipes.com']
    start_urls = ['http://allrecipes.com/recipes/84/healthy-recipes/']

    def parse(self, response):
        for x in range(20):
            sleep(1)
            db.reference().child('test1').push({
                'link': response.url
            })
