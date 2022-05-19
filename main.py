from turtle import width
import pygame
from gameMap import GameMap
from screenBoard import ScreenBoard
from run_better_route import  Etapa, Node, aEstrela, Personagem
from time import sleep
from random import randint
health=pygame.image.load("assets/begin_fill_health_bar.png")
       
def main():
  Width=300
  Heigth=82
  running=True
  pygame.init()
  pygame.font.init()
  mapaconfig=GameMap('mapa.txt',82,300)
  screenSettings=ScreenBoard(1200,82*4+150,3,1)
  custoParcial = 0
  screenSettings.draw_map(mapaconfig)
  Dagilidade=mapaconfig.get_agility()
  lPersonagem=[]
  for i in Dagilidade:
    pers=Personagem(Dagilidade[i],i)
    lPersonagem.append(pers)
  for i in range(0,len(lPersonagem)):
    screenSettings.draw_character_HUD(40+166*i,82*4+33,lPersonagem[i],mapaconfig)
    screenSettings.draw_health_bar(40+166*i, 82*4+103)
  finalPath = list()
  '''for index, etapas in enumerate(mapaconfig.etapas[:-1]):
    coordInicial=mapaconfig.findGoal(etapas)
    coordetapa1=mapaconfig.findGoal(mapaconfig.etapas[index+1])
    etapa1=Etapa(coordetapa1[0],coordetapa1[1],[lPersonagem[1]])
    noInicial=Node(mapaconfig,etapa1,coordInicial[0],coordInicial[1],0)
    screenSettings.writeCost(f"Custo Parcial = {custoParcial}",900 ,0,(0,0,0))
    screenSettings.writeCost(f"Dude = {lPersonagem[1].nome}",900 ,50,(0,0,0))
    screenSettings.writeCost(f"Vida = {lPersonagem[1].vida}",900 ,100,(0,0,0))
    listPath = aEstrela(mapaconfig,etapa1,noInicial,screenSettings)
    custoParcial += listPath[-1].g
    dificuldade=(index+1)*10+listPath[-1].g
    tempo=dificuldade/etapa1.somaAgilidade
    finalPath.extend(listPath)
    sleep(0.5)'''
  #screenSettings.draw_map(mapaconfig)
  screenSettings.writeCost(f"Custo Final = {custoParcial}",900 ,0,(0,0,0))
  for no in finalPath:
    screenSettings.draw_path(no.x,no.y,mapaconfig,(255,0,0))
    sleep(0.02)
  while running:
      for event in pygame.event.get():
          if event.type==pygame.QUIT:
              running=False
  pygame.quit()
main()