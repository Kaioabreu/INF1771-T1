from time import sleep
from screenBoard import *

class Etapa:
    
  def __init__(self, x, y, lPersonagens):
    self.GoalX= x
    self.GoalY= y
    self.lPersonagens= lPersonagens
      
  def manhattan(self,x,y):
    return abs(self.GoalX - x)+abs(self.GoalY - y)

def IsValid(x,y):
  return(x>=0 and x<=300 and y>=0 and y<=82)  

class Node:
  def __init__(self,GameMap,etapa,x,y,g):
    self.x=x
    self.y=y
    self.h=etapa.manhattan(x,y)
    self.g = g #mudar
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
    return reversed(pathList)


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
                   ScreenBoard.draw_path(nextNode.x,nextNode.y,GameMap,(154,205,50))
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
    print("Caminho não encontrado")
    return None



    
    
        
     





    


