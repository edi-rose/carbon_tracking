
from sys import builtin_module_names
import db_connect as db
import matplotlib.pyplot as plt
import json
import numpy as np
from datetime import datetime as dt


def getAllCarbon(): 
    data = json.loads(db.getAllCarbonFromDB()[0][0])
    dates = []
    prices = []
    for x in data:
        dates.append(dt.strptime(x["date"],'%Y-%m-%d %H:%M:%S.%f'))
        prices.append(x["value"])
    return [dates , prices]

def getAllSalt(): 
    data = json.loads(db.getAllSaltFromDB()[0][0])
    dates = []
    prices = []
    for x in data:
        dates.append(dt.strptime(x["date"],'%Y-%m-%d %H:%M:%S.%f'))
        prices.append(x["value"])
    return [dates, prices]

def plotAllSaltAndCarbon():
    carbon_data = getAllCarbon()
    salt_data = getAllSalt()
    carbonAX = plt.subplot()
    carbonAX.set_xlabel('dates')
    carbonAX.set_ylabel('carbon price')
    carbonAX.plot(carbon_data[0], carbon_data[1], color = 'blue', label='carbon')
    plt.legend(loc='upper center')
    saltAX = carbonAX.twinx()
    saltAX.set_xlabel('dates')
    saltAX.set_ylabel('salt price')
    saltAX.plot(salt_data[0], salt_data[1], color='red', label='salt')

plotAllSaltAndCarbon()
plt.title('carbon vs salt price')
plt.legend()
plt.show()