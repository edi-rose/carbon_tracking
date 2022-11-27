import csv
import time
from datetime import datetime
import db_connect as db

# this file is only needed for one time addition of historical data. 


data = []
with open("historical_carbon_prices.csv") as csvfile:
    reader = csv.reader(csvfile) # change contents to floats
    for row in reader: # each row is a list
        data.append(row)

refined = []
for row in data:
    date = datetime.strptime(row[0], '%Y/%m/%d').date()
    date_string = datetime.strftime(date, '%Y-%m-%d')
    refined.append((date_string, float(row[1])))

for key in dict(refined):
    db_price = db.getPriceWithDate(key, 'carbon')
    if(db_price =='none'):
        db.insertHistoricalPrice('carbon', key + " 00:00:00", dict(refined)[key])
