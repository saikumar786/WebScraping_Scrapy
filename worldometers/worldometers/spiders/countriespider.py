# -*- coding: utf-8 -*-
import scrapy
import logging

class CountriespiderSpider(scrapy.Spider):
    name = 'countriespider'
    allowed_domains = ['www.worldometers.info'] #Shouldn't keep http://
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        #title = response.xpath("//h1/text()").get()
        countries = response.xpath('//td/a')

        for country in countries:
            name = country.xpath('.//text()').get()
            url = country.xpath('.//@href').get()

            #absolute_url = f"https://www.worldometers.info{url}"
            #Another way of doing absolute url
            # absolute_url = response.urljoin(url)

            #yield scrapy.Request(url=absolute_url)
            yield response.follow(url=url, callback = self.parse_country, meta = {'country_name': name})


    def parse_country(self, response):
        # logging.info(response.url)
        name = response.request.meta['country_name']
        rows = response.xpath("(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr")
                               #//table[@class='table table-striped table-bordered table-hover table-condensed table-list'][1]/tbody/tr[1]
        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()
            yield{
                'country_name' : name,
                'year' : year,
                'population' : population
            }
