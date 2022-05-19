from itertools import combinations
from math import comb
from gameMap import GameMap
test = GameMap('mapa.txt',10,10)
print()

class Combination:
    def __init__(self,listaPersonagem):
        self.listaPersonagem = listaPersonagem
        self.bestCombination = list()
        return 
    
    def getBestCombination(self):
        return self.bestCombination
    
    def generateCombination(self):
        listaAux = list()
        listaP = self.listaPersonagem
        #comb_1 = combinations(listaP,1)
        #[listaAux.append(p) for p in comb_1]
        #comb_2 = combinations(listaP,2)
        #[listaAux.append(p) for p in comb_2]
        comb_3 = combinations(listaP,3)
        [listaAux.append(p) for p in comb_3]
        comb_4 = combinations(listaP,4)
        [listaAux.append(p) for p in comb_4]
        comb_5 = combinations(listaP,5)
        [listaAux.append(p) for p in comb_5]
        comb_6 = combinations(listaP,6)
        [listaAux.append(p) for p in comb_6]
        comb_7 = combinations(listaP,7)
        [listaAux.append(p) for p in comb_7]
        
        listaAux = list(listaAux)
        print(listaAux)
        

#Testando 
c = Combination(list(test.get_agility().keys()))
c.generateCombination()

        

