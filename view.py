from controller import *


print(('welcome to deish credit card system').upper())
print('PRESS 1: TO CARD REGISTER')
print('PRESS 2: TO REGISTER YOUR STORE')
print('PRESS 3: MAKE A PURCHASE')
print('PRESS 4: TO MAKE A RELATORY')
print('PRESS 5: TO CLOSE THE SYSTEM')


while True:    
    userChoice = input("PRESS 1, 2, 3, 4 OR 5: ")
    if userChoice == "1":
        cards+=1
        flag = input("Card Flag: ")
        client_Name = input("Your Name: ")
        while True:
            totalLimit = input("Input your monthly income:(ONLY NUMBERS): ")
            if int(totalLimit):
                break
        card = card_register(cards, flag, client_Name, totalLimit)
        print("%s Your Credit card has been successfully registered!" % (card[1]["name"]))
        print("Your card number is : %d"%(card[0]))
        print("You total limit is: %.2f" % (card[1]["totalLimit"]))
        print("Enjoy")
    
    elif userChoice == "2":
        stores +=1
        storeName = input("Your store name: ")
        storeAdress = input("Adress: ")
        operatingHours = input("Operating Hours: (This format HH.MM - HH.MM) 00.00 to 23.59")
        store = store_register(stores, storeName, storeAdress, operatingHours)
        print("%s has been successfully registered!" % (store[1]["name"]))
        print("Your store number is : %d"%(store[0]))
        print("Enjoy")
        


