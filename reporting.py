import db_connect as db
import matplotlib.pyplot as plt
import numpy as np

def plotSaltAndCarbon(startDate="2000-01-01", endDate="2029-12-12"):
    carbon_data = db.getPricesByDate(startDate, endDate, 'carbon')
    salt_data = db.getPricesByDate(startDate, endDate, 'salt')
    carbonAX = plt.subplot()
    carbonAX.set_xlabel('dates')
    carbonAX.set_ylabel('Carbon Price')
    carbonAX.plot(carbon_data.keys(), carbon_data.values(), color = 'blue', label='carbon')
    plt.legend(loc='upper center')
    saltAX = carbonAX.twinx()
    saltAX.set_xlabel('dates')
    saltAX.set_ylabel('Salt Share Price')
    saltAX.plot(salt_data.keys(), salt_data.values(), color='red', label='salt')

def plotAllSalt():
    data = db.getAllSaltFromDB()
    dates = data.keys()
    prices = data.values()
    plt.plot(dates, prices, color='red', label='salt')
    
plotSaltAndCarbon("2020-01-01","2022-12-01")
plt.title('carbon vs salt price')
plt.legend()
plt.show()

# print(getPriceByDateAndType("2001-01-01", "2044-01-01", 'carbon'))
    
# plotAllSalt()
# plt.show()