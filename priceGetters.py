
from lib2to3.pgen2.driver import Driver
from selenium import webdriver

driver = webdriver.Safari()


def getCarbonPrice():
    driver.get("https://commtrade.co.nz")
    p = driver.find_element_by_id("ctl00_Products_Td3_0").text
    ##driver.quit()
    return p


def getSaltSharePrice():
    driver.get("https://www.nzx.com/instruments/CO2")
    p2 = driver.find_element_by_xpath("/html/body/section/div[2]/div/section[1]/div/div[1]/h1").text
    return p2

def getPrices():
    v={
        'carbon': getCarbonPrice(),
        'salt_share': getSaltSharePrice()
    }
    driver.quit()
    return v
