import pygame
from sprites.tile import Tile


class Level:
    def __init__(self, level_map, cell_size):
        """Constructor that creates the level

        Args:
            level_map: 2D array that shows the placement of mines and digits
            cell_size: the size of a single tile on the grid
        """
        self.level_map = level_map
        self.cell_size = cell_size

        self.tiles = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self._create_level()

    def update(self):
        """Handles all necessary updates on the game screen
        """
        self.tiles.update()

    def click(self, pos, button):
        """Performs a click-action on the specified position on the screen

        Args:
            pos: pair of coordinates that represents a position on the screen
            button: string representation of which button was pressed (left/right)
        """
        for tile in self.tiles:
            if tile.rect.collidepoint(pos):
                if button == "left":
                    self.trigger(tile)
                elif button == "right":
                    tile.flag()

    def trigger(self, tile):
        """Triggers the functionality of a tile.
        If the tile is empty, this simply opens it. If it contains a mine, the mine explodes.

        Args:
            tile: the specific tile that will be triggered
        """
        if tile.open() and tile.digit == 0:
            self.chord(tile)
        if tile.digit == -1:
            tile.explode()

    def chord(self, tile):
        """Opens all tiles around a specified tile

        Args:
            tile: the tile which is used as the origin point of this action
        """
        tile_y = tile.rect.y
        tile_x = tile.rect.x
        for y in range(tile_y-self.cell_size, tile_y+self.cell_size+1, self.cell_size):
            for x in range(tile_x-self.cell_size, tile_x+self.cell_size+1, self.cell_size):
                self.click((x, y), "left")

    def check_completion(self):
        """Checks whether the game has been completed, in one way or another

        Returns:
            "win": all empty tiles have been opened without exploding any mines
            "loss": a mine has exploded
            "incomplete": the game has been interrupted in an unfinished state
        """
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
        """Creates all the sprites that the level consists of, according to the given level map
        """
        width = len(self.level_map[0])
        height = len(self.level_map)

        for y in range(height):
            for x in range(width):
                digit = self.level_map[y][x]
                norm_x = x * self.cell_size
                norm_y = y * self.cell_size
                self.tiles.add(Tile(norm_x, norm_y, digit))

        self.all_sprites.add(self.tiles)
