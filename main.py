import pygame
from bestCombination import Combination, bestCombination
from gameMap import GameMap
from screenBoard import ScreenBoard
from run_better_route import  Etapa, Node, aEstrela, Personagem, calculaTodasEtapas
from time import sleep
from random import randint
import pickle

def main():
  running=True
  pygame.init()
  pygame.font.init()
  mapaconfig=GameMap('mapa.txt', 82, 300)
  screenSettings=ScreenBoard()
  
  Dagilidade=mapaconfig.get_agility()
  lPersonagem=[]
  for i in Dagilidade:
    pers=Personagem(Dagilidade[i],i)
    lPersonagem.append(pers)
  screenSettings.draw_game(mapaconfig,lPersonagem)
  #Para pegar o ponto inicial e adicionar no finalPath
  (custoAstar,finalPath) = calculaTodasEtapas(mapaconfig, screenSettings, lPersonagem)
  screenSettings.writeCost(f"Custo do A*{custoAstar}",900,40,(255,255,255) )
  screenSettings.writeCost(f"O melhor caminho foi achado",900 ,0,(255,255,255))
  screenSettings.writeCost("Achando a melhor combinação",900 ,20,(255,255,255))
  mapaconfig.sortDictDifficulty()
  #Encontrando a melhor combinação de personagens
  c = Combination(mapaconfig.difficulty)
  c.calcBestCombination()
  bestCombination = c.bestCombination
  #Redesenhando o mapa e pintando o caminho
  screenSettings.draw_game(mapaconfig,lPersonagem)
  #Desenhando o caminho final
  screenSettings.draw_finalPath(finalPath,bestCombination,lPersonagem,mapaconfig)
  while running:
      for event in pygame.event.get():
          if event.type==pygame.QUIT:
              running=False
  pygame.quit()

main()