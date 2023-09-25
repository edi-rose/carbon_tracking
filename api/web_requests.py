import requests
from datetime import datetime
from bs4 import BeautifulSoup

def getCarbonNews():
    url = "https://www.carbonnews.co.nz/rssfeed.asp?tag=21"
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    return response.text

def getPrices(): 
    html  = getCarbonNews()
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('item')
    market_updates = []
    for item in items:
        if is_market_latest(item.title.text):
            obj = {
                'price': parsePrice(item.title.text),
                'date': formatDate(item.pubdate.text)
            }
            market_updates.append(obj)
    return market_updates

def is_market_latest(title='blank'): 
    if 'MARKET LATEST' in title: 
        return True
    else:
        return False
    
def formatDate(str):
    date = datetime.strptime(str, '%a, %d %b %Y %H:%M:%S ')
    new_str = date.strftime('%Y/%m/%d')
    return new_str


def parsePrice(title='blank'):
    return title.split('$',1)[1].split("\r",1)[0]

getPrices()