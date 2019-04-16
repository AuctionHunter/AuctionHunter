# -*- coding: utf-8 -*-
import scrapy


class RedditbotSpider(scrapy.Spider):
    name = 'iaaibot'
    start_urls = ['https://www.iaai.com/Search?url=pd6JWbJ9kRzcBdFK3vKeyhemMpm/KU7A3DtM+lH1s0yxTvF4GlWIr4FPc5g5DUFcr6s73QlyLnPM1uEFyE8r/2ULidMlH7kMLaYTJ+6F+ypqJKrj/BB5+adRv3mhMcDQcB8kCi+dTs/qULqT8w3o6w==&crefiners=|vehicletype:Automobiles&keyword=']

    def parse_page(self, response):
        #parse info for particular auction entry page

        #get previously scraped image link and vin from meta attribute 
        image_and_vin = response.meta['image_and_vin']
        vin = image_and_vin[1]
        car_image = image_and_vin[0]

        prices = response.xpath("//*[@id='vehicles-container']/div[2]/div[2]/div[2]/div[1]/div[2]/ul/li[2]/span/text()").extract()
        estimated_price = "0"
        for text in prices:
            if "ACV" in text or "ERC" in text:
                estimated_price = text
                estimated_price = ''.join(x for x in text if x.isdigit())

        title = response.xpath('//h1[@class="pd-title-ymm"]/text()')[0].extract()
        body = response.xpath('//*[@id="vehicletabDiv"]/div[5]/div[2]/p/text()')[0].extract()
        body = ' '.join(body.split())

        try:
            primary_damage = response.xpath('//*[@id="vehicles-container"]/div[2]/div[1]/div[2]/div[4]/div[2]/p/span/text()')[0].extract()
            secondary_damage = response.xpath('//*[@id="vehicles-container"]/div[2]/div[1]/div[2]/div[5]/div[2]/p/span/text()')[0].extract()
            #if there is no secondary damage, this will be replaced with the odometer
            if "mi" in secondary_damage:
                secondary_damage = "none"
                miles = response.xpath('//*[@id="vehicles-container"]/div[2]/div[1]/div[2]/div[5]/div[2]/p/span/text()')[0].extract()
                start_code = response.xpath('//*[@id="vehicles-container"]/div[2]/div[1]/div[2]/div[6]/div[2]/p/span/text()')[0].extract()
                key_fob = response.xpath('//*[@id="vehicles-container"]/div[2]/div[1]/div[2]/div[7]/div[2]/p/span/text()')[0].extract()
                airbags = response.xpath('//*[@id="vehicles-container"]/div[2]/div[1]/div[2]/div[9]/div[2]/p/span/text()')[0].extract()
            else:
                miles = response.xpath('//*[@id="vehicles-container"]/div[2]/div[1]/div[2]/div[6]/div[2]/p/span/text()')[0].extract()
                start_code = response.xpath('//*[@id="vehicles-container"]/div[2]/div[1]/div[2]/div[7]/div[2]/p/span/text()')[0].extract()
                key_fob = response.xpath('//*[@id="vehicles-container"]/div[2]/div[1]/div[2]/div[8]/div[2]/p/span/text()')[0].extract()
                airbags = response.xpath('//*[@id="vehicles-container"]/div[2]/div[1]/div[2]/div[10]/div[2]/p/span/text()')[0].extract()
        except IndexError:
            primary_damage = "none"
            secondary_damage = "none"
            miles = "100,000 mi (not required/exept"
            start_code = "Run & Drive "
            key_fob = "Present"
            airbags = "Deployed"

        info = {
            'estimated_price' : estimated_price,
            'car_name' : title,
            'miles':miles,
            'vin':vin,
            'body' : body,
            'primary_damage':primary_damage,
            'secondary_damage':secondary_damage,
            'start_code' : start_code,
            'key_fob' : key_fob,
            'airbags' : airbags,
            'car_image' : car_image,
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
            url = url.replace("..", "https://www.iaai.com")
            if url is not None:
                request = scrapy.Request(url, self.parse_page)
                #pass image and vin as meta attribute
                request.meta['image_and_vin'] = [CarImage[i].split('\"')[1], Vin[i]]
                yield request
            i+=1

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

