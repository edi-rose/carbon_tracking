import csv
import time
from datetime import datetime
import db_connect as db

# This file is used to fill in the gaps of the carbon price data for when i forget to turn on the bot
# Update the csv here: https://raw.githubusercontent.com/theecanmole/nzu/master/nzu-weekly-prices-data.csv

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
        db.insertPrice('carbon', key + " 00:00:00", dict(refined)[key])
