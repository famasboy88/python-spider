# -*- coding: utf-8 -*-
import scrapy
import time
import schedule
from pyrebase import pyrebase
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


class FirebasetestSpider(scrapy.Spider):
    ################################################################
    name = 'firebasetest'
    allowed_domains = ['panlasangpinoy.com']
    start_urls = ['http://panlasangpinoy.com/indexes/recipe-index/']
    ################################################################
    def pushToFirebase():
        data = {
            "name": "Its morning!"
        }
        results = db.child("users").push(data, user['idToken'])

    def parse(self, response):
        pass
    schedule.every(5).seconds.do(pushToFirebase)
    while 1:
        schedule.run_pending()
        time.sleep(1)
