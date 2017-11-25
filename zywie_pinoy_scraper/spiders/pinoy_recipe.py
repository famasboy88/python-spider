# -*- coding: utf-8 -*-
import scrapy


class PinoyRecipeSpider(scrapy.Spider):
    name = 'pinoy_recipe'
    allowed_domains = ['panlasangpinoy.com']
    start_urls = ['http://panlasangpinoy.com/indexes/recipe-index/']

    def parse(self, response):
        links = response.css('li.ei-item > h3 > a::attr(href)').extract()
        for link in links:
            link = response.urljoin(link)
            yield scrapy.Request(link, callback=self.subcat)
        pass

    def subcat(self, response):
        links = response.css('li.ei-item > h4.ei-item-title > a::attr(href)').extract()
        for link in links:
            link = response.urljoin(link)
            yield scrapy.Request(link, callback=self.getDetails)
        pass

    def getDetails(self, response):
        name_food = response.css('header.entry-header > h1::text').extract_first()
        list_recipe = response.css('li.ingredient::text').extract()
        description = response.css('div.entry-content > p::text').extract_first()
        pinoy = {
            'name_food': name_food,
            'list_recipe': list_recipe,
            'description': description
        }
        yield pinoy
