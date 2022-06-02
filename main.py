import pygame
from bestCombination import Combination, bestCombination
from gameMap import GameMap
from screenBoard import ScreenBoard
from run_better_route import  Etapa, Node, aEstrela, Personagem
from time import sleep
from random import randint
import pickle

def main():
  GameInterfaceVariables= {'Witdh':300,'Height':82,'HUDSize':150,'Margin':1,'TileSize':3,'HUDMarginX':40,'CharHUDX':166}
  Width=300
  Heigth=82
  running=True
  pygame.init()
  pygame.font.init()
  mapaconfig=GameMap('mapa.txt',Heigth,Width)
  TileMargin=GameInterfaceVariables['TileSize']+GameInterfaceVariables['Margin']
  screenSettings=ScreenBoard(Width*TileMargin,Heigth*TileMargin+GameInterfaceVariables['HUDSize'],GameInterfaceVariables['TileSize'],GameInterfaceVariables['Margin'])
  custoParcial = 0
  screenSettings.draw_map(mapaconfig)
  screenSettings.draw_moldure()
  Dagilidade=mapaconfig.get_agility()
  lPersonagem=[]
  for i in Dagilidade:
    pers=Personagem(Dagilidade[i],i)
    lPersonagem.append(pers)
  for i in range(0,len(lPersonagem)):
    screenSettings.draw_character_HUD(GameInterfaceVariables['HUDMarginX']+GameInterfaceVariables['CharHUDX']*i,Heigth*TileMargin+33,lPersonagem[i],mapaconfig)
  #Para pegar o ponto inicial e adicionar no finalPath
  coordInicial=mapaconfig.findGoal('0')
  coordetapa1=mapaconfig.findGoal(mapaconfig.etapas[1])
  etapa1=Etapa(coordetapa1[0],coordetapa1[1])
  noInicial=Node(mapaconfig,etapa1,coordInicial[0],coordInicial[1],0)
  finalPath = list()
  finalPath.append(noInicial)
  listaCustoParcial = list() #lista dos custos do caminho (a*) por etapas
  for index, etapa in enumerate(mapaconfig.etapas[:-1]):
    coordInicial=mapaconfig.findGoal(etapa)
    coordetapa1=mapaconfig.findGoal(mapaconfig.etapas[index+1])
    etapa1=Etapa(coordetapa1[0],coordetapa1[1])
    noInicial=Node(mapaconfig,etapa1,coordInicial[0],coordInicial[1],0)
    listPath = aEstrela(mapaconfig,etapa1,noInicial,screenSettings)
    mapaconfig.setDifficultySum(index+1, listPath[-1].g)
    custoParcial += listPath[-1].g
    listaCustoParcial.append(listPath[-1].g)
    finalPath.extend(listPath)
  screenSettings.writeCost(f"Custo do A*{custoParcial}",900,40,(255,255,255) )
  screenSettings.writeCost(f"O melhor caminho foi achado",900 ,0,(255,255,255))
  screenSettings.writeCost("Achando a melhor combinação",900 ,20,(255,255,255))
  mapaconfig.sortDictDifficulty()
  #Encontrando a melhor combinação de personagens
  c = Combination(mapaconfig.difficulty)
  c.calcBestCombination()
  bestCombination = c.bestCombination
  #Redesenhando o mapa e pintando o caminho
  screenSettings.draw_map(mapaconfig)
  screenSettings.draw_moldure()
  etapa=0
  custoTotal = 0
  #precisa disso para redesenhar os personagem? 
  for i in range(0,len(lPersonagem)):
    screenSettings.draw_character_HUD(GameInterfaceVariables['HUDMarginX']+GameInterfaceVariables['CharHUDX']*i,Heigth*TileMargin+33,lPersonagem[i],mapaconfig)
  #sleep(0.5)
  for no in finalPath:

    if (mapaconfig.getTileType(no.x,no.y) == mapaconfig.etapas[etapa] and etapa <= 30):
      custoTotal += listaCustoParcial[etapa] + c.bestList[etapa]
      screenSettings.writeCost(f"Custo Final = {round(custoTotal,2)}",900 ,0,(255,255,255))
      screenSettings.writeCost(f"Custo da Etapa = {round(listaCustoParcial[etapa] + c.bestList[etapa],2)}",900 ,20,(0,255,255))
      screenSettings.draw_moldure()
      for i in bestCombination[etapa][0]:
        screenSettings.draw_selected_character(i)
        for j in lPersonagem:
          if(i==j.nome):
            j.usar()
      etapa+=1
      for i in range(0,len(lPersonagem)):
        screenSettings.draw_character_HUD(GameInterfaceVariables['HUDMarginX']+GameInterfaceVariables['CharHUDX']*i,Heigth*TileMargin+33,lPersonagem[i],mapaconfig)
      sleep(1)
    screenSettings.draw_path(no.x,no.y,mapaconfig,(255,0,0))
    sleep(0.03)
   

  while running:
      for event in pygame.event.get():
          if event.type==pygame.QUIT:
              running=False
  pygame.quit()

main()