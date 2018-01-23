class RBNode():
    def __init__(self, Key):
        self.__Key = Key
        self.__left = None
        self.__right = None
        self.__pai = None
        self.__cor = "black"
        self.__dados = {}

    def getDado(self):
        return self.__dados

    def setdados(self, chave, mudanca):
        self.__dados[chave] = mudanca

    def getKey(self):
        return self.__Key

    def setKey(self, novoKey):
        self.__Key = novoKey

    def getFilhoEsquerdo(self):
        return self.__left

    def setFilhoEsquerdo(self, novoFilho):
        self.__left = novoFilho

    def getFilhoDireito(self):
        return self.__right

    def setFilhoDireito(self, Novofilho):
        self.__right = Novofilho

    def getPai(self):
        return self.__pai

    def setPai(self, novoPai):
        self.__pai = novoPai

    def getCor(self):
        return self.__cor

    def setCor(self, cor):
        self.__cor = cor


class RBTree():
    def __init__(self):
        self.__none = RBNode(None)
        self.__none.setFilhoDireito(self.__none)
        self.__none.setFilhoEsquerdo(self.__none)
        self.__none.setPai(self.__none)
        self.__raiz = self.__none
        self.__carry = {}

    def getRaiz(self):
        return self.__raiz

    def setRaiz(self, novaRaiz):
        self.__raiz = novaRaiz

    def getNone(self):
        return self.__none

    def inorder_Tree_Walk(self, x):
        if x != self.__none:
            self.inorder_Tree_Walk(x.getFilhoEsquerdo())
            print(x.getKey(), x.getCor())
            self.inorder_Tree_Walk(x.getFilhoDireito())

    def preorder_tree_Walk(self, x):
        if x != self.__none:
            print(x.getKey(), x.getCor())
            self.preorder_tree_Walk(x.getFilhoEsquerdo())
            self.preorder_tree_Walk(x.getFilhoDireito())

    def tree_Minimum(self, nodo):
        while nodo.getFilhoEsquerdo() != self.getNone():
            nodo = nodo.getFilhoEsquerdo()
        return nodo

    def tree_Maximum(self, nodo):
        while nodo.getFilhoDireito() != self.getNone():
            nodo = nodo.getFilhoDireito()
        return nodo

    def tree_Sucessor(self, nodo):
        if nodo.getFilhoDireito() != self.getNone():
            return self.tree_Minimum(nodo.getFilhoDireito())
        y = nodo.getPai()
        while y != self.getNone() and nodo == y.getFilhoDireito():
            nodo = y
            y = y.getPai()
        return y

    def recursive_tree_search(self, x, value):
        if x == self.__none or value == x.getKey():
            return x
        if value < x.getKey():
            return self.recursive_tree_search(x.getFilhoEsquerdo(), value)
        else:
            return self.recursive_tree_search(x.getFilhoDireito(), value)

    def rightRotate(self, nodo):
        y = nodo.getFilhoEsquerdo()
        nodo.setFilhoEsquerdo(y.getFilhoDireito())
        if y.getFilhoDireito() != self.__none:
            y.getFilhoDireito().setPai(nodo)
        y.setPai(nodo.getPai())
        if nodo.getPai() == self.__none:
            self.setRaiz(y)
        elif nodo == nodo.getPai().getFilhoDireito():
            nodo.getPai().setFilhoDireito(y)
        else:
            nodo.getPai().setFilhoEsquerdo(y)
        y.setFilhoDireito(nodo)
        nodo.setPai(y)

    def leftRotate(self, nodo):
        y = nodo.getFilhoDireito()
        nodo.setFilhoDireito(y.getFilhoEsquerdo())
        if y.getFilhoEsquerdo() != self.__none:
            y.getFilhoEsquerdo().setPai(nodo)
        y.setPai(nodo.getPai())
        if nodo.getPai() == self.__none:
            self.setRaiz(y)
        elif nodo == nodo.getPai().getFilhoEsquerdo():
            nodo.getPai().setFilhoEsquerdo(y)
        else:
            nodo.getPai().setFilhoDireito(y)
        y.setFilhoEsquerdo(nodo)
        nodo.setPai(y)

    def RBInsert(self, nodo):
        y = self.__none
        x = self.getRaiz()
        while x != self.__none:
            y = x
            if nodo.getKey() < x.getKey():
                x = x.getFilhoEsquerdo()
            else:
                x = x.getFilhoDireito()
        nodo.setPai(y)
        if y == self.__none:
            self.setRaiz(nodo)
        elif nodo.getKey() < y.getKey():
            y.setFilhoEsquerdo(nodo)
        else:
            y.setFilhoDireito(nodo)
        nodo.setFilhoDireito(self.__none)
        nodo.setFilhoEsquerdo(self.__none)
        nodo.setCor("red")
        self.RB_Insert_Fixup(nodo)

    def RB_Insert_Fixup(self, nodo):
        while nodo.getPai().getCor() == "red":
            if nodo.getPai() == nodo.getPai().getPai().getFilhoEsquerdo():
                y = nodo.getPai().getPai().getFilhoDireito()
                if y.getCor() == "red":
                    nodo.getPai().setCor("black")
                    y.setCor("black")
                    nodo.getPai().getPai().setCor("red")
                    nodo = nodo.getPai().getPai()
                else:
                    if nodo == nodo.getPai().getFilhoDireito():
                        nodo = nodo.getPai()
                        self.leftRotate(nodo)
                    nodo.getPai.setCor("black")
                    nodo.getPai().getPai().setCor("red")
                    self.rightRotate(nodo.getPai().getPai())
            else:
                y = nodo.getPai().getPai().getFilhoEsquerdo()
                if y.getCor() == "red":
                    nodo.getPai().setCor("black")
                    y.setCor("black")
                    nodo.getPai().getPai().setCor("red")
                    nodo = nodo.getPai().getPai()
                else:
                    if nodo == nodo.getPai().getFilhoEsquerdo():
                        nodo = nodo.getPai()
                        self.rightRotate(nodo)
                    nodo.getPai().setCor("black")
                    nodo.getPai().getPai().setCor("red")
                    self.leftRotate(nodo.getPai().getPai())
        self.getRaiz().setCor("black")

    def transplant(self, u, v):
        if u.getPai() == self.__none:
            self.setRaiz(v)
        elif u == u.getPai().getFilhoEsquerdo():
            u.getPai().setFilhoEsquerdo(v)
        else:
            u.getPai().setFilhoDireito(v)

        v.setPai(u.getPai())

    def RBDelete(self, nodo):
        y = nodo
        yCorOriginal = y.getCor()
        if nodo.getFilhoEsquerdo() == self.__none:
            x = nodo.getFilhoDireito()
            self.transplant(nodo, nodo.getFilhoDireito())
        elif nodo.getFilhoDireito() == self.__none:
            x = nodo.getFilhoEsquerdo()
            self.transplant(nodo, nodo.getFilhoEsquerdo())
        else:
            y = self.tree_Minimum(nodo.getFilhoDireito())
            yCorOriginal = y.getCor()
            x = y.getFilhoDireito()
            if y.getPai() == nodo:
                x.setPai(y)
            else:
                self.transplant(y, y.getFilhoDireito())
                y.setFilhoDireito(nodo.getFilhoDireito())
                y.getFilhoDireito().setPai(y)
            self.transplant(nodo, y)
            y.setFilhoEsquerdo(nodo.getFilhoEsquerdo())
            y.getFilhoEsquerdo().setPai(y)
            y.setCor(nodo.getCor())
        if yCorOriginal == "black":
            self.deleteFix(x)

    def RB_Delete_Fixup(self, nodo):
        while nodo != self.getRaiz() and nodo.getCor() == "black":
            if nodo == nodo.getPai().getFilhoEsquerdo():
                w = nodo.getPai().getFilhoDireito()
                if w.getCor() == "red":
                    w.setCor("black")
                    nodo.getPai().setCor("red")
                    self.leftRotate(nodo.getPai())
                    w = nodo.getPai().getFilhoDireito()
                if w.getFilhoEsquerdo().getCor() == "black" and w.getFilhoDireito().getCor() == "black":
                    w.setCor("red")
                    nodo = nodo.getPai()
                else:
                    if w.getFilhoDireito().getCor() == "black":
                        w.getFilhoEsquerdo().setCor("black")
                        w.setCor("red")
                        self.rightRotate(w)
                        w = nodo.getPai().getFilhoDireito()
                    w.setCor(nodo.getPai().getCor())
                    nodo.getPai().setCor("black")
                    w.getFilhoDireito().setCor("black")
                    self.leftRotate(nodo.getPai())
                    nodo = self.getRaiz()
            else:
                w = nodo.getPai().getFilhoEsquerdo()
                if w.getCor() == "red":
                    w.setCor("black")
                    nodo.getPai().setCor("red")
                    self.rightRotate(nodo.getPai())
                    w = nodo.getPai().getFilhoEsquerdo()()
                if w.getFilhoDireito().getCor() == "black" and w.getFilhoEsquerdo().getCor() == "black":
                    w.setCor("red")
                    nodo = nodo.getPai()
                else:
                    if w.getFilhoEsquerdo().getCor() == "black":
                        w.getFilhoDireito().setCor("black")
                        w.setCor("red")
                        self.leftRotate(w)
                        w = nodo.getPai().getFilhoEsquerdo()
                    w.setCor(nodo.getPai().getCor())
                    nodo.getpai().setCor("black")
                    w.getFilhoEsquerdo.setCor("black")
                    self.rightRotate(nodo.getPai())
                    nodo = self.getRaiz()
        nodo.setCor("black")

    def deleteFix(self, x):
        while x != self.getRaiz() and x.getCor() == "black":
            if x == x.getPai().getFilhoEsquerdo():
                w = x.getPai().getFilhoDireito()
                if w.getCor() == "red":
                    w.setCor("black")
                    x.getPai().setCor("red")
                    self.leftRotate(x.getPai())
                    w = x.getPai().getFilhoDireito()
                if w.getFilhoEsquerdo().getCor() == "black" and w.getFilhoDireito().getCor() == "black":
                    w.setCor("red")
                    x = x.getPai()
                else:
                    if w.getFilhoDireito().getCor() == "black":
                        w.getFilhoEsquerdo().setCor("black")
                        w.setCor("red")
                        self.rightRotate(w)
                        w = x.getPai().getFilhoDireito()
                    w.setCor(x.getPai().getCor())
                    x.getPai().setCor("black")
                    w.getFilhoDireito().setCor("black")
                    self.leftRotate(x.getPai())
                    x = self.getRaiz()
            else:
                w = x.getPai().getFilhoEsquerdo()
                if w.getCor() == "red":
                    w.setCor("black")
                    x.getPai().setCor("red")
                    self.rightRotate(x.getPai())
                    w = x.getPai().getFilhoEsquerdo()()
                if w.getFilhoDireito().getCor() == "black" and w.getFilhoEsquerdo().getCor() == "black":
                    w.setCor("red")
                    x = x.getPai()
                else:
                    if w.getFilhoEsquerdo().getCor() == "black":
                        w.getFilhoDireito().setCor("black")
                        w.setCor("red")
                        self.leftRotate(w)
                        w = x.getPai().getFilhoEsquerdo()()
                    w.setCor(x.getPai().getCor())
                    x.getPai().setCor("black")
                    w.getFilhoEsquerdo().setCor("black")
                    self.rightRotate(x.getPai())
                    x = self.getRaiz()
        x.setCor("black")

    def storeInorder(self, x):
        if x != self.__none:
            self.storeInorder(x.getFilhoEsquerdo())
            print(("Id: %d - Loja: %s - Valor: %.2f") %(x.getKey(), x.getDado()["name"], x.getDado()["receivableAmount"]))
            self.storeInorder(x.getFilhoDireito())
    
    def inOrderGet(self):
        if self.__raiz is not self.__none:
            root = self.__raiz
            self.getData(root)
            out = self.__carry
            self.__carry = {}
            return out
        else:
            return None

    def getData(self, node):
        if node != self.__none:
            self.getData(node.getFilhoEsquerdo())
            self.__carry[str(node.getKey())] = node.getDado()
            self.getData(node.getFilhoDireito())
