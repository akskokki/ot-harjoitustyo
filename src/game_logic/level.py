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
                    self.trigger(tile)
                elif button == "right":
                    tile.flag()

    def trigger(self, tile):
        if tile.open() and tile.digit == 0:
            self.chord(tile)
        if tile.digit == -1:
            tile.explode()

    def chord(self, tile):
        tile_y = tile.rect.y
        tile_x = tile.rect.x
        for y in range(tile_y-self.cell_size, tile_y+self.cell_size+1, self.cell_size):
            for x in range(tile_x-self.cell_size, tile_x+self.cell_size+1, self.cell_size):
                self.click((x, y), "left")

    def check_completion(self):
        complete = True
        for tile in self.tiles:
            if tile.exploded:
                return "loss"
            if tile.digit > -1 and not tile.opened:
                complete = False
        if complete:
            return "win"
        return "incomplete"

    def _create_level(self):
        width = len(self.level_map[0])
        height = len(self.level_map)

        for y in range(height):
            for x in range(width):
                digit = self.level_map[y][x]
                norm_x = x * self.cell_size
                norm_y = y * self.cell_size
                self.tiles.add(Tile(norm_x, norm_y, digit))

        self.all_sprites.add(self.tiles)
