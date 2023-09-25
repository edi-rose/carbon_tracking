import data_helpers as helpers
import api.headless_getters as headless_getters
import db_connect as db

def addNewAuctions():
    auctionDates = headless_getters.getAuctionDates()
    for date in auctionDates: 
        duplicates = db.getEventWithDateType(date, 'carbon_auction')
        if duplicates == 'none':
            db.insertEvent('carbon_auction', 'None', 'None', date)
    

addNewAuctions()