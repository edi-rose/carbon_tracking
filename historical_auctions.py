import data_helpers as helpers
import priceGetters as getters
import db_connect as db

def addNewAuctions():
    auctionDates = getters.getAuctionDates()
    for date in auctionDates: 
        duplicates = db.getEventWithDateType(date, 'carbon_auction')
        if duplicates == 'none':
            db.insertEvent('carbon_auction', 'None', 'None', date)
    

addNewAuctions()