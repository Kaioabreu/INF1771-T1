from multiprocessing import set_forkserver_preload
from time import sleep
from screenBoard import *
from random import randint
class Personagem:
  def __init__(self,agilidade,nome):
    self.nome=nome
    self.vida=8
    self.agilidade=agilidade
    self.image = pygame.image.load("assets/"+str(nome)+".png")
  def usar(self):
    self.vida-=1
  def reset(self):
   self.vida=8

def somaAgili(etapa):
  soma = 0
  for i in etapa.lPersonagens:
    soma+= i.agilidade
  return soma
class Etapa:
    
  def __init__(self, x, y, lPersonagens):
    self.GoalX= x
    self.GoalY= y
    self.lPersonagens= lPersonagens
    self.somaAgilidade=somaAgili(self)
      
  def manhattan(self,x,y):
    return abs(self.GoalX - x)+abs(self.GoalY - y)

def IsValid(x,y):
  return(x>=0 and x<=299 and y>=0 and y<=81)  

class Node:
  def __init__(self,GameMap,etapa,x,y,g):
    self.x=x
    self.y=y
    self.h=etapa.manhattan(x,y)
    self.g = g
    self.f = self.g + self.h
    self.partner=None
  
  def getVizinhos(self, GameMap, etapa):
    x=self.x
    y=self.y
    vizinhos=[]
    if (IsValid(x-1,y)): 
      vizinhos.append(Node(GameMap,etapa,x-1,y,self.g+GameMap.get_tile_difficulty(GameMap.getTileType(x-1,y))))
    if (IsValid(x+1,y)):
      vizinhos.append(Node(GameMap,etapa,x+1,y,self.g+GameMap.get_tile_difficulty(GameMap.getTileType(x+1,y))))
    if (IsValid(x,y-1)):
      vizinhos.append(Node(GameMap,etapa,x,y-1,self.g+GameMap.get_tile_difficulty(GameMap.getTileType(x,y-1))))
    if (IsValid(x,y+1)):
      vizinhos.append(Node(GameMap,etapa,x,y+1,self.g+GameMap.get_tile_difficulty(GameMap.getTileType(x,y+1))))
    return vizinhos
  
  def getPath(self):
    temp=self
    pathList = list()
    while(temp.partner!=None):
      pathList.append(temp)
      temp=temp.partner
    return pathList[::-1]


def pegaMenor(lista):
    menor = lista[0]
    for i in lista[1:]:
        if menor.f > i.f:
            menor = i
    return menor

def aEstrela(GameMap,etapa, node, ScreenBoard):
    aberta=[]
    fechada=[]  
    aberta.append(node)
    current=node
    cor = (randint(0,255),randint(0,255),randint(0,255))
    while aberta:
        current = pegaMenor(aberta)
        #print(current.x,current.y)
        if (current.x == etapa.GoalX and current.y == etapa.GoalY):
            pathList = current.getPath()
            return pathList
        aberta.remove(current)
        fechada.append(current)
        vizinhos=current.getVizinhos(GameMap, etapa)
        for nextNode in vizinhos:
            inFechada=False
            inAberta=False
            for i in fechada:
                if(nextNode.x==i.x and nextNode.y==i.y):
                   ScreenBoard.draw_path(nextNode.x,nextNode.y,GameMap,cor)
                   inFechada=True
            if(not(inFechada)):   
                for i in aberta: 
                    if(nextNode.x==i.x and nextNode.y==i.y):
                        inAberta=True
                        if (nextNode.f<i.f):
                            i.f=nextNode.f
                            nextNode.partner=current
                if(inAberta==False):
                   aberta.append(nextNode)
                   nextNode.partner=current
    print("Caminho n??o encontrado")
    return None

def calculaTodasEtapas(mapaconfig, screenSettings ,lPersonagem):
  coordInicial=mapaconfig.findGoal('0')
  coordetapa1=mapaconfig.findGoal(mapaconfig.etapas[1])
  etapa1=Etapa(coordetapa1[0],coordetapa1[1],[lPersonagem[1]])
  noInicial=Node(mapaconfig,etapa1,coordInicial[0],coordInicial[1],0)
  finalPath = list()
  finalPath.append(noInicial)
  listaCustoParcial = list() #lista dos custos do caminho (a*) por etapas
  custoAstar = 0
  for index, etapa in enumerate(mapaconfig.etapas[:-1]):
    coordInicial=mapaconfig.findGoal(etapa)
    coordetapa1=mapaconfig.findGoal(mapaconfig.etapas[index+1])
    etapa1=Etapa(coordetapa1[0],coordetapa1[1],[lPersonagem[1]])
    noInicial=Node(mapaconfig,etapa1,coordInicial[0],coordInicial[1],0)
    listPath = aEstrela(mapaconfig,etapa1,noInicial,screenSettings)
    mapaconfig.setDifficultySum(index+1, listPath[-1].g)
    custoAstar += listPath[-1].g
    listaCustoParcial.append(listPath[-1].g)
    finalPath.extend(listPath)
  return (custoAstar, finalPath)
        
     





    


