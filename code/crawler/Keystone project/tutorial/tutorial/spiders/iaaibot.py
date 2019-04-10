# -*- coding: utf-8 -*-
import scrapy


class RedditbotSpider(scrapy.Spider):
    name = 'iaaibot'
    start_urls = ['https://www.iaai.com/Search?url=pd6JWbJ9kRzcBdFK3vKeyhemMpm/KU7A3DtM+lH1s0yxTvF4GlWIr4FPc5g5DUFcr6s73QlyLnPM1uEFyE8r/8U74e14sBFxzJttfS/ZQnHDptNLYoLCwzB0wylNtXev/TRixgyK1p4rOgh5ssc3rw==&crefiners=|vehicletype:Automobiles']

    def parse_page(self, reponse):
        #parse info for particular auction entry page
        estimated_price = response.xpath("//ul[contains(@class, 'list-sale-info')]//li//span//text()")[3].extract()
        repair_costs = response.xpath("//ul[contains(@class, 'list-sale-info')]//li//span//text()")[5].extract()

        price_info = [estimated_price,repair_costs]
        #yield or give the scraped info to scrapy
        return price_info

    def parse(self, response):
        #Extracting the content using css selectors
        CarName = response.css('#dvSearchList h4::text').getall()
        CarImage = response.css('.lazy').getall()
        Miles = response.css('td:nth-child(3) p~ p+ p::text').getall()
        Vin = response.css('a~ p:nth-child(3)::text').getall()
        PrimaryDamage = response.css('td:nth-child(5) p:nth-child(2)::text').getall()

        #link parsing
        table = response.css('table.table')
        rows = table.xpath("//tbody//tr")

        for entry in rows:
            url = entry.xpath("td//@href")[1].extract()

            if url is not None:
                price_info += response.follow(url, self.parse_page)

        #Give the extracted content row wise
        i = 0
        for item in zip(CarName,Miles,Vin,PrimaryDamage,CarImage):
            #create a dictionary to store the scraped info
            scraped_info = {
                'car name' : item[0],
                'miles':item[1],
                'vin':item[2],
                'primary damage':item[3],
                'car image' : item[4], #Set's the url for scrapy to download images
                'estimated price' : price_info[i],
                'repair costs' : price_info[i+1]
            }
            if((i+1)<len(price_info)):
                i+=2
            #yield or give the scraped info to scrapy
            yield scraped_info

