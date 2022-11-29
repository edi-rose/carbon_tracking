import re
from datetime import datetime as dt
import json

# turn price from $1.2 -> 1.2
def cleanPrice(price):
    raw = price.split()
    return float(re.findall( r'\d+\.*\d*', raw[0])[0])

def convertToDatetime(data):
    dates = []
    prices = []
    for x in data:
        dates.append(dt.strptime(x["date"],'%Y-%m-%d %H:%M:%S.%f'))
        prices.append(x["value"])

    dictionary = dict(zip(dates, prices))
    return dictionary

def sortData(data: dict):
    sorted_dict = dict(sorted(data.items()))
    return sorted_dict

def refinePricesForReports(data):
    return sortData(convertToDatetime(json.loads(data)))