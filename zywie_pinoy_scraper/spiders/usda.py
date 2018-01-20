# -*- coding: utf-8 -*-
import scrapy
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


class UsdaSpider(scrapy.Spider):
    name = 'usda'
    allowed_domains = ['www.googleapis.com']
    start_urls = ['https://api.nal.usda.gov/ndb/search/?format=xml&offset=0&sort=r&q=carrot&ds=Standard%20Reference&fg=Vegetables%20and%20Vegetable%20Products&api_key=fCaQFZDctF3YHA85VzFd4eHphM9GukBUWFJh2Uld']
    ##########################################################################
    def parse(self, response):
        rootDB = db.reference()
        ref_food_exchange = rootDB.child('food_exchange_list_tag').get()
        for key, food_item in ref_food_exchange.items():
            for value in food_item:
                link = "https://api.nal.usda.gov/ndb/search/?format=xml&offset=0&sort=r&q="+value+"&ds=Standard%20Reference&api_key=fCaQFZDctF3YHA85VzFd4eHphM9GukBUWFJh2Uld"
                link = response.urljoin(link)
                request = scrapy.Request(link, callback=self.getSearch, dont_filter=True)
                request.meta['exchange_category'] = key
                request.meta['food_item'] = value
                yield request

    def getSearch(self, response):
        ndbno = response.xpath('//item/ndbno/text()').extract_first()
        if(ndbno != None):
            link = "https://api.nal.usda.gov/ndb/reports?ndbno="+ndbno+"&type=b&format=xml&api_key=fCaQFZDctF3YHA85VzFd4eHphM9GukBUWFJh2Uld"
            link = response.urljoin(link)
            request = scrapy.Request(link, callback=self.getDetail, dont_filter=True)
            request.meta['exchange_category'] = response.meta['exchange_category']
            request.meta['food_item'] = response.meta['food_item']
            yield request
        else:
            return

    def getDetail(self, response):
        # energy = response.xpath('//nutrient[@name="Energy"]/@value').extract_first()
        # quantity = response.xpath('//nutrient[@name="Energy"]/measures/measure/@qty').extract_first()
        # energy = float(energy)
        # quantity = float(quantity)
        # db.reference().child('test_usda_food_exchange').child(response.meta['exchange_category']).child(response.meta['food_item']).update({
        #     'kcal': energy,
        #     'value_grams': quantity
        # })

        proximity = response.xpath('//nutrient[@group="Proximates"]/@name').extract()
        for proxi in proximity:
            unit = response.xpath('//nutrient[@name="'+proxi+'"]/@unit').extract_first()
            value = response.xpath('//nutrient[@name="'+proxi+'"]/@value').extract_first()
            db.reference().child('test_usda_food_exchange').child(response.meta['exchange_category']).child(response.meta['food_item']).child(proxi).update({
                'unit': unit,
                'value': value
            })
