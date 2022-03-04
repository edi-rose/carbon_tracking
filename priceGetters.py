
from lib2to3.pgen2.driver import Driver
from matplotlib.pyplot import get
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Safari()


def getCarbonPrice():
    driver.get("https://commtrade.co.nz")
    try:
        cp_raw = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "ctl00_Products_Td3_0"))
        ).text
    finally:
        return cp_raw

def getSaltSharePrice():   
    driver.get("https://www.nzx.com/instruments/CO2")
    try:
        ss = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/section/div[2]/div/section[1]/div/div[1]/h1"))
        ).text
    finally:
        return ss

def getPrices():
    try: cp_raw= getCarbonPrice()
    finally: ss = getSaltSharePrice()
    v=  [ss, cp_raw]
    driver.close()
    return v

##print(getSaltSharePrice())

