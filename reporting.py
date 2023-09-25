import db_connect as db
import matplotlib.pyplot as plt
import numpy as np
import historical_nzx as nzx
import data_helpers as help
import datetime as dt
import historical_salt_prices as historical_salt
import historical_carbon_prices as historical_carbon
from datetime import timedelta, date

def plotDiffSaltAndCarbon(start, end):
    carbon_prices = db.getPricesByDate(start, end, 'carbon')
    salt_prices = db.getPricesByDate(start, end, 'salt')

def plotTwoPrices(dict1, dict2, startStr, endStr):
    dates = help.getDatesBetween(startStr, endStr)
    dates_final = []
    dict1_values = []
    dict2_values = []
    
    for date in dates: 
        if date in dict1 and date in dict2:
            dict1_values.append(dict1[date])
            dict2_values.append(dict2[date])
            dates_final.append(date)

    plt.plot(dates_final, dict1_values, color = 'blue')
    plt.plot(dates_final, dict2_values, color='red')

def plotSaltAndNZX(startDate="2000-01-01", endDate="2029-12-12"):
    dates = help.getDatesBetween(startDate, endDate)
    dates_final = []
    nzx_prices = []
    salt_prices = []

    for date in dates: 
        if date in nzx.nzx_price_dict and date in historical_salt.salt_price_dict:
            nzx_prices.append(nzx.nzx_price_dict[date])
            salt_prices.append(historical_salt.salt_price_dict[date])
            dates_final.append(date)
    

    plt.plot(dates_final, nzx_prices, color='blue', label='NZX50')
    plt.plot(dates_final, salt_prices, color='red', label='salt')


def plotSaltAndCarbon(startDate="2000-01-01", endDate="2029-12-12"):
    auction_dates = db.getEventsByDateRangeType(startDate,endDate, 'carbon_auction')
    carbon_data = db.getPricesByDate(startDate, endDate, 'carbon')
    salt_data = db.getPricesByDate(startDate, endDate, 'salt')
    carbonAX = plt.subplot()
    carbonAX.set_ylabel('Carbon Price')
    carbonAX.plot(carbon_data.keys(), carbon_data.values(), color = 'blue', label='carbon')
    plt.legend(loc='upper center')
    saltAX = carbonAX.twinx()
    saltAX.set_xlabel('')
    saltAX.set_ylabel('Salt Share Price')
    # for date in auction_dates:
    #     plt.axvline(x=date)
    saltAX.plot(salt_data.keys(), salt_data.values(), color='red', label='salt')

def plotAllSalt():
    data = db.getAllSaltFromDB()
    dates = data.keys()
    prices = data.values()
    plt.plot(dates, prices, color='red', label='salt')

def plotAuctions(startDate, endDate, delta, type):
    auction_dates = db.getEventsByDateRangeType(startDate,endDate, 'carbon_auction')
    for auction in auction_dates:
        beforeAuction = auction[0] - timedelta(days=delta)
        afterAuction = auction[0] + timedelta(days=delta)
        prices = db.getPricesByDate(beforeAuction, afterAuction, type)
        keys = []
        if prices is not None: 
            for price in prices:
                keys.append((price - auction[0])/timedelta(days=1))
        
            plt.plot(keys, prices.values(), label=auction[0].strftime("%Y-%m-%d"))
    plt.Axes.set_ylabel("Jarden Carbon Spot Price")

def plotAuctionsSaltAndCarbon(startDate, endDate, delta):
    auction_dates = db.getEventsByDateRangeType(startDate,endDate, 'carbon_auction')  
    carbonAX = plt.subplot()
    carbonAX.set_xlabel('dates')
    carbonAX.set_ylabel('Carbon Price')
    saltAX = carbonAX.twinx()
    saltAX.set_xlabel('dates')
    saltAX.set_ylabel('Salt Share Price')
    for auction in auction_dates:
        beforeAuction = auction[0] - timedelta(days=delta)
        afterAuction = auction[0] + timedelta(days=delta)
        salt_prices = db.getPricesByDate(beforeAuction, afterAuction, 'salt')
        carbon_prices = db.getPricesByDate(beforeAuction, afterAuction, 'carbon')
        salt_keys = []
        carbon_keys = []
        for salt_price in salt_prices:
            salt_keys.append((salt_price - auction[0])/timedelta(days=1))
        for carbon_price in carbon_prices:
            carbon_keys.append((carbon_price - auction[0])/timedelta(days=1))
        
        carbonAX.plot(carbon_keys, carbon_prices.values(), color = 'blue', label='Carbon')
        saltAX.plot(salt_keys, salt_prices.values(), color='red', label='Salt')

#plotAllNZX()
#plotTwoPrices(db.getPricesByDate("2020-01-01","2022-12-01", 'carbon'), historical_salt.salt_price_dict,"2020-01-01","2022-12-01")

#plotAuctions('2015-01-01', '2024-01-01', 30, 'carbon')
plotSaltAndCarbon("2001-08-25","2023-12-25")
#plotSaltAndNZX('2022-01-01', "2022-12-25")
plt.title('Carbon vs Salt')
plt.legend()
plt.show()

# print(getPriceByDateAndType("2001-01-01", "2044-01-01", 'carbon'))
    
# plotAllSalt()
# plt.show()