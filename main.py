import pygame
import matrix_methods
from run_better_route import GameMap, Etapa, Node, ScreenBoard, aEstrela
from time import sleep
dictdifficulty=matrix_methods.get_tile_difficulty()
       
def main():
  running=True
  pygame.init()
  mapaconfig=GameMap(82,300,matrix_methods.get_matriz())
  screenSettings=ScreenBoard(1800,492,5,1)
  screenSettings.draw_map(mapaconfig)
  finalPath = list()
  for index, etapas in enumerate(mapaconfig.etapas[:-1]):
    coordInicial=mapaconfig.findGoal(etapas)
    coordetapa1=mapaconfig.findGoal(mapaconfig.etapas[index+1])
    etapa1=Etapa(coordetapa1[0],coordetapa1[1],[])
    noInicial=Node(mapaconfig,etapa1,coordInicial[0],coordInicial[1],0)
    finalPath.extend(aEstrela(mapaconfig,etapa1,noInicial,screenSettings))
  sleep(1)
  screenSettings.draw_map(mapaconfig)
  for no in finalPath:
    screenSettings.draw_path(no.x,no.y,mapaconfig,(255,0,0))
  while running:
      for event in pygame.event.get():
          if event.type==pygame.QUIT:
              running=False
  pygame.quit()
main()