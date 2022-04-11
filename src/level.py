from sprites.tile import Tile
import pygame

class Level:
    def __init__(self, level_map):
        self.level_map = level_map

        self.tiles = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self._create_level()
    
    def update(self):
        self.tiles.update()
    
    def click(self, pos):
        buttons = pygame.mouse.get_pressed()
        for tile in self.tiles:
            if tile.rect.collidepoint(pos):
                if buttons[0] == True:
                    tile.open()
                elif buttons[2] == True:
                    tile.flag()

    def _create_level(self):
        width = len(self.level_map[0])
        height = len(self.level_map)

        for y in range(height):
            for x in range(width):
                cell = self.level_map[y][x]
                norm_x = x * 20
                norm_y = y * 20
                self.tiles.add(Tile(norm_x, norm_y, cell))
        
        self.all_sprites.add(self.tiles)