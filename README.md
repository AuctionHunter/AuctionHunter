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

Python 3.6.7 or greater: https://www.python.org/downloads/

NodeJS 9 or greater: https://nodejs.org/en/download/

MongoDB: https://docs.mongodb.com/manual/administration/install-community/

MongoDB compass: https://docs.mongodb.com/compass/master/install/

### Setting Up Python 3.7 and React
*It is suggested that this be run on linux (tested with Ubuntu 18.04), but it should work on windows as well with slight command differences for setting up python*

1. `git clone https://github.com/AuctionHunter/AuctionHunter.git`
2. `cd AuctionHunter/code`
3. Create and activate virtual environment for your platform: https://docs.python.org/3/library/venv.html Assuming named venv and located at AuctionHunter/code/venv
    * Something like: `python3 -m pip install virtualenv` and `python3 -m virtualenv venv` then `source venv/bin/activate`
4. `pip install -r frontend/requirements.txt`  # install frontend python requirements
5. `pip install scrapy`
6. `cd frontend/frontend`
7. `npm install`  # install frontend nodejs requirements (this will take a while)

### Running VueJS Alternative frontend
*From code/webapp directory*
This step assumes you have already built the database and run dataEnhancer.py
1. Navigate to code/webapp
2. `npm install`
3. `npm run build`
4. `npm start`
5. Navigate to http://localhost:8080/

## Demo

*Now your going to need multiple terminals, this can be achieved countless ways - choose your fav, mine is tmux*

*Make sure the virtualenv is activated any time your running python commands*

0. Start MongoDB compass community (the gui verson that is an included add on to mongodb), new connection to hostname: localhost, port: 27017.
1. Navigate to AuctionHunter/Code/crawler/'Keystone Project'/tutorial/tutorial/spiders
2. `scrapy crawl iaaibot`
    * Note: If scraping produces incomplete results, replace the "start_urls" variable on line 7 of code/crawler/'Keystone Project'/tutorial/tutorial/spiders/iaaibot.py with the current url from https://www.iaai.com/Home/Default under Vehicle type > Automobiles.
3. Navigate to AuctionHunter/code/database
4. `python dataEnchancer.py`
    * To view database entries, open mongoDB compass and view scrapy > scrapy_items database.
5. `python manage.py migrate`  # install tables into database
5. Term1 in AuctionHunter/code/frontend/ `python manage.py runserver`  # start backend
6. Term2 in AuctionHunter/code/frontend/frontend/ `npm start`  # start serving the frontend (might take a while)
7. Once both commands have finished and are  `localhost:8000`
