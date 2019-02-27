# -*- coding: utf-8 -*-
import scrapy


class RedditbotSpider(scrapy.Spider):
    name = 'iaaibot'
    start_urls = ['https://www.iaai.com/Search?url=pd6JWbJ9kRzcBdFK3vKeyhemMpm/KU7A3DtM+lH1s0yxTvF4GlWIr4FPc5g5DUFcr6s73QlyLnPM1uEFyE8r/8U74e14sBFxzJttfS/ZQnHDptNLYoLCwzB0wylNtXev/TRixgyK1p4rOgh5ssc3rw==&crefiners=&keyword=']

    def parse(self, response):
        #Extracting the content using css selectors
        CarName = response.css('#dvSearchList h4::text').getall()
        CarImage = response.css('.lazy').getall()
        Miles = response.css('td:nth-child(3) p~ p+ p::text').getall()
        Vin = response.css('a~ p:nth-child(3)::text').getall()
        PrimaryDamage = response.css('td:nth-child(5) p:nth-child(2)::text').getall()
        #Give the extracted content row wise
        for item in zip(CarName,Miles,Vin,PrimaryDamage,CarImage):
            #create a dictionary to store the scraped info
            scraped_info = {
                'car name' : item[0],
				'miles':item[1],
				'vin':item[2],
				'primary damage':item[3],
				'car image' : item[4], #Set's the url for scrapy to download images
				
            }

            #yield or give the scraped info to scrapy
            yield scraped_info

