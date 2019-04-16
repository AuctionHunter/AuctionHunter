# AuctionHunter

## Group Members
* Alexander Hull
* Alexander Jacobson
* Yufei Zeng



## Client 
Ryan Kalb

# How to run

## Prerequisites

Installation is different for each operating system, so the instructions provided on each website for desired OS should be followed. 

Python: https://www.python.org/downloads/

Scrapy: https://docs.scrapy.org/en/latest/intro/install.html

MongoDB: https://docs.mongodb.com/manual/administration/install-community/
MongoDB compass: https://docs.mongodb.com/compass/master/install/


## Demo 

0. Start MongoDB compass community (the gui verson that is an included add on to mongodb), new connection to hostname: localhost, port: 27017. 
1. Navigate to AuctionHunter/Code/crawler/'Keystone Project'/tutorial/tutorial/spiders
2. run "scrapy crawl iaaibot" in terminal

Note: If scraping produces incomplete results, replace the "start_urls" variable on line 7 of Code/crawler/'Keystone Project'/tutorial/tutorial/spiders/iaaibot.py with the current url from https://www.iaai.com/Home/Default under Vehicle type > Automobiles. 

3. Navigate to AuctionHunter/code/database
4. run "python dataEnchancer.py"
5. To view database entries, open mongoDB compass and view scrapy > scrapy_items database. 




