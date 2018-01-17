from atuante import *


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
        while True:
            openTime = input("Opening time: (Only Hours: ) 01 to 23:")
            if int(openTime):
                closeTime = input("Close time: (Only Hours: ) 01 to 24:")
                if int(closeTime):
                    break
        
        store = store_register(stores, storeName, storeAdress, int(openTime), int(closeTime))
        print("%s has been successfully registered!" % (store[1]["name"]))
        print("Your store number is : %d"%(store[0]))
        print("Enjoy")
        
    elif userChoice == "3":
        while True:
            storeBuy = input("ENTER STORE ID OR X TO RETURN:")
            if storeBuy =="X":
                break
            if int(storeBuy):
                atualStore = store_search(int(storeBuy))
                if atualStore:
                    hourVerify = hour_verify(atualStore[1])
                    if hourVerify:
                        while True:
                            cardId = input("ENTER YOUR CARD ID OR X TO RETURN : ")
                            if cardId == "X":
                                break
                            if int(cardId):
                                atualCard = cards_serach(int(cardId))
                                if atualCard:
                                    while True:
                                        purchaseValue = input("The value of the purchase: ")
                                        if float(purchaseValue):
                                            limit = limit_verify(atualCard[1])                                          
                                            if limit >= float(purchaseValue):
                                                ob1 = card_func(float(purchaseValue), atualCard[1])
                                                ob2 = store_func(float(purchaseValue), atualStore[1])
                                                print("Purchase made successfully.")
                                                break
                                            else:
                                                print("insufficient limit")
                                                break

                                        else:
                                            print("invalid value")
                                        
                                
                                else:
                                    print("card does not exist")
                                    break 
                                            
                                       
                            else:
                                print("card does not exist")
                                break 
                                
                        
                    else:
                        x = error_time(atualStore[1])
                        print("You can't do that. %s is closed, come back %.2f to %.2f"%(x[0],x[1],x[2])) 
                        break              
                else:
                    print("store does not exist")
                    break
            else:
                print("store does not exist")
                break
                
                
    elif userChoice == "4":
        print('PRESS 1: TO CARD RELATORY')
        print('PRESS 2: TO STORE RELATORY')
        print('PRESS 3: PAYMENT RELATORY')
        print('PRESS X: TO GO BACK TO MAIN MENU')
        while True:
            choice = input("PRESS 1, 2, 3 or X")
            if choice == "1":
                cardId = input("CARD ID:")
                if int(cardId):
                    card = cards_serach(int(cardId))
                    if card:
                        exit2 = relatory(card[1])
                        print("Suas compras em ordem decrescente de valor foram : %s"%(exit2))
                        break
                    else:
                        print("card not found")  
                        break              
                else:
                    print("card not found")
                    break
            elif choice == "2":
                storeId = input("STORE ID:")
                if int(storeId):                
                    store = store_search(int(storeId))
                    if store:
                        exit1 = relatory(store[1])
                        print("Suas vendas em ordem decresente de valor foram %s" % (exit1))
                        break
                    else:
                        print("store not found")
                        break
                else:
                    print("store not found")
                    break
            
            elif choice == "3":
                payment_relatory()
                break
                
            elif choice == "X":
                break
              
                
                
                
            
            
        
        
        
        
                
            
        
        
        





