import pygame
from utilities.load_image import load_image


class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, digit):
        """Constructor that creates the tile

        Args:
            x,y: the coordinates of the tile
            digit: the value of the tile; -1 is a mine, 0 is a blank and 1-8 is a numbered tile
        """
        super().__init__()
        self.digit = digit

        self.opened = False
        self.flagged = False
        self.exploded = False

        self._images = self._load_images()

        self.image = self._images["unopened"]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def open(self):
        """Opens the tile if it is in a state in which it can be opened
        """
        if not self.flagged and not self.opened:
            self.opened = True
            return True
        return False

    def flag(self):
        """Inverts the state of the tile's flag
        """
        if not self.opened:
            self.flagged = not self.flagged

    def explode(self):
        """Explodes the tile if it is not flagged
        """
        if not self.flagged:
            self.exploded = True

    def update(self):
        """Sets the tile's image to appropriately display its current state
        """
        if self.exploded:
            self.image = self._images["mine_clicked"]
        elif self.opened:
            self.image = self._images[str(self.digit)]
        elif self.flagged:
            self.image = self._images["flag"]
        else:
            self.image = self._images["unopened"]

    def _load_images(self):
        """Loads all of the necessary images for the tile
        """
        return {
            "-1": load_image("tile_mine_1.png"),
            "0": load_image("tile_empty.png"),
            "1": load_image("tile_1.png"),
            "2": load_image("tile_2.png"),
            "3": load_image("tile_3.png"),
            "4": load_image("tile_4.png"),
            "5": load_image("tile_5.png"),
            "6": load_image("tile_6.png"),
            "7": load_image("tile_7.png"),
            "8": load_image("tile_8.png"),
            "mine_clicked": load_image("tile_mine_2.png"),
            "unopened": load_image("tile_unopened.png"),
            "flag": load_image("tile_flag.png")
        }
