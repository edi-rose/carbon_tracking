import priceGetters as getter
import numpy as np 
import re
import db_connect as db
from datetime import datetime
import time


def listen():
    day =  datetime.now().weekday() # 0 is Monday 6, is Sunday
    hour = datetime.now().time().hour
    while 18 > hour > 7 & day < 5:  
        marketIsOpen = getter.getCarbonIsOpen()
        while marketIsOpen: 
            print('checking for new prices')
            try:
                kickOff()
            except:
                print('find price failed')
            else:
                print('check complete')
                time.sleep(300)
    else:
        print('market is closed')
        time.sleep(3600)

def GetAndRefineNewPrices():
    t = getter.getPrices()
    arr = np.array(t)
    print(arr)

    ss_raw = arr[0].split()
    cp_raw = arr[1].split()

    cp = float(re.findall( r'\d+\.*\d*', cp_raw[0])[0])
    ss = float(re.findall( r'\d+\.*\d*', ss_raw[0])[0])
    return np.array([cp,ss])


def kickOff(): 
    dt = datetime
    carbon_previous = db.getLatestCarbonFromDB()[2]
    salt_previous = db.getLatestSaltFromDB()[2]

    current_prices = GetAndRefineNewPrices()
    carbon_current = current_prices[0]
    salt_current = current_prices[1]

    if salt_current != salt_previous: 
        print('new salt price detected at: ', dt)
        diff = salt_current - salt_previous
        try: 
            db.insertSaltPrice(salt_current, diff)
        except: 
            print('adding salt price failed')

    if carbon_current != carbon_previous: 
        print('new carbon price detected at: ', dt)
        try:
            db.insertCarbonPrice(carbon_current, carbon_previous, salt_current)
        except: 
            print('adding carbon price failed')
    else:
        print('no new price detected, waiting 5 minutes')
    return True 

#this starts erryythang
listen()