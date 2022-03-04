import priceGetters as getter
import numpy as np 
import re


def GetAndRefinePrices():

    t = getter.getPrices()
    arr = np.array(t)

    cp_raw = arr[0].split()
    ss_raw = arr[1].split()

    cp = float(re.findall( r'\d+\.*\d*', cp_raw[0])[0])
    ss = float(re.findall( r'\d+\.*\d*', ss_raw[0])[0])
    return np.array([cp,ss])
