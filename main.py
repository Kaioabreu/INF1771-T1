import pygame
import matrix_methods
from run_better_route import GameMap, Etapa, Node

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
      
  def draw_tile(self, screen, x, y, MapSettings):
      element=MapSettings.map[y][x]
      cor=cores.get(element,(153,0,153))
      pygame.draw.rect(screen,cor,[(self.margin+self.tile_size)*x+self.tile_size,(self.margin+self.tile_size)*y+self.margin,self.tile_size,self.tile_size])
        
  def draw_map(self, screen, MapSettings):
      screen.fill((0,0,0))
      for i in range(MapSettings.rows):
          for j in range(MapSettings.columns):
              self.draw_tile(screen, j, i, MapSettings)
      pygame.display.flip()
       
def main():
  running=True
  pygame.init()
  mapaconfig=GameMap(82,300,matrix_methods.get_matriz())
  screenSettings=ScreenBoard(1800,492,5,1)
  screen=pygame.display.set_mode((screenSettings.width, screenSettings.height))
  screenSettings.draw_map(screen,mapaconfig)
  
  while running:
      for event in pygame.event.get():
          if event.type==pygame.QUIT:
              running=False
  pygame.quit()
main()