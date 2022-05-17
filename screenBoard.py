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

    def __init__(self, width, height, tile_size, margin):
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.margin = margin
        self.screen = pygame.display.set_mode((width, height))

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
    def writeCost(self,custo,x,y, cor):
        gameFont = pygame.font.SysFont('Comic Sans MS', 24)
        texto = gameFont.render(custo, False,cor)
        self.screen.blit(texto, (x,y))
        pygame.display.flip()
        return 

