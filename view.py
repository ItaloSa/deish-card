from controller import *
import os

clear = lambda: os.system('cls')

def show_menu():
    print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
    print('█       DEISH CREDIT CARD SYSTEM       █')
    print('█                                      █')
    print('█ PRESS 1: TO CARD REGISTER            █')
    print('█ PRESS 2: TO REGISTER YOUR STORE      █')
    print('█ PRESS 3: MAKE A PURCHASE             █')
    print('█ PRESS 4: TO MAKE A RELATORY          █')
    print('█ PRESS 5: TO CLOSE THE SYSTEM         █')
    print('█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█')

def card_registration():
    print('╔ CARD REGISTRATION')
    flag = input("║ Card Flag: ")
    client_Name = input("║ Your Name: ")
    while True:
        totalLimit = input("║ Input your monthly income (only numbers): ")
        if int(totalLimit):
            break
    card = card_register(cards, flag, client_Name, totalLimit)
    print('║')
    print("║ %s Your Credit card has been successfully registered!" % (card[1]["name"]))
    print("║ Your card number is : %d"%(card[0]))
    print("║ You total limit is: %.2f" % (card[1]["totalLimit"]))
    print("╚ Enjoy")
    x = input('\n PRESS RETURN TO EXIT... ')

def store_registration():
    print('╔ STORE REGISTRATION')
    storeName = input("║ Your store name: ")
    storeAdress = input("║ Adress: ")
    while True:
        openTime = input("║ Opening time (hh:mm): ").split(':')
        print(openTime)
        if int(openTime[0]):
            closeTime = input("║ Close time: (hh:mm): ").split(':')
            if int(closeTime[0]):
                break
    print('║')
    store = store_register(stores, storeName, storeAdress, openTime, closeTime)
    print("║ %s has been successfully registered!" % (store[1]["name"]))
    print("║ Your store number is : %d"%(store[0]))
    print("╚ Enjoy")
    x = input('\n PRESS RETURN TO EXIT... ')

def purchase():
    print('╔ PURCHASE')
    while True:
        storeBuy = input("║ ENTER STORE ID OR X TO RETURN TO HOME: ")
        if storeBuy == 'X' or storeBuy == 'x':
            break
        if int(storeBuy):
            atualStore = store_search(int(storeBuy))
            if atualStore:
                hourVerify = hour_verify(atualStore[1])
                if hourVerify:                
                    cardId = input("║ ENTER YOUR CARD ID OR X TO RETURN: ")
                    if cardId == 'X' or cardId == 'x':
                        break
                    if int(cardId):
                        atualCard = cards_serach(int(cardId))
                        if atualCard:
                            while True:
                                purchaseValue = input("║ The value of the purchase: ")
                                if float(purchaseValue):
                                    limit = limit_verify(atualCard[1])                                          
                                    if limit >= float(purchaseValue):
                                        ob1 = card_func(float(purchaseValue), atualCard[1])
                                        ob2 = store_func(float(purchaseValue), atualStore[1])
                                        print("║ Purchase made successfully.")
                                        break
                                    else:
                                        print("╠ Insufficient limit!")
                                        break
                                else:
                                    print("╠ Invalid value!")                                   
                        else:
                            print("╠ Card does not exist!")
                            break    
                    else:
                        print("╠ Card does not exist!")
                        break     
                else:
                    x = error_time(atualStore[1])
                    print("╠ You can't do that. %s is closed, come back %.2f to %.2f" %(x[0],x[1],x[2])) 
                    break              
            else:
                print("╠ Store does not exist")
                break
        else:
            print("╠ Store does not exist")
            break
    print('║')
    x = input('╚ PRESS RETURN TO EXIT... ')

def show_report_menu():
    print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
    print('█          ACCOUNT BALANCE MENU        █')
    print('█ PRESS 1: TO CARD BALANCE             █')
    print('█ PRESS 2: TO STORE BALANCE            █')
    print('█ PRESS 3: PAYMENT BALANCE             █')
    print('█ PRESS X: TO RETURN TO MAIN MENU      █')
    print('█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█')

def card_balance():
    print('╔ CARD BALANCE')
    cardId = input("║ CARD ID:")
    if int(cardId):
        card = cards_serach(int(cardId))
        if card:
            exit2 = relatory(card[1])
            print("║ Your purchases in descending order of value have been: %s" %(exit2))
        else:
            print("║ Card not found")                
    else:
        print("║ Card not found")
    print('║')
    x = input('╚ PRESS RETURN TO EXIT... ')

def store_balance():
    print('╔ STORE BALANCE')
    storeId = input("║ STORE ID:")
    if int(storeId):                
        store = store_search(int(storeId))
        if store:
            exit1 = relatory(store[1])
            print("╠ Your sales in descending order of value have been: %s" % (exit1)) 
        else:
            print("║ Store not found")
    else:
        print("║ Store not found")
    print('║')
    x = input('╚ PRESS RETURN TO EXIT... ')

def report_menu():
    while True:
        clear()
        show_report_menu()
        choice = input("» INPUT")
        if choice == "1":
            clear()
            card_balance()
            break
        elif choice == "2":
            store_balance()
            clear() 
            break
        elif choice == "3":
            payment_relatory()
            clear()
            break
            
        elif choice == "X":
            break

load_data()
while True:
    #clear()      
    show_menu()    
    userChoice = input("» INPUT: ")
    if userChoice == "1":
        clear()
        cards+=1
        card_registration()
              
    elif userChoice == "2":
        clear()
        stores +=1
        store_registration()
                
    elif userChoice == "3":
        clear()
        purchase()              
                
    elif userChoice == "4":
        clear()
        report_menu()
    
    elif userChoice == "5":
        save_data()
        break