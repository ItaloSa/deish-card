from math import ceil
from RBTreeTest import *
import datetime

cardsTree = RBTree()
storesTree = RBTree()

cards = 0
stores = 0

def card_register(cardsNumber, flag, name, limit):
    x = RBNode(cardsNumber)
    limit = float(ceil(int(limit)*0.3))
    x.setdados("flag",flag)
    x.setdados("name",name)
    x.setdados("totalLimit",limit)
    x.setdados("limitAviable",limit)
    x.setdados("relatory", [])
    cardsTree.RBInsert(x)
    return x.getKey(),x.getdado()
    

def store_register(storeNumber, name, adress, open, close):
    x = RBNode(storeNumber)
    storeNumber = storeNumber
    x.setdados("name",name)
    x.setdados("adress",adress)
    x.setdados("operatingHours", [])
    x.setdados("relatory", [])
    x.getdado()["operatingHours"].append(open)
    x.getdado()["operatingHours"].append(close)
    x.setdados("monthlyBalance", 0.0)
    x.setdados("receivableAmount",0.0)
    storesTree.RBInsert(x)
    return x.getKey(),x.getdado()

def store_search(valor):
    k = storesTree.recursive_tree_search(storesTree.getRaiz(), valor)
    if k != storesTree.getNone():
        return True,k
    else:
        return False
    
def hour_verify(store):
    currentDT = datetime.datetime.now()
    x = int(currentDT.hour)
    print(x)
    openTime = store.getdado()["operatingHours"][0]
    closeTime = store.getdado()["operatingHours"][1]
    if x >= (openTime) and x <= int(closeTime):
        return True
    else:
        return False
    
def error_time(store):
    x = store.getdado()
    name = x["name"]
    open = float(x["operatingHours"][0])
    close = float(x["operatingHours"][1])
    return name,open,close

def cards_serach(valor):
    k = cardsTree.recursive_tree_search(cardsTree.getRaiz(), valor)
    if k != cardsTree.getNone():
        return True,k
    else:
        return False

def limit_verify(card):
    x = card.getdado()
    limite = x["limitAviable"]
    return limite
    
def card_func(value, card):
    x = card.getdado()
    x["limitAviable"] -= value
    x["relatory"].append(value)
    return x
    
def store_func(value,store):
    x = store.getdado()
    x["monthlyBalance"] += value
    discount = value*0.02
    payment = value- discount
    x["receivableAmount"] += payment
    x["relatory"].append(value)
    return x

def quicksort(A,p,r):
    if p < r:
        q = partition(A,p,r)
        quicksort(A, p,q-1)
        quicksort(A,p+1,r)

        
def partition(a,p,r):
    x = a[r]
    i = p-1
    for j in range(p,r):
        if a[j] >=x:
            i = i+1
            a[i],a[j] = a[j],a[i]
    a[i+1],a[r] = a[r],a[i+1]
    
    return i+1

def relatory(nodo):
    string= ""
    x = nodo.getdado()
    lista = x["relatory"]
    a = quicksort(lista, 0,len(lista)-1)
    for i in lista:
        string+=str(i)+" "
    return string
    
        
def payment_relatory():
    storesTree.inorder(storesTree.getRaiz())
      
    
    
    
     
    
    
    