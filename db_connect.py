
import mysql.connector as db
import datetime
import main


connection = db.connect(host="localhost", port="3306", user="root", password="Th3B3llJar", database="carbon_market_schema")
if connection.is_connected(): 
    print("DB is connected")
else: print("getDb Failed")

date= datetime.datetime

def insertCarbonPrice(price):
    db= connection.cursor()
    db.callproc('insert_carbon',[price])
    connection.commit()
    return db.rowcount

def insertSaltPrice(price):
    db= connection.cursor()
    db.callproc('insert_salt',[price])
    connection.commit()
    return db.rowcount

prices= main.GetAndRefinePrices()
carbon_price = prices[0]
salt_price = prices[1]


