# -*- coding: utf-8 -*-
import scrapy
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class FirebasetestSpider(scrapy.Spider):
    ################################################################
    name = 'firebasetest'
    allowed_domains = ['panlasangpinoy.com']
    start_urls = ['http://panlasangpinoy.com/indexes/recipe-index/']
    ################################################################

    def parse(self, response):
        db.reference().child('food_title').set({})
