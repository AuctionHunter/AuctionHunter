# AuctionHunter

## Group Members
* Alexander Hull
* Alexander Jacobson
* Yufei Zeng



## Client 
Ryan Kalb

## How to run

Requires the following:
Python: https://www.python.org/downloads/
Scrapy: https://docs.scrapy.org/en/latest/intro/install.html
MongoDB: https://docs.mongodb.com/manual/administration/install-community/

0. Start MongoDB compass community, new connection to hostname: localhost, port: 27017. 
1. Navigate to AuctionHunter/Code/crawler/'Keystone Project'/tutorial/tutorial/spiders
2. run "scrapy crawl iaaibot"

Note: Its a good idea to replace the "start_urls" variable on line 7 of Code/crawler/'Keystone Project'/tutorial/tutorial/spiders/iaaibot.py with the current url from https://www.iaai.com/Home/Default under Vehicle type > Automobiles. 

3. Navigate to AuctionHunter/code/database
4. run "python dataEnchancer.py"
5. To view database entries, open mongoDB compass and view scrapy > scrapy_items database. 




