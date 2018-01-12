class Nil():
    def __init__(self):
        self._color = 'black'
        self._key = None
        self._father = self
        self._left = self
        self._right = self
    
    def __repr__(self):
        return 'None'

    def __str__(self):
        return 'None'
    
    def getColor(self):
        return self._color

    def getFather(self):
        return self._father

    def getLeft(self):
        return self._left

    def getRight(self):
        return self._right

    def setColor(self, value):
        self._color = value

    def setFather(self, value):
        self._father = value

    def setLeft(self, value):
        self._left = value
    
    def setRight(self, value):
        self._right = value
