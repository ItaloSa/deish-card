from math import ceil
import datetime, json
from tree import RBTree, RBNode
import os

class QuickSort():
    def __init__(self, A, p, r):
        self._sort = self.quicksort(A, p, r)

    def quicksort(self, A, p, r):
        if p < r:
            q = self.partition(A, p, r)
            self.quicksort(A, p, q - 1)
            self.quicksort(A, p + 1, r)


    def partition(self, a, p, r):
        x = a[r]
        i = p - 1
        for j in range(p, r):
            if a[j] >= x:
                i = i + 1
                a[i], a[j] = a[j], a[i]
        a[i + 1], a[r] = a[r], a[i + 1]

        return i + 1

class Store():
    def __init__(self):
        self.__cardsTree = RBTree()
        self.__storesTree = RBTree()
        self.__cards = 0
        self.__stores = 0
        self.__boot = self.start()
    
    def start(self):
        if os.path.isfile('data.json'):
            self.load_data()
        else:
            print('welcome')

    def load_data(self):
        arq = open("data.json", "r", encoding="utf-8")
        carry = arq.read()
        arq.close()
        data = json.loads(carry)
        
        self.__cards += data['config'][0]
        self.__stores += data['config'][1]
        
        try:
            for item in data['cards']:
                cardData = data['cards'][item]
                node = RBNode(int(item))
                node.getDado().update(cardData)
                self.__cardsTree.RBInsert(node) 
        except:
            print("No cards!")

        try:
            for item in data['stores']:
                storeData = data['stores'][item]
                node = RBNode(int(item))
                node.getDado().update(storeData)   
                self.__storesTree.RBInsert(node)
        except:
            print("No stores!")

    def save_data(self):
        out = {}
        cardsData = self.__cardsTree.inOrderGet()
        storesData = self.__storesTree.inOrderGet()
        config = [self.__cards, self.__stores]

        out.update({'cards': cardsData, 'stores': storesData, 'config': config})
        data = json.dumps(out)

        arq = open("data.json", "w", encoding="utf-8")
        arq.write(data)
        arq.close()

    def card_register(self, flag, name, limit):        
        cardsNumber = self.__cards + 1
        x = RBNode(cardsNumber)
        limit = float(ceil(int(limit) * 0.3))
        x.setdados("flag", flag)
        x.setdados("name", name)
        x.setdados("totalLimit", limit)
        x.setdados("limitAviable", limit)
        x.setdados("relatory", [])
        self.__cardsTree.RBInsert(x)
        self.__cards += 1
        return x.getKey(), x.getDado()


    def store_register(self, name, adress, open, close):
        storeNumber = self.__stores + 1
        x = RBNode(storeNumber)
        storeNumber = storeNumber
        x.setdados("name", name)
        x.setdados("adress", adress)
        x.setdados("operatingHours", [])
        x.setdados("relatory", [])
        openTime = int(open[0]) * 60 + int(open[1])
        x.getDado()["operatingHours"].append(openTime)
        closeTime = int(close[0]) * 60 + int(close[1])
        x.getDado()["operatingHours"].append(closeTime)
        x.setdados("monthlyBalance", 0.0)
        x.setdados("receivableAmount", 0.0)
        self.__storesTree.RBInsert(x)
        self.__stores += 1
        return x.getKey(), x.getDado()


    def store_search(self, valor):
        k = self.__storesTree.recursive_tree_search(self.__storesTree.getRaiz(), valor)
        if k != self.__storesTree.getNone():
            return True, k
        else:
            return False


    def hour_verify(self, store):
        currentDT = datetime.datetime.now()
        h = int(currentDT.hour)
        m = int(currentDT.minute)
        hour = h * 60 + m
        openTime = store.getDado()["operatingHours"][0]
        closeTime = store.getDado()["operatingHours"][1]
        if hour >= (openTime) and hour <= closeTime:
            return True
        else:
            return False


    def error_time(self, store):
        x = store.getDado()
        name = x["name"]
        
        open = float(x["operatingHours"][0])
        hour = int(open/60)
        minutes = open - hour*60
        openTime = "%d:%d" %(hour, minutes)
        
        close = float(x["operatingHours"][1])
        hour = int(close/60)
        minutes = close - hour*60
        closeTime = "%d:%d" %(hour, minutes)

        return name, openTime, closeTime


    def cards_serach(self, valor):
        k = self.__cardsTree.recursive_tree_search(self.__cardsTree.getRaiz(), valor)
        if k != self.__cardsTree.getNone():
            return True, k
        else:
            return False


    def limit_verify(self, card):
        x = card.getDado()
        limite = x["limitAviable"]
        return limite


    def card_func(self, value, card):
        x = card.getDado()
        x["limitAviable"] -= value
        x["relatory"].append(value)
        return x


    def store_func(self, value, store):
        x = store.getDado()
        x["monthlyBalance"] += value
        discount = value * 0.02
        payment = value - discount
        x["receivableAmount"] += payment
        x["relatory"].append(value)
        return x


    def relatory(self, nodo):
        string = ""
        x = nodo.getDado()
        lista = x["relatory"]
        QuickSort(lista, 0, len(lista) - 1)
        for i in lista:
            string += str(i) + " "
        return string


    def payment_relatory(self):
        print('SYSTEM PAYMENT BALANCE')
        print('Stores: ')
        self.__storesTree.storeInorder(self.__storesTree.getRaiz())

