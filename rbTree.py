from nil import Nil
from node import Node

class Tree(Node):

    def __init__(self):
        self._none = Nil()
        self._root = self._none
        self._carry = {}
        self._maior = 0
        self._x = 0

    def getRoot(self):
        return self._root

    def getNone(self):
        return self._none

    def __repr__(self):
        return 'Tree', self._root
    
    def __str__(self):
        return 'Tree', self._root
    
    def add(self, key, data=None):
        node = Node(self._none, key, data)
        y = self._none
        x = self._root
        while x != self._none:
            y = x
            if node.getKey() < x.getKey():
                x = x.getLeft()
            else:
                x = x.getRight()
        node.setFather(y)
        if y == self._none:
            self._root = node
        elif node.getKey() < y.getKey():
            y.setLeft(node)
        else:
            y.setRight(node)
        node.setColor('red')
        self.rbInsertFixup(node)

    def delete(self, value):
        node = self.search(value)
        if node != self._none:
            if node.getLeft() == self._none or node.getRight() == self._none:
                y = node
            else:
                y = self.successor(node)
            if y.getLeft() != self._none:
                x = y.getLeft()
            else:
                x = y.getRight()
            if x != self._none:
                x.setFather(y.getFather())
            if y.getFather() == self._none:
                self._root = x
            else:
                if y == y.getFather().getLeft():
                    y.getFather().setLeft(x)
                else:
                    y.getFather().setRight(x)
            if y != node:
                node.setKey(y.getKey())
            if y.getColor() == 'black':
                self.rbDeleteFixup(x)
            return y
        else:
            return None

    def maximum(self, node):
        while node.getRight() != self._none:
            node = node.getRight()
        return node

    def minimum(self, node):
        while node.getLeft() != self._none:
            node = node.getLeft()
        return node
    
    def leftRotate(self, node):
        y = node.getRight()
        node.setRight(y.getLeft())
        if y.getLeft() != self._none:
            y.getFather().setLeft(node)
        y.setFather(node.getFather())
        if node.getFather() == self._none:
            self._root = y
        elif node == node.getFather().getLeft():
            node.getFather().setLeft(y)
        else:
            node.getFather().setRight(y)
        y.setLeft(node)
        node.setFather(y)

    def rbDeleteFixup(self, node):
        while node != self._root and node.getColor() == 'black':
            if node == node.getFather().getLeft():
                w = node.getFather().getRight()
                if w.getColor() == 'red':
                    w.setColor('black')
                    node.getFather().setColor('red')
                    self.leftRotate(node.getFather())
                    w = node.getFather().getRight()
                if w.getLeft().getColor() == 'black' and w.getRight().getColor() == 'black':
                    w.setColor('red')
                    node = node.getFather()
                else:
                    if w.getRight().getColor() == 'black':
                        w.getLeft().setColor('black')
                        w.setColor('red')
                        self.rightRotate(w)
                        w = node.getFather().getRight()
                    w.setColor(node.getFather().getColor())
                    node.getFather().setColor('black')
                    w.getRight().setColor('black')
                    self.leftRotate(node.getFather())
                    node = self._root
            else:
                w = node.getFather().getLeft()
                if w.getColor() == 'red':
                    w.setColor('black')
                    node.getFather().setColor('red')
                    self.rightRotate(node.getFather())
                    w = node.getFather().getLeft()
                if w.getRight().getColor() == 'black' and w.getLeft().getColor() == 'black':
                    w.setColor('red')
                    node = node.getFather()
                else:
                    if w.getLeft().getColor() == 'black':
                        w.getRight().setColor('black')
                        w.setColor('red')
                        self.leftRotate(w)
                        w = node.getFather().getLeft()
                    w.setColor(node.getFather().getColor())
                    node.getFather().setColor('black')
                    w.getLeft().setColor('black')
                    self.rightRotate(node.getFather())
                    node = self._root
        node.setColor('black')

    def rbInsertFixup(self, node):
        while node.getFather().getColor() == 'red':
            if node.getFather() == node.getFather().getFather().getLeft():
                y = node.getFather().getFather().getRight()
                if y.getColor() == 'red':
                    node.getFather().setColor('black')
                    y.setColor('black')
                    node.getFather().getFather().setColor('red')
                    node = node.getFather().getFather()
                else:
                    if node == node.getFather().getRight():
                        node = node.getFather()
                        self.leftRotate(node)
                    node.getFather().setColor('black')
                    node.getFather().getFather().setColor('red')
                    self.rightRotate(node.getFather().getFather())
            else:
                y = node.getFather().getFather().getLeft()
                if y.getColor() == 'red':
                    node.getFather().setColor('black')
                    y.setColor('black')
                    node.getFather().getFather().setColor('red')
                    node = node.getFather().getFather()
                else:
                    if node == node.getFather().getLeft():
                        node = node.getFather()
                        self.rightRotate(node)
                    node.getFather().setColor('black')
                    node.getFather().getFather().setColor('red')
                    self.leftRotate(node.getFather().getFather())
        self._root.setColor('black')
    
    def rightRotate(self, node):
        y = node.getLeft()
        node.setLeft(y.getRight())
        if y.getRight() != self._none:
            y.getFather().setRight(node)
        y.setFather(node.getFather())
        if node.getFather() == self._none:
            self._root = y
        elif node == node.getFather().getRight():
            node.getFather().setRight(y)
        else:
            node.getFather().setLeft(y)
        y.setRight(node)
        node.setFather(y)

    def search(self, value):
        node = self._root
        while node != self._none and value != node.getKey():
            if value < node.getKey():
                node = node.getLeft()
            else:
                node = node.getRight()
        return node

    def successor(self, node):
        if node.getRight() != self._none:
            return self.minimum(node.getRight())
        y = node.getFather()
        while y != self._none and node == y.getRight():
            node = y
            y = node.getFather()
        return y

    #views
    def inOrderGet(self):
        if self._root is not self._none:
            rainode = self._root
            self.inOrder(rainode)
            out = self._carry
            self._carry = {}
            return out
        else:
            return None

    def inOrder(self, node):
        if node != self._none:
            self.inOrder(node.getLeft())
            self._carry[str(node.getKey())] = node.getData()
            self.inOrder(node.getRight()) 
