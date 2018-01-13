from math import ceil

cards = 0
stores = 0

def card_register(cardsNumber, flag, name, limit):
    data = {}
    limit = float(ceil(int(limit)*0.3))
    cardNumber = cardsNumber
    data["flag"] =  flag
    data["name"] = name
    data["totalLimit"] = limit
    data["limitAviable"] = limit
    return cardNumber,data

def store_register(storeNumber, name, adress, operatingHours):
    data = {}
    storeNumber = storeNumber
    data["name"] = name
    data["adress"] = adress
    data["operatingHours"] = []
    hours = operatingHours.split(" ")
    for i in hours:
        j = float(i)
        data["operatingHours"].append(j)        
    data["monthlyBalance"] = 0.0
    data["receivableAmount"] = 0.0
    return storeNumber,data
    