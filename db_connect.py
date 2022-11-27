import pymysql as db
import password
from datetime import datetime as dt
import calculations as calcs

def insertCarbonPrice(carbon_current):
    connection = connectDB()
    cursor= connection.cursor()
    try:  
        cursor.callproc('insert_carbon',[carbon_current])
    except: 
        print('error in insertCarbonPrice at: ', dt.now())
        connection.rollback()
    else: 
        connection.commit()
        disconnectDB(connection)
    return

def insertSaltPrice(price):
    connection = connectDB()
    cursor = connection.cursor()
    try:
        cursor.callproc('insert_salt',[price])
    except: 
        print('error in insertSaltPrice at: ', dt.now())
        connection.rollback()
    else: 
        connection.commit()
        disconnectDB(connection)
        return

def insertNTA(nta):
    connection = connectDB()
    cursor = connection.cursor()
    try:
        cursor.callproc('insert_nta',[nta])
    except: 
        print('error in insert_nta at: ', dt.now())
        connection.rollback()
    else: 
        connection.commit()
        disconnectDB(connection)
        return

def insertHistoricalPrice(type, date, price):
    connection = connectDB()
    cursor = connection.cursor()
    try:
        cursor.callproc('insert_historical_price',[type, date, price])
    except: 
        print('error in insert_historical_price at: ', dt.now())
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
        print('error in getLatestCarbonFromDB at: ', dt.now())
        connection.rollback()
        disconnectDB(connection)
        return
    else: 
        result = cursor.fetchall()
        for r in result:
            if r is not None:
                disconnectDB(connection)
                return r
        #hack for first row
        return [0,0,0] 

def getLatestSaltFromDB():
    connection = connectDB()
    cursor= connection.cursor()   
    try: 
        cursor.callproc('get_latest_salt')
    except:
        print('error in getLatestSaltFromDB at: ', dt.now())
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
        return [0,0,0]

def getLatestNTA():
    connection = connectDB()
    cursor= connection.cursor()   
    try: 
        cursor.callproc('get_latest_nta')
    except:
        print('error in getLatestNTA at: ', dt.now())
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
        return [0,0,0]

def getAllSaltFromDB():
    connection = connectDB()
    cursor= connection.cursor()   
    try: 
        cursor.callproc('get_all_salt')
    except:
        print('error in getAllSaltFromDB at: ', dt.now())
        connection.rollback()
        disconnectDB()
        return
    else: 
        result_raw = cursor.fetchall()
        return result_raw

def getAllCarbonFromDB():
    connection = connectDB()
    cursor= connection.cursor()   
    try: 
        cursor.callproc('get_all_carbon')
    except:
        print('error in getAllCarbonFromDB at: ', dt.now())
        connection.rollback()
        disconnectDB()
        return
    else: 
        result_raw = cursor.fetchall()
        disconnectDB(connection)
        return result_raw

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

def getPriceWithDate(date, type):
    connection = connectDB()
    cursor= connection.cursor()   
    try: 
        cursor.callproc('get_price_with_date', [date, type])
    except:
        print('error in get_price_with_date at: ', dt.now())
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
        return 'none'
    
def getPricesByDate(start, end, type):
    connection = connectDB()
    cursor= connection.cursor()   
    try: 
        cursor.callproc('get_prices_by_dates', [start, end, type])
    except:
        print('error in get_prices_by_date')
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
        return 'none'