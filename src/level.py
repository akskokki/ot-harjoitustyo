import pygame
from sprites.tile import Tile


class Level:
    def __init__(self, level_map, cell_size):
        self.level_map = level_map
        self.cell_size = cell_size

        self.tiles = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self._create_level()

    def update(self):
        self.tiles.update()

    def click(self, pos, button):
        for tile in self.tiles:
            if tile.rect.collidepoint(pos):
                if button == "left":
                    tile.open()
                elif button == "right":
                    tile.flag()

    def _create_level(self):
        width = len(self.level_map[0])
        height = len(self.level_map)

        for y in range(height):
            for x in range(width):
                cell = self.level_map[y][x]
                norm_x = x * self.cell_size
                norm_y = y * self.cell_size
                self.tiles.add(Tile(norm_x, norm_y, cell))

        self.all_sprites.add(self.tiles)
