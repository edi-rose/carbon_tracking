
import db_connect as db
import matplotlib.pyplot as plt
import json
import numpy as np
from datetime import datetime as dt


def plotAllCarbon(): 
    data = json.loads(db.getAllCarbonFromDB()[0][0])
    dates = []
    prices = []
    for x in data:
        dates.append(dt.strptime(x["date"],'%Y-%m-%d %H:%M:%S.%f'))
        prices.append(x["value"])

    plt.plot(dates, prices)
    plt.show()
    return data
