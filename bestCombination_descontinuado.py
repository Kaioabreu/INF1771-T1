from itertools import combinations
from math import comb
from random import random, shuffle
from gameMap import GameMap
from run_better_route import Personagem
import random
from operator import itemgetter
 
test = GameMap('mapa.txt',300,82)
print()

class Combination:
    def __init__(self,listaPersonagem):
        self.listaPersonagem = listaPersonagem
        self.bestCombination = open("bestCombination.txt","r").readline()
        return 
    
    def getBestCombination(self):
        return self.bestCombination
    
    def generateCombination(self):
        listaAux = []
        listaP = self.listaPersonagem
        for i in listaP:            
            listaAux.append([i.nome])
        comb_2 = combinations(listaP,2)
        for p in comb_2:
            l=[]
            for i in p:
                l.append(i.nome)
            listaAux.append(l) 
        comb_3 = combinations(listaP,3)
        for p in comb_3:
            l=[]
            for i in p:
                l.append(i.nome)
            listaAux.append(l) 
        '''
        comb_4 = combinations(listaP,4)
        for p in comb_4:
            l=[]
            for i in p:
                l.append(i.nome)
            listaAux.append(l) 
        comb_5 = combinations(listaP,5)
        for p in comb_5:
            l=[]
            for i in p:
                l.append(i.nome)
            listaAux.append(l) 
        comb_6 = combinations(listaP,6)
        for p in comb_6:
            l=[]
            for i in p:
                l.append(i.nome)
            listaAux.append(l) 
        comb_7 = combinations(listaP,7)
        for p in comb_7:
            l=[]
            for i in p:
                l.append(i.nome)
            listaAux.append(l)
        '''
        listaAux = list(listaAux)
        return listaAux

    def checkPosibility(self,lista):
        for i in lista:
            for j in self.listaPersonagem:
                if(i==j.nome):
                    if(j.vida<=0):
                        return False
        return True
    
    def selectOnePosibility(self,lista):
        for i in lista:
            for j in self.listaPersonagem:
                if(i==j.nome):
                    j.usar()
                    #print("%s : %d vidas"%(j.nome, j.vida))
    def faz31etapas(self):
        l=self.generateCombination()
        possibleFinal=[]
        for i in range(0,31):
            notDone = True
            while(notDone):
                selected=l[random.randint(0,len(l)-1)]
                
                if(self.checkPosibility(selected)):
                    self.selectOnePosibility(selected)
                    possibleFinal.append(selected)
                    notDone=False
                All0=True
                for i in self.listaPersonagem:
                    if(i.vida!=0):
                        All0=False
                if All0==True:
                    return -1
        for i in self.listaPersonagem:
            for j in range(0,i.vida):
                for k in possibleFinal:
                    if(i.nome not in k):
                        k.append(i.nome)
                        i.usar()
                        break
            '''while(i.vida>0):
                random.shuffle(possibleFinal)
                #print(possibleFinal)
                while(i.nome in possibleFinal[0]):
                    random.shuffle(possibleFinal)
                i.usar()
                possibleFinal[0].append(i.nome)'''
        
        return possibleFinal
def FindOne():
    for i in c.listaPersonagem:
        i.reset()
    possible=c.faz31etapas()
    while (possible==-1):
        for i in c.listaPersonagem:
            i.reset()
        possible=c.faz31etapas()
    return possible
def calcAgilityAndSort(lista):
    lAgi=[]
    for i in lista:
        SumAgilidade=0
        for j in i:
            SumAgilidade+=Dagilidade[j]
        lAgi.append([i,SumAgilidade])
    lAgi=sorted(lAgi, key=itemgetter(1))
    return lAgi
def calcDifficulty(lAgi,dictEtapas):
    lEtapas=list(dictEtapas.items())
    Difficulty=0
    for i in range(0,31):
        Difficulty+=lEtapas[i][1]/lAgi[i][1]
    return Difficulty
                        
            

#Testando
lPersonagem=[]
Dagilidade=test.get_agility()
for i in Dagilidade:
    pers=Personagem(Dagilidade[i],i)
    lPersonagem.append(pers)
c = Combination(lPersonagem)

dictt=test.difficultySum
sum=0
for i in dictt.values():
    sum+=i
contador=0
bestList = FindOne()
best=calcDifficulty(calcAgilityAndSort(FindOne()),dictt)
bestFind = bestList
while(contador<50):
    find = FindOne()
    new=calcDifficulty(calcAgilityAndSort(find),dictt)
    print(new)
    if (new<best):
        contador=0
        best=new
        bestList = calcAgilityAndSort(find)
        bestFind = find
    else:
        contador+=1  


print(len(bestFind))
f=open("bestCombination.txt","w")
f.write(str(bestList))
print(f"O melhor foi {best} com {bestList}\n\n{bestFind}")
f.close()
