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
            self.image = self._images["opened"]
        elif self.flagged:
            self.image = self._images["flag"]
        else:
            self.image = self._images["unopened"]

    def _load_images(self):
        """Loads all of the necessary images for the tile
        """
        opened_image = "tile_" + str(self.digit) + ".png"
        if self.digit == -1:
            opened_image = "tile_mine_1.png"

        return {
            "opened": load_image(opened_image),
            "unopened": load_image("tile_unopened.png"),
            "mine_clicked": load_image("tile_mine_2.png"),
            "flag": load_image("tile_flag.png")
        }
