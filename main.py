import pygame
from gameMap import GameMap
from screenBoard import ScreenBoard
from run_better_route import  Etapa, Node, aEstrela
from time import sleep
from random import randint
       
def main():
  running=True
  pygame.init()
  pygame.font.init()
  mapaconfig=GameMap('mapa.txt',82,300)
  screenSettings=ScreenBoard(1800,492,5,1)
  custoParcial = 0
  screenSettings.draw_map(mapaconfig)
  
  finalPath = list()
  for index, etapas in enumerate(mapaconfig.etapas[:-1]):
    coordInicial=mapaconfig.findGoal(etapas)
    coordetapa1=mapaconfig.findGoal(mapaconfig.etapas[index+1])
    etapa1=Etapa(coordetapa1[0],coordetapa1[1],[])
    noInicial=Node(mapaconfig,etapa1,coordInicial[0],coordInicial[1],0)
    screenSettings.writeCost(f"Custo Parcial = {custoParcial}",1500 ,0,(0,0,0))
    listPath = aEstrela(mapaconfig,etapa1,noInicial,screenSettings)
    custoParcial += listPath[-1].g
    finalPath.extend(listPath)
    sleep(0.5)
  screenSettings.draw_map(mapaconfig)
  screenSettings.writeCost(f"Custo Final = {custoParcial}",1500 ,0,(0,0,0))
  for no in finalPath:
    screenSettings.draw_path(no.x,no.y,mapaconfig,(255,0,0))
    sleep(0.1)
  while running:
      for event in pygame.event.get():
          if event.type==pygame.QUIT:
              running=False
  pygame.quit()
main()