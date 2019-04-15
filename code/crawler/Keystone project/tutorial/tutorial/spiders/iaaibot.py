# -*- coding: utf-8 -*-
import scrapy


class RedditbotSpider(scrapy.Spider):
    name = 'iaaibot'
    start_urls = ['https://www.iaai.com/Search?url=pd6JWbJ9kRzcBdFK3vKeyhemMpm/KU7A3DtM+lH1s0yxTvF4GlWIr4FPc5g5DUFcr6s73QlyLnPM1uEFyE8r/8U74e14sBFxzJttfS/ZQnHDptNLYoLCwzB0wylNtXev/TRixgyK1p4rOgh5ssc3rw==&crefiners=|vehicletype:Automobiles']

    def parse_page(self, response):
        #parse info for particular auction entry page

        #get previously scraped image link and vin from meta attribute 
        image_and_vin = response.meta['image_and_vin']
        vin = image_and_vin[0]
        car_image = image_and_vin[1]

        price_raw = response.xpath("//ul[contains(@class, 'list-sale-info')]//li//span//text()")
        title = response.xpath('//h1[@class="pd-title-ymm"]/text()')[0].extract()
        body = response.xpath('//*[@id="vehicletabDiv"]/div[5]/div[2]/p/text()')[0].extract()
        body = ' '.join(body.split())
        primary_damage = response.xpath('//*[@id="vehicles-container"]/div[2]/div[1]/div[2]/div[3]/div[2]/p/span/text()')[0].extract()
        secondary_damage = response.xpath('//*[@id="vehicles-container"]/div[2]/div[1]/div[2]/div[5]/div[2]/p/span/text()')[0].extract()
        miles = response.xpath('//*[@id="vehicles-container"]/div[2]/div[1]/div[2]/div[6]/div[2]/p/span/text()')[0].extract()
        start_code = response.xpath('//*[@id="vehicles-container"]/div[2]/div[1]/div[2]/div[7]/div[2]/p/span/text()')[0].extract()
        key_fob = response.xpath('//*[@id="vehicles-container"]/div[2]/div[1]/div[2]/div[8]/div[2]/p/span/text()')[0].extract()
        try:
            airbags = response.xpath('//*[@id="vehicles-container"]/div[2]/div[1]/div[2]/div[10]/div[2]/p/span/text()')[0].extract()
        except IndexError:
            airbags = "Deployed"

        if(len(price_raw) >= 4):
            estimated_price = price_raw[3].extract()
        else: 
            estimated_price = "Sold"

        info = {
            'estimated price' : estimated_price,
            'car name' : title,
            'miles':miles,
            'vin':vin,
            'body' : body,
            'primary damage':primary_damage,
            'secondary damage':secondary_damage,
            'start code' : start_code,
            'key fob' : key_fob,
            'airbags' : airbags,
            'car image' : car_image,
            'url' : response.request.url,
        }
        #yield or give the scraped info to scrapy
        return info

    def parse(self, response):
        #Extracting the content using css selectors
        #CarName = response.css('#dvSearchList h4::text').getall()
        CarImage = response.css('.lazy').getall()
        #Miles = response.css('td:nth-child(3) p~ p+ p::text').getall()
        Vin = response.css('a~ p:nth-child(3)::text').getall()
        #PrimaryDamage = response.css('td:nth-child(5) p:nth-child(2)::text').getall()

        #link parsing
        table = response.css('table.table')
        rows = table.xpath("//tbody//tr")
        
        i = 0
        for url in rows:
            url = url.xpath("td//@href")[1].extract()
            #url.replace("..", "https://www.iaai.com")
            i += 1
            if url is not None:
                request = scrapy.Request(url, self.parse_page)
                #pass image and vin as meta attribute
                request.meta['image_and_vin'] = [CarImage[i], Vin[i]]
                yield request

#        #Give the extracted content row wise
#        for item in zip(CarName,Miles,Vin,PrimaryDamage,CarImage, url):
#            #create a dictionary to store the scraped info
#            scraped_info = {
#                'car name' : item[0],
#                'miles':item[1],
#                'vin':item[2],
#                'primary damage':item[3],
#                'car image' : item[4], #Set's the url for scrapy to download images
#                'url' : item[5].xpath("td//@href")[1].extract(),
#            }
#            #yield or give the scraped info to scrapy
#            yield scraped_info

