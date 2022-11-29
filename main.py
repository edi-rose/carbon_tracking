import priceGetters as getter
import numpy as np 
import re
import db_connect as db
from datetime import datetime
import time
import calculations as calcs
import data_helpers as helper

def listen():
    # day/hour method doesnt work if im not in NZTS
    # day =  datetime.now().weekday() # 0 is Monday 6, is Sunday
    # hour = datetime.now().time().hour
    marketIsOpen = getter.getCarbonIsOpen()
    while True: 
        if marketIsOpen == True:
            print('checking for new prices')
            try:
                kickOff()
            except:
                print('find price failed')
            finally:
                print('check complete')
                time.sleep(300)
        else:
            #if market is close, try again in an hour
            print('market is closed')
            time.sleep(3600)


def kickOff(): 
    dt = datetime.now()
    carbon_previous = db.getLatestCarbonFromDB()[2]
    salt_previous = db.getLatestSaltFromDB()[2]

    carbon_current = getter.getCarbonPrice()
    salt_current = getter.getSaltPrice()

    nta_current = getter.getSaltNTA()
    nta_previous = db.getLatestNTA()[2]

    if salt_current != salt_previous: 
        print('new salt price detected at: ', dt)
        try: 
            db.insertSaltPrice(salt_current)
        except: 
            print('adding salt price failed')

    if carbon_current != carbon_previous: 
        print('new carbon price detected at: ', dt)
        salt_estimate_standard = calcs.estimateNextSaltPrice(carbon_current, carbon_previous, salt_current)
        salt_estimate_thomas = calcs.estimateNextSaltPriceThomas(carbon_current, carbon_previous, salt_current)
        print("standard estimate: ", salt_estimate_standard)
        print("thomas' estimate: ", salt_estimate_thomas)
        # we've stopped adding the estimates and diff to the database these, will now be done on the FE if needed. 
        try:
            db.insertCarbonPrice(carbon_current)
        except: 
            print('adding carbon price failed')

    if nta_current != nta_previous: 
        print('new nta price detected at: ', dt)
        try:
            db.insertNTA(nta_current)
        except: 
            print('adding nta price failed')
    else:
        print('no new price detected, waiting 5 minutes')
        return True 

#this starts erryythang
listen()