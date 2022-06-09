import pymysql as db
import password
import time
import calculations as calcs

def insertCarbonPrice(carbon_current, carbon_previous, salt_price):
    connection = connectDB()
    cursor= connection.cursor()
    salt_estimate_standard = calcs.estimateNextSaltPrice(carbon_current, carbon_previous, salt_price)
    salt_estimate_thomas = calcs.estimateNextSaltPriceThomas(carbon_current, carbon_previous, salt_price)
    diff = carbon_current - carbon_previous
    print(salt_estimate_standard)
    print(salt_estimate_thomas)
    try: 
        cursor.callproc('insert_carbon',[carbon_current, diff, salt_estimate_standard, salt_estimate_thomas])
    except: 
        print('error in insertCarbonPrice at: ', time.now)
        connection.rollback()
    else: 
        connection.commit()
        disconnectDB(connection)
    return

def insertSaltPrice(price, diff):
    connection = connectDB()
    cursor = connection.cursor()
    try:
        cursor.callproc('insert_salt',[price, diff])
    except: 
        print('error in insertSaltPrice at: ', time.now)
        connection.rollback()
    else: 
        connection.commit()
        disconnectDB(connection)
    return

def getLatestCarbonFromDB():
    connection = connectDB()
    cursor= connection.cursor()
    try: 
        cursor.callproc('get_latest_carbon')
    except: 
        print('error in getLatestCarbonFromDB at: ', time.now)
        connection.rollback()
        disconnectDB(connection)
        return
    else: 
        result = cursor.fetchall()
        for r in result:
            if r is not None:
                disconnectDB(connection)
                print('carbon is not none')
                return r
        #hack for first row
        return [0,0,0,0,0] 

def getLatestSaltFromDB():
    connection = connectDB()
    cursor= connection.cursor()   
    try: 
        cursor.callproc('get_latest_salt')
    except:
        print('error in getLatestSaltFromDB at: ', time.now)
        connection.rollback()
        disconnectDB()
        return
    else: 
        result = cursor.fetchall()
        for r in result:
            if r is not None:
                disconnectDB(connection)
                return r             
        #hack for empty table
        return [0,0,0,0,0]

def connectDB():
    connection = db.connect(host="localhost", port=3306, user="root", password=password.getPassword(), database="carbon_market_schema")
    if connection is not None:
        return connection
    else: 
        print('could not connect to db')
        return None

def disconnectDB(connection):
    if connection is not None:
        connection.close()
        return
    else: 
        print('database was already disconnected')
        return
