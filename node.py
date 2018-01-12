class Node():
    def __init__(self, treeNone, key, data=None):
        self._key = key
        self._data = data
        self._father = treeNone
        self._left = treeNone
        self._right = treeNone
        self._color = ''

    def __str__(self):
        return str(self._key)

    def __repr__(self):
        return str(self._key)
    
    def getColor(self):
        return self._color

    def getData(self):
        return self._data

    def getFather(self):
        return self._father

    def getKey(self):
        return self._key   

    def getLeft(self):
        return self._left

    def getRight(self):
        return self._right

    def setColor(self, value):
        self._color = value

    def setData(self, value):
        self._data = value

    def setFather(self, value):
        self._father = value

    def setKey(self, value):
        self._key = value
  
    def setLeft(self, value):
        self._left = value
    
    def setRight(self, value):
        self._right = value
