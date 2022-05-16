import pygame
from time import sleep
import matrix_methods
dictdifficulty=matrix_methods.get_tile_difficulty()
cores={
  'R':(128,128,128),#cinza
  'A':(0, 150, 255),#azul
  'M':(139,69,19),# marrom 
  'V':(0,51,0),#verde
  'F':(34, 139, 34),#emerald green
  '.':(218,200,179)#bege
}

class ScreenBoard:
    
  def __init__(self, width, height, tile_size, margin):
      self.width=width
      self.height=height
      self.tile_size=tile_size
      self.margin=margin
      self.screen=pygame.display.set_mode((width, height))
      
  def draw_tile(self, x, y, MapSettings):
      element=MapSettings.map[y][x]
      cor=cores.get(element,(153,0,153))
      pygame.draw.rect(self.screen,cor,[(self.margin+self.tile_size)*x+self.tile_size,(self.margin+self.tile_size)*y+self.margin,self.tile_size,self.tile_size])

  def draw_path(self, x,y, MapSettings,cor):
      pygame.draw.rect(self.screen,cor,[(self.margin+self.tile_size)*x+self.tile_size,(self.margin+self.tile_size)*y+self.margin,self.tile_size,self.tile_size])
      pygame.display.flip()
  def draw_map(self, MapSettings):
      self.screen.fill((0,0,0))
      for i in range(MapSettings.rows):
          for j in range(MapSettings.columns):
              self.draw_tile(j, i, MapSettings)
      pygame.display.flip()
class GameMap:
  etapas=["1","2","3","4","5","6","7","8","9","B","C","D","E","G","H","I","J","K","L","N","O","P","Q","S","T","U","V","W","X","Y","Z"]
    
  def __init__(self,rows,columns,mapa):
    self.rows=rows
    self.columns=columns
    self.map=mapa
      
  def findGoal(self, goal):
    for y,row in enumerate(self.map):
      for x,item in enumerate(row):
        if(goal==item):
          return [x,y]
    return -1
  def getTileType(self, x,y):
    if(self.map[y][x] in ".ARVM"):
        return self.map[y][x]
    else :
        return 'Etapa'
    
class Etapa:
    
  def __init__(self, x, y, lPersonagens):
    self.GoalX= x
    self.GoalY= y
    self.lPersonagens= lPersonagens
      
  def manhattan(self,x,y):
    return abs(self.GoalX - x)+abs(self.GoalY - y)
    
class Node:
  def __init__(self,GameMap,etapa,x,y,g):
    self.x=x
    self.y=y
    self.h=etapa.manhattan(x,y)
    self.g = g #mudar
    self.f = self.g + self.h
    self.partner=None
    
def IsValid(x,y):
  return(x>=0 and x<=300 and y>=0 and y<=82)
        
def getVizinhos(node,GameMap,etapa):
  x=node.x
  y=node.y
  vizinhos=[]
  if (IsValid(x-1,y)): 
    vizinhos.append(Node(GameMap,etapa,x-1,y,node.g+dictdifficulty[GameMap.getTileType(x-1,y)]))
  if (IsValid(x+1,y)):
    vizinhos.append(Node(GameMap,etapa,x+1,y,node.g+dictdifficulty[GameMap.getTileType(x+1,y)]))
  if (IsValid(x,y-1)):
    vizinhos.append(Node(GameMap,etapa,x,y-1,node.g+dictdifficulty[GameMap.getTileType(x,y-1)]))
  if (IsValid(x,y+1)):
    vizinhos.append(Node(GameMap,etapa,x,y+1,node.g+dictdifficulty[GameMap.getTileType(x,y+1)]))
  return vizinhos

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
            temp=current
            while(temp.partner!=None):
                ScreenBoard.draw_path(temp.x,temp.y,GameMap,(255,0,0))#CONSTRUIR LISTA PARA PEGAR INVERSO
                temp=temp.partner
            return current
        aberta.remove(current)
        fechada.append(current)
        vizinhos=getVizinhos(current, GameMap, etapa)
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



    
    
        
     





    


