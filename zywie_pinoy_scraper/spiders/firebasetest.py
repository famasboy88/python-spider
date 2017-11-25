# -*- coding: utf-8 -*-
import scrapy
from pyrebase import pyrebase


class FirebasetestSpider(scrapy.Spider):
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
    data = {
        "name": "Its morning!"
    }
    results = db.child("users").push(data, user['idToken'])
    name = 'firebasetest'
    allowed_domains = ['firebase.py']
    start_urls = ['http://firebase.py/']

    def parse(self, response):
        pass
