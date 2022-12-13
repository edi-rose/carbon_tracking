import re
from datetime import datetime as dt
from datetime import timedelta, date
import json

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

def getDatesBetween(start, end):
    dates = []
    start_dt = dt.strptime(start,'%Y-%m-%d')
    end_dt = dt.strptime(end,'%Y-%m-%d')
    for date in daterange(start_dt, end_dt):
        dates.append(date.strftime("%Y-%m-%d"))
    return dates
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

def refinePricesForReports(data:dict):
    return sortData(convertToDatetime(json.loads(data)))

def changeDateFromSlashesToDashes(date):
    str = dt.strptime(date, '%d/%m/%Y').strftime('%d-%m-%Y')
    return dt.strptime(str, '%d-%m-%Y')

def dateStringToDatetime(date):
    return dt.strptime(date, '%Y-%m-%d')