import pymysql as db
import password
from datetime import datetime as dt
import calculations as calcs
import data_helpers as helpers

def insertPrice(type, date, price):
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
        result_raw = cursor.fetchall()[0][0]
        refined = helpers.refinePricesForReports(result_raw)
        disconnectDB()
        return refined

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
        result_raw = cursor.fetchall()[0][0]
        refined = helpers.refinePricesForReports(result_raw)
        disconnectDB(connection)
        return refined

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
        disconnectDB(connection)
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
        disconnectDB(connection)
        return
    else: 
        result_raw = cursor.fetchall()[0][0]
        if result_raw: 
            refined = helpers.refinePricesForReports(result_raw)           
            return refined
        else: 
            return None

def insertEvent(type, text, description, date):
    connection = connectDB()
    cursor = connection.cursor()
    try:
        cursor.callproc('insert_event',[type, text, description, date])
    except connection.Error as error:
        print("Failed to execute stored procedure: {}".format(error))
        print('error in insert_event at: ', dt.now())
        connection.rollback()
        disconnectDB(connection)
    else: 
        connection.commit()
        disconnectDB(connection)
        return

def getEventWithDateType(date, type):
    connection = connectDB()
    cursor= connection.cursor()   
    try: 
        cursor.callproc('get_event_by_date_type', [date, type])
    except:
        print('error in get_event_by_date_type at: ', dt.now())
        connection.rollback()
        disconnectDB(connection)
        return
    else: 
        result = cursor.fetchall()
        print(result)
        for r in result:
            if r is not None:
                disconnectDB(connection)
                return r             
        #hack for empty table
        return 'none'

def getEventsByDateRangeType(start, end, type):
    connection = connectDB()
    cursor= connection.cursor()   
    try: 
        cursor.callproc('get_events_by_date_range_type', [start, end, type])
    except connection.Error as error:
        print("Failed to execute stored procedure: {}".format(error))
        print('error in insert_event at: ', dt.now())
        connection.rollback()
        disconnectDB(connection)
        return
    else: 
        result_raw = cursor.fetchall()
        return result_raw