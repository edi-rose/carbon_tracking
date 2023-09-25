from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import data_helpers as helper
import time

chrome_driver = '/Users/edirose/Desktop/drivers/chromedriver'
options = Options()
options.headless = True

def getCarbonIsOpen():
    driver = getHeadlessDriver()
    driver.get("https://commtrade.co.nz")
    try:  
        time.sleep(5)
        isOpen = False
        
        isOpen = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "marketstatus"))
        ).text
    except:
        print('could not find out whether market is open or not')
    finally:
        if isOpen == "MARKET IS OPEN":
            return True
        if isOpen == "MARKET IS CLOSED":
            return False
        else:
            print('GetCarbonIsOpen returned with unexpected status: ', isOpen)
            return False

def getCarbonPrice():
    driver = getHeadlessDriver()
    driver.get("https://commtrade.co.nz")
    try:
        cp_raw = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "ctl00_Products_Td3_0"))
        ).text
    except: 
        print('could not getCarbonPrice')
    finally:
        return helper.cleanPrice(cp_raw)

def getSaltPrice():   
    driver = getHeadlessDriver()
    driver.get("https://www.nzx.com/instruments/CO2")
    try:
        ss_raw = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/section/div[2]/div/section[1]/div/div[1]/h1"))
        ).text
    except: 
        print('could not getSaltSharePrice')
    finally:
        return helper.cleanPrice(ss_raw)


def getHeadlessDriver():
    gecko_driver = '/Users/edirose/Desktop/drivers/geckodriver'
    options = Options()
    options.headless = False
    return webdriver.Firefox(executable_path=gecko_driver ,options=options)

def getSaltNTA():   
    driver = getHeadlessDriver()
    driver.get("https://www.nzx.com/instruments/CO2")
    try:
        ss = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/section/div[2]/div/div[1]/div[3]/div/table/tbody/tr[3]/td[2]"))
        ).text
    except: 
        print('could not getSaltSharePrice')
    finally:
        return helper.cleanPrice(ss)

def getAuctionDates():
    driver = getHeadlessDriver()
    driver.get("https://www.etsauctions.govt.nz/public/auction_noticeboard")
    card_body_div = driver.find_element(By.CSS_SELECTOR, 'div.card-body')
    elements = card_body_div.find_elements(By.TAG_NAME, 'a')
    dates= []
    links = []

    for element in elements:
        str = element.get_attribute('href')
        links.append(str)

    for link in links:
        driver.get(link)
        try:
            date = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='auction_information']/tbody/tr[3]/td"))
            ).text
        except:
            continue
        else:
            dates.append(helper.changeDateFromSlashesToDashes(date))
    driver.quit()
    return dates

