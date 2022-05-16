import pygame
import matrix_methods
from run_better_route import GameMap, Etapa, Node, ScreenBoard, aEstrela

dictdifficulty=matrix_methods.get_tile_difficulty()
       
def main():
  running=True
  pygame.init()
  mapaconfig=GameMap(82,300,matrix_methods.get_matriz())
  screenSettings=ScreenBoard(1800,492,5,1)
  screenSettings.draw_map(mapaconfig)
  coordInicial=mapaconfig.findGoal("1")
  coordetapa1=mapaconfig.findGoal("2")
  print(coordetapa1)
  etapa1=Etapa(coordetapa1[0],coordetapa1[1],[])
  noInicial=Node(mapaconfig,etapa1,coordInicial[0],coordInicial[1],0)
  aEstrela(mapaconfig,etapa1,noInicial,screenSettings)
  while running:
      for event in pygame.event.get():
          if event.type==pygame.QUIT:
              running=False
  pygame.quit()
main()