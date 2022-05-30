from webbrowser import BackgroundBrowser
import pygame
cores = {
    'R': (128, 128, 128),  # cinza
    'A': (0, 150, 255),  # azul
    'M': (139, 69, 19),  # marrom
    'V': (0, 51, 0),  # verde
    'F': (34, 139, 34),  # emerald green
    '.': (218, 200, 179)  # bege
}


class ScreenBoard:
    healthBarSprints=(pygame.image.load("assets/begin_fill_health_bar.png"),pygame.image.load("assets/fill_health_bar.png"),pygame.image.load("assets/end_fill_health_bar.png"),pygame.image.load("assets/begin_empty_health_bar.png"),pygame.image.load("assets/empty_health_bar.png"),pygame.image.load("assets/end_empty_health_bar.png"))
    HudMoldure=(pygame.image.load("assets/HUDMOLDURE.png"))
    selectedMoldure=pygame.image.load("assets/selectChar.png")

    def __init__(self, width, height, tile_size, margin):
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.margin = margin
        self.screen = pygame.display.set_mode((width, height))
        self.gameFont22 = pygame.font.Font("assets/alterebro-pixel-font.ttf", 32)
    def draw_moldure(self):
        self.screen.blit(self.HudMoldure,(0,(self.tile_size+self.margin)*82))
        pygame.display.flip()
    def draw_tile(self, x, y, MapSettings):
        element = MapSettings.map[y][x]
        cor = cores.get(element, (153, 0, 153))
        pygame.draw.rect(self.screen, cor, [(self.margin+self.tile_size)*x+self.tile_size,
                         (self.margin+self.tile_size)*y+self.margin, self.tile_size, self.tile_size])

    def draw_path(self, x, y, MapSettings, cor):
        pygame.draw.rect(self.screen, cor, [(self.margin+self.tile_size)*x+self.tile_size,
                         (self.margin+self.tile_size)*y+self.margin, self.tile_size, self.tile_size])
        pygame.display.flip()

    def draw_map(self, MapSettings):
        self.screen.fill((0, 0, 0))
        for i in range(MapSettings.rows):
            for j in range(MapSettings.columns):
                self.draw_tile(j, i, MapSettings)
        pygame.display.flip()

    def draw_health_bar(self, x, y, health=8):       
        self.screen.blit(pygame.transform.scale(self.healthBarSprints[3],(14,18)),(x,y))
        for i in range(1,7):
            self.screen.blit(pygame.transform.scale(self.healthBarSprints[4],(18,18)),(x+14+16*(i-1),y))
        self.screen.blit(pygame.transform.scale(self.healthBarSprints[5],(14,18)),(x+14+16*6+2,y))
        if(health!=0):
            self.screen.blit(pygame.transform.scale(self.healthBarSprints[0],(14,18)),(x,y))
        for i in range(1,health):
            if(i!=7):
                self.screen.blit(pygame.transform.scale(self.healthBarSprints[1],(18,18)),(x+14+16*(i-1),y))
        if(health==8):
            self.screen.blit(pygame.transform.scale(self.healthBarSprints[2],(14,18)),(x+14+16*6+2,y))
        pygame.display.flip()
    
    def draw_character_HUD(self, x, y, personagem,MapSettings):
       self.screen.blit(pygame.transform.scale(personagem.image,MapSettings.ImageSize[personagem.nome]),(x,y))
       name = self.gameFont22.render(personagem.nome, False, (0,0,0))
       agility = self.gameFont22.render(str(personagem.agilidade), False, (0,0,0))
       self.screen.blit(name, (x+MapSettings.ImageSize[personagem.nome][0]+10,y+5))
       self.screen.blit(agility, (x+MapSettings.ImageSize[personagem.nome][0]+10,y+35))
       self.draw_health_bar(x,y+70,personagem.vida)
       pygame.display.flip()
    
    def draw_selected_character(self, lPersonagens):
        daux={"Aang":0, "Zukko":1, "Toph":2, "Katara":3, "Sokka":4, "Appa":5, "Momo":6}
        for i in lPersonagens:
            self.screen.blit(self.selectedMoldure,(100+166*daux[i],500))
        pygame.display.flip()
            

    def writeCost(self,custo,x,y, cor):
        gameFont = pygame.font.SysFont('Comic Sans MS', 24)
        texto = gameFont.render(custo, False,cor,(0,0,0))
        self.screen.blit(texto, (x,y))
        pygame.display.flip()
        return 

