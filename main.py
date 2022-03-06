import priceGetters as getter
import numpy as np 
import re
import db_connect as db
import datetime
import time


def listen():
    while True: 
        print('checking for new prices')
        try:
            kickOff()
        except:
            print('find price failed')
        else:
            print('check complete')
        time.sleep(300)

def GetAndRefineNewPrices():
    t = getter.getPrices()
    arr = np.array(t)

    ss_raw = arr[0].split()
    cp_raw = arr[1].split()

    cp = float(re.findall( r'\d+\.*\d*', cp_raw[0])[0])
    ss = float(re.findall( r'\d+\.*\d*', ss_raw[0])[0])
    return np.array([cp,ss])


def kickOff(): 
    dt = datetime.datetime
    carbon_previous = db.getLatestCarbonFromDB()[2]
    salt_previous = db.getLatestSaltFromDB()[2]

    current_prices = GetAndRefineNewPrices()
    carbon_current = current_prices[0]
    salt_current = current_prices[1]

    if salt_current != salt_previous: 
        print('new salt price detected at: ', dt)
        diff = salt_current - salt_previous
        db.insertSaltPrice(salt_current, diff)

    if carbon_current != carbon_previous: 
        print('new carbon price detected at: ', dt)
        diff = carbon_current - carbon_previous
        db.insertCarbonPrice(carbon_current, diff)
    else:
        print('no new price detected, waiting 5 minutes')
    return True 
    
listen()