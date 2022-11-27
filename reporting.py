import db_connect as db
import matplotlib.pyplot as plt
import json
import numpy as np
import time
from datetime import datetime as dt

def refineData(data):
    dates = []
    prices = []
    for x in data:
        dates.append(dt.strptime(x["date"],'%Y-%m-%d %H:%M:%S.%f'))
        prices.append(x["value"])

    # sorting not working in sql so have to do here
    dictionary = dict(zip(dates, prices))
    sorted_dict = dict(sorted(dictionary.items()))
    dates = sorted_dict.keys()
    prices = sorted_dict.values()
    return [dates, prices]

def getAllCarbon(): 
    data = json.loads(db.getAllCarbonFromDB()[0][0])
    refined = refineData(data)
    return refined

def getAllSalt(): 
    data = json.loads(db.getAllSaltFromDB()[0][0])
    refined = refineData(data)
    return refined

def getPriceByDateAndType(start, end, type):
    data = json.loads(db.getPricesByDate(start, end, type)[0])
    refined = refineData(data)
    return refined

def plotSaltAndCarbon(startDate="2000-01-01", endDate="2029-12-12"):
    carbon_data = getPriceByDateAndType(startDate, endDate, 'carbon')
    salt_data = getPriceByDateAndType(startDate, endDate, 'salt')
    carbonAX = plt.subplot()
    carbonAX.set_xlabel('dates')
    carbonAX.set_ylabel('carbon price')
    carbonAX.plot(carbon_data[0], carbon_data[1], color = 'blue', label='carbon')
    plt.legend(loc='upper center')
    saltAX = carbonAX.twinx()
    saltAX.set_xlabel('dates')
    saltAX.set_ylabel('salt price')
    saltAX.plot(salt_data[0], salt_data[1], color='red', label='salt')

def plotAllSalt():
    data = getAllSalt()
    dates = data[0]
    prices = data[1]
    plt.plot(dates, prices, color='red', label='salt')
    
plotSaltAndCarbon("2001-01-01","2022-12-01")
plt.title('carbon vs salt price')
plt.legend()
plt.show()

# print(getPriceByDateAndType("2001-01-01", "2044-01-01", 'carbon'))
    
# plotAllSalt()
# plt.show()