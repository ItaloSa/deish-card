from math import ceil

cards = 0
stores = 0

def card_register(cardsNumber,flag,name,limit):
    data = {}
    limit = float(ceil(int(limit)*0.3))
    cardNumber = cardsNumber
    data["flag"] =  flag
    data["name"] = name
    data["totalLimit"] = limit
    data["limitAviable"] = limit
    return cardNumber,data
    