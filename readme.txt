This project tracks and analyses the New Zealand Carbon Market. 
The file db_connect.py makes calls to a mySQL database which is not available to the public. 
In theory any one could pull my work and start scraping prices and storing them in their own DB. 
The getters.py file uses selenium to webscrape the following: 
    - Carbon Spot Price (https://www.commtrade.co.nz/)
    - Salt Share Price (https://www.nzx.com/instruments/CO2)
    - Carbon Auction Announcements (https://www.etsauctions.govt.nz/public/auction_noticeboard)

The Carbon and Salt scrapers can only get current prices. So for all the data before I started scraping we 
needed another source. 

Salt is quite easy. Sharesies prints the daily price for all their records in their network tab.
Carbon has been manually scraped by github user theecanmole and his data is publicly available here: https://github.com/theecanmole/nzu
theecanmole if you're reading this please get in touch, I'd love to buy you a beer. 

reporting.py holds the function which create the graphs I've made so far.
