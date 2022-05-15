import pygame
from sprites.tile import Tile


class Level:
    """Class which handles the creation of and changes to the minefield

    Attributes:
        level_map: 2D array that shows the placement of mines and digits
        cell_size: the size of a single tile on the grid
        tiles: a pygame sprite group containing all Tile-objects
        tiles_grid: all Tile-objects in a grid for handling of certain operations
        all_sprites: a pygame sprite group containing all sprites to be rendered
        chord_queue: stores all chording operations that will be executed on the next frame
    """

    def __init__(self, level_map, cell_size):
        """Constructor that creates the level

        Args:
            level_map: 2D array that shows the placement of mines and digits
            cell_size: the size of a single tile on the grid
        """
        self.level_map = level_map
        self.cell_size = cell_size

        self.tiles = pygame.sprite.Group()
        self.tiles_grid = []
        self.all_sprites = pygame.sprite.Group()
        self.chord_queue = []

        self._create_level()

    def update(self):
        """Handles all necessary updates on the game screen
        """
        self.tiles.update()
        self._clear_chord_queue()

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
        """Adds all tiles around a specific tile to a queue from which they will be opened

        Args:
            tile: the tile which is used as the origin point of this action
        """
        tile_y = int(tile.rect.y / self.cell_size)
        tile_x = int(tile.rect.x / self.cell_size)

        for y in range(tile_y-1, tile_y+2):
            for x in range(tile_x-1, tile_x+2):
                if 0 <= y < len(self.tiles_grid) and 0 <= x < len(self.tiles_grid[0]):
                    self.chord_queue.append(self.tiles_grid[y][x])

    def _clear_chord_queue(self):
        """Triggers all tiles in the chord queue and then clears the queue
        """
        for tile in self.chord_queue:
            self.trigger(tile)
        self.chord_queue = []

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
                self._open_all_mines()
                return "loss"
            if tile.digit > -1 and not tile.opened:
                complete = False
        if complete:
            return "win"
        return "incomplete"

    def _open_all_mines(self):
        """Opens all tiles containing mines
        """
        for tile in self.tiles:
            if tile.digit == -1:
                tile.open()

    def _create_level(self):
        """Creates all the sprites that the level consists of, according to the given level map
        """
        width = len(self.level_map[0])
        height = len(self.level_map)

        for y in range(height):
            tiles_grid_row = []
            for x in range(width):
                digit = self.level_map[y][x]
                norm_x = x * self.cell_size
                norm_y = y * self.cell_size

                tile = Tile(norm_x, norm_y, digit)
                self.tiles.add(tile)
                tiles_grid_row.append(tile)
            self.tiles_grid.append(tiles_grid_row)

        self.all_sprites.add(self.tiles)
