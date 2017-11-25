# -*- coding: utf-8 -*-
import scrapy
import time
import schedule
from pyrebase import pyrebase


class FirebasetestSpider(scrapy.Spider):
    ################################################################
    name = 'firebasetest'
    allowed_domains = ['panlasangpinoy.com']
    start_urls = ['http://panlasangpinoy.com/indexes/recipe-index/']
    ################################################################
    config = {
        "apiKey": "AIzaSyC6oVdbBUuBALe1l0hwcEx_E7IOw0UUEhs",
        "authDomain": "pythonproject-e0183.firebaseapp.com",
        "databaseURL": "https://pythonproject-e0183.firebaseio.com",
        "projectId": "pythonproject-e0183",
        "storageBucket": "pythonproject-e0183.appspot.com",
        "messagingSenderId": "878861089919"
    }
    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()
    user = auth.sign_in_with_email_and_password('admin@zywie.com', 'admin123')
    db = firebase.database()

    def parse(self, response):
        links = response.css('li.ei-item > h3 > a::attr(href)').extract_first()
        data = {
            "name": "Its morning!",
            "link": links
        }
        results = self.db.child("users").push(data, self.user['idToken'])
