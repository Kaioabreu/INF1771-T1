from turtle import width
import pygame
from bestCombination import Combination, bestCombination
from gameMap import GameMap
from screenBoard import ScreenBoard
from run_better_route import  Etapa, Node, aEstrela, Personagem
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