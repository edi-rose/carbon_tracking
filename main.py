import priceGetters as getter
import numpy as np 
import re
import db_connect as db

def findPrices(): 
    carbon_previous = db.getLatestCarbonFromDB()[2]
    salt_previous = db.getLatestSaltFromDB()[2]

    current_prices = GetAndRefineNewPrices()
    carbon_current = current_prices[0]
    salt_current = current_prices[1]

    if salt_current != salt_previous: 
        diff = salt_current - salt_previous
        db.insertSaltPrice(salt_current, diff)

    if carbon_current != carbon_previous: 
        diff = carbon_previous - carbon_current
        db.insertCarbonPrice(carbon_current, diff)
    return 

def GetAndRefineNewPrices():
    t = getter.getPrices()
    arr = np.array(t)

    ss_raw = arr[0].split()
    cp_raw = arr[1].split()

    cp = float(re.findall( r'\d+\.*\d*', cp_raw[0])[0])
    ss = float(re.findall( r'\d+\.*\d*', ss_raw[0])[0])
    return np.array([cp,ss])

findPrices()