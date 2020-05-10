# -*- coding: utf-8 -*-
import scrapy


class GlassesSpider(scrapy.Spider):
    name = 'glasses'
    allowed_domains = ['www.glassesshop.com/bestsellers']
    start_urls = ['https://www.glassesshop.com/bestsellers/']

    def parse(self, response):
        for glasses in response.xpath("//div[@class='col-sm-6 col-md-4 m-p-product']"):
            # glass_url = 
            # glass_img_url = 
            # glass_name = 
            # glass_price = 

            yield{
                'url' : glasses.xpath(".//div[@class='pimg default-image-front']/a/@href").get(),
                'img_url' : glasses.xpath(".//div[@class='pimg default-image-front']/a/img/@src").get(), 
                'name' : glasses.xpath(".//div[@class='row']/p[@class='pname col-sm-12']/a/text()").get(),
                'price' : glasses.xpath(".//div[@class='pprice col-sm-12']/span/text()").get()
            }

        next_page = response.xpath("//ul[@class='pagination']/li[position() = last()]/a/@href").get()
        if(next_page):
            yield scrapy.Request(url=next_page, callback=self.parse)
