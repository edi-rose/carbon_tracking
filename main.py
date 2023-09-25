import api.headless_getters as web
import numpy as np 
import re
import db_connect as db
from datetime import datetime as dt
import calculations as calcs
import time
import data_helpers as helper


def listen():
    # day/hour method doesnt work if im not in NZTS
    # day =  datetime.now().weekday() # 0 is Monday 6, is Sunday
    # hour = datetime.now().time().hour
    #marketIsOpen =  #web.getCarbonIsOpen() 
    marketIsOpen = True # for testing
    while True: 
        if marketIsOpen:
            print('checking for new prices')
            try:
                kickOff()
            except:
                print('kickoff failed')
            finally:
                print('check complete')
                time.sleep(300)
        else:
            #if market is close, try again in an hour
            print('market is closed')
            time.sleep(3600)


def kickOff(): 
    carbon_previous = db.getLatestCarbonFromDB()[2]

    print('latest carbon: ', carbon_previous)

    salt_previous = db.getLatestSaltFromDB()[2]
    print('latest salt: ', salt_previous)    
    carbon_current = web.getCarbonPrice()
    salt_current = web.getSaltPrice()

    nta_current = web.getSaltNTA()
    nta_previous = db.getLatestNTA()[2]

    if salt_current != salt_previous: 
        print('new salt price ', salt_current, " detected at: ", dt.now())
        try: 
            db.insertPrice('salt', dt.now(), salt_current)
        except: 
            print('adding salt price failed')

    if carbon_current != carbon_previous: 
        print('new carbon price: ', carbon_current, ' dected at: ', dt.now())
        salt_estimate_standard = calcs.estimateNextSaltPrice(carbon_current, carbon_previous, salt_current)
        salt_estimate_thomas = calcs.estimateNextSaltPriceThomas(carbon_current, carbon_previous, salt_current)
        print("standard estimate: ", salt_estimate_standard)
        print("thomas' estimate: ", salt_estimate_thomas)
        # we've stopped adding the estimates and diff to the database these, will now be done on the FE if needed. 
        try:
            db.insertPrice('carbon', dt.now(), carbon_current)
        except: 
            print('adding carbon price failed')

    if nta_current != nta_previous: 
        print('new nta price: ', nta_current, ' detected at: ',  dt.now())
        try:
            db.insertPrice('nta', dt.now(), nta_current)
        except: 
            print('adding nta price failed')
    else:
        return True 

#this starts erryythang
listen()
