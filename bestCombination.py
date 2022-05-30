from itertools import combinations
from math import comb
from random import random, shuffle
from gameMap import GameMap
from run_better_route import Personagem
import random
from random import randint
from operator import itemgetter
import pickle


print()


def bestCombination():
    try:
        with open('bestCombination', 'rb') as fp:
            bestComb = pickle.load(fp)
        return bestComb
    # Caso o arquivo não exista ainda
    except:
        return None


def gerarInfoPersongem():
    # Apenas para obter as informações dos personagens
    test = GameMap('mapa.txt', 1, 1)
    lPersonagem = []
    Dagilidade = test.get_agility()
    for i in Dagilidade:
        pers = Personagem(Dagilidade[i], i)
        lPersonagem.append(pers)
    return (lPersonagem, Dagilidade)

def calcDifficulty(lAgi, dictEtapas):
    lEtapas = list(dictEtapas.items())
    listDifficulty = list()
    Difficulty = 0
    for i in range(0, 31):
        listDifficulty.append(lEtapas[i][1]/lAgi[i][1])
        Difficulty += lEtapas[i][1]/lAgi[i][1]
    return (Difficulty, listDifficulty)


class Combination:
    def __init__(self,dictt):
        self.lPersonagem = gerarInfoPersongem()[0]
        self.Dagilidade = gerarInfoPersongem()[1]
        self.bestCombination = bestCombination() # Melhor combinção de personagem até agora
        self.bestList = None    #melhor lista de custo por etapa 
        self.dictCustoCaminho = dictt 
        return

    def getBestCombination(self):
        return self.bestCombination

    def generateCombination(self):
        listaAux = [[], [], [], [], [], [], []]
        listaP = self.lPersonagem
        for i in listaP:
            listaAux[0].append([i.nome])
        comb_2 = combinations(listaP, 2)
        for p in comb_2:
            l = []
            for i in p:
                l.append(i.nome)
            listaAux[1].append(l)
        comb_3 = combinations(listaP, 3)
        for p in comb_3:
            l = []
            for i in p:
                l.append(i.nome)
            listaAux[2].append(l)

        comb_4 = combinations(listaP, 4)
        for p in comb_4:
            l = []
            for i in p:
                l.append(i.nome)
            listaAux[3].append(l)
        comb_5 = combinations(listaP, 5)
        for p in comb_5:
            l = []
            for i in p:
                l.append(i.nome)
            listaAux[4].append(l)
        comb_6 = combinations(listaP, 6)
        for p in comb_6:
            l = []
            for i in p:
                l.append(i.nome)
            listaAux[5].append(l)
        comb_7 = combinations(listaP, 7)
        for p in comb_7:
            l = []
            for i in p:
                l.append(i.nome)
            listaAux[6].append(l)

        listaAux = list(listaAux)
        return listaAux

    def checkPosibility(self, lista):
        for i in lista:
            for j in self.lPersonagem:
                if(i == j.nome):
                    if(j.vida == 0):
                        return False
        return True

    def selectOnePosibility(self, lista):
        for i in lista:
            for j in self.lPersonagem:
                if(i == j.nome):
                    j.usar()
                    #print("%s : %d vidas"%(j.nome, j.vida))

    def faz31etapas(self):
        a1 = a2 = a3 = a4 = a5 = a6 = a7 = 0
        while(a1+2*a2+3*a3+4*a4+5*a5+6*a6+7*a7 != 56 or (a1+a2+a3+a4+a5+a6+a7) != 31):
            a1 = randint(0, 10)
            a2 = randint(0, 26)
            a3 = randint(0, 18)
            a4 = randint(0, 2)
            a5 = randint(0, 0)
            a6 = randint(0, 0)
            a7 = randint(0, 0)
        l = self.generateCombination()
        possibleFinal = []
        for i in range(a7):
            selected = l[6][0]
            self.selectOnePosibility(selected)
            possibleFinal.append(selected)
        for i in range(a6):
            notDone = True
            while(notDone):
                selected = l[5][random.randint(0, len(l[5])-1)]
                if(self.checkPosibility(selected)):
                    self.selectOnePosibility(selected)
                    possibleFinal.append(selected)
                    notDone = False
        for i in range(a5):
            notDone = True
            while(notDone):
                selected = l[4][random.randint(0, len(l[4])-1)]
                if(self.checkPosibility(selected)):
                    self.selectOnePosibility(selected)
                    possibleFinal.append(selected)
                    notDone = False
        for i in range(a4):
            notDone = True
            while(notDone):
                selected = l[3][random.randint(0, len(l[3])-1)]
                if(self.checkPosibility(selected)):
                    self.selectOnePosibility(selected)
                    possibleFinal.append(selected)
                    notDone = False
        for i in range(a3):
            notDone = True
            while(notDone):
                selected = l[2][random.randint(0, len(l[2])-1)]
                if(self.checkPosibility(selected)):

                    self.selectOnePosibility(selected)
                    possibleFinal.append(selected)
                    notDone = False
        for i in range(a2):
            notDone = True
            while(notDone):
                selected = l[1][random.randint(0, len(l[1])-1)]
                if(self.checkPosibility(selected)):

                    self.selectOnePosibility(selected)
                    possibleFinal.append(selected)
                    notDone = False
        for i in range(a1):
            notDone = True
            while(notDone):
                selected = l[0][random.randint(0, len(l[0])-1)]
                if(self.checkPosibility(selected)):

                    self.selectOnePosibility(selected)
                    possibleFinal.append(selected)
                    notDone = False
        return possibleFinal

    def FindOne(self):
        for i in self.lPersonagem:
            i.reset()
        possible = self.faz31etapas()
        contador = 0
        while (possible == -1 and contador < 1000000):
            for i in self.lPersonagem:
                i.vida = 8
            possible = self.faz31etapas()
            contador += 1
        return possible

    def calcAgilityAndSort(self):
        Dagilidade = self.Dagilidade
        lista = self.FindOne()
        lAgi = []
        for i in lista:
            SumAgilidade = 0
            for j in i:
                SumAgilidade += Dagilidade[j]
            lAgi.append([i, SumAgilidade])
        lAgi = sorted(lAgi, key=itemgetter(1))
        return lAgi

    def calcBestCombination(self):
        dictt = self.dictCustoCaminho
        sum = 0
        for i in dictt.values():
            sum += i
        contador = 0
        if self.bestCombination: #Se não existir vai ser None, assim irá direto ao None
            (best,self.bestList) = calcDifficulty(self.bestCombination,dictt)
        else:
            best = 100000000000
        while(contador < 1000):
            lista = self.calcAgilityAndSort()
            (new, newList) = calcDifficulty(lista, dictt)
            if (new < best):
                contador = 0
                best = new
                self.bestList = newList
                self.bestCombination = lista
                with open('bestCombination', 'wb') as fp:
                    pickle.dump(self.bestCombination, fp)
            else:
                contador += 1
        print(f"{best}\n{self.bestCombination}")

        return 
