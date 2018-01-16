from rbTree import Tree
import os
import json

class Controller():
    def __init__(self, path):
        self.__path = path
        self.__boot = self.initializer()

    def initializer(self):
        if self.path_exists(self.__path):
            print('db ja existe')
            #recuperar banco de dados
        else:
            path = self.__path + '/aDeishConfig.json'
            config = json.dumps({
                'colections': {}    
                }
            )
            configFile = open(path, 'w')
            configFile.write(config)
            configFile.close()
                
    def path_exists(self, path):
        if not os.path.exists(path):
            os.mkdir(path)
            return False
        else:
            return True

    def new_arq(self, name):
        arq = open(name, 'w')
        arq.close()

class DeishDb():

    def __init__(self, path='deish-db'):
        self._colections = {}
        self.__path = path
        self.__controller = Controller(path)

    def deish(self):
        return {'mensage': "Hello, i'm here! i'm in version pre-alpha. Enjoy, but be careful :-)"}

    def get_colections(self):
        #lista de colecoes
        return self._colections
    
    def colection_exists(self, colection):
        if not colection in self._colections:
            return False
        else:
            return True
        
    def new_colection(self, colection):
        if not self.colection_exists(colection):
            path = self.__path + '/' + colection + '.json'
            self._colections[colection] = {'tree': Tree(), 'path': path}
            self.__controller.new_arq(path)
            print('Colection created')
            return {'mensage': 'Colection created'}
        else:
            print('Colection exists')
            return {'mensage': 'Colection exists'}
        
    def push(self, colection, key, data):
        if self.colection_exists(colection):
            colectionSrc = self._colections[colection]['tree']
            colectionSrc.add(key, data)
            return {'mensage': 'Ok'}
        else:
            self.new_colection(colection)
            return self.push(colection, key, data)

    def get(self, colection, key=None):
        if self.colection_exists(colection):
            colectionSrc = self._colections[colection]['tree']
            if key is None:
                carryData = colectionSrc.inOrderGet()
                if carryData is None:
                    return {'mensage': 'This colection is empty'}
                else:
                    return carryData
            else:
                item = colectionSrc.search(key)
                return item.getData()
        else:
            return {'mensage': 'Not Found'}

    def update(self, colection, key, data):
        if self.colection_exists(colection):
            colectionSrc = self._colections[colection]['tree'].search(key).getData()
            colectionSrc.update(data)
            return {'mensage': 'Ok'}
        else:
            return {'mensage': 'Not Found'}
    
    def remove(self, colection, key=None):
        if self.colection_exists(colection):
            colectionSrc = self._colections[colection]['tree']
            if key is not None:
                remove = colectionSrc.delete(key)
                if remove is None:
                    return {'mensage': 'Not Found'}
                else:
                    if colectionSrc.inOrderGet() is None:
                        self.remove(colection)
                        return {'mensage': 'item %d and colection %s deleted' %(key, colection)}
                    return remove.getData()
            else:
                self._colections.pop(colection)
                return {'mensage': 'Colection %s deleted' %(colection)}
