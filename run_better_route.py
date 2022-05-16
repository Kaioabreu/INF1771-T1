import matrix_methods
dictdifficulty=matrix_methods.get_tile_difficulty()
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
    return self.map[y][x]
    
class Etapa:
    
  def __init__(self, x, y, lPersonagens):
    self.GoalX= x
    self.GoalY= y
    self.lPersonagens: [lPersonagens]
      
  def manhattan(self,x,y):
    return abs(self.GoalX - x)+abs(self.GoalY - y)
    
class Node:
  def __init__(self,GameMap,etapa,x,y,g):
    self.x=x
    self.y=y
    self.h=etapa.manhattan(x,y)
    self.g = g #mudar
    self.f = self.g + self.h
    
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

#main



    
    
        
     





    


