import math

def testPrices():
    carbon_current = 80
    carbon_previous = 87

    salt_current = 2.55
    salt_previous = 2.55
    return [carbon_current, carbon_previous, salt_current, salt_previous]

def applyTransactionFee(cost, fee_decimal):
    return cost * (1 - fee_decimal)


# this estimate uses 0.9115. It is the percentage of salt funds which is currently made up of nz carbon to our knowledge
def estimateNextSaltPrice(carbon_current, carbon_previous, salt_current):
    carbon_diff_percent = (carbon_current - carbon_previous) / carbon_previous
    salt_price_estimate = salt_current * (1 + (carbon_diff_percent * 0.9115))
    print(salt_price_estimate)
    return salt_price_estimate


# this estimate uses thomas observation that every $0.30 change in the carbon price reflects a 1c change in the salt price
def estimateNextSaltPriceThomas(carbon_current, carbon_previous, salt_current):
    return salt_current + ((carbon_current - carbon_previous)/0.25)*0.01