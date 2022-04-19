import pygame
from utilities.load_image import load_image


class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, digit):
        super().__init__()
        # -1: mine, 0-8: number
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
        if not self.flagged and not self.opened:
            self.opened = True
            return True
        return False

    def flag(self):
        if self.opened is False:
            self.flagged = not self.flagged

    def explode(self):
        self.exploded = True

    def update(self):
        if self.exploded:
            self.image = self._images["mine_clicked"]
        elif self.opened:
            self.image = self._images[str(self.digit)]
        elif self.flagged:
            self.image = self._images["flag"]
        else:
            self.image = self._images["unopened"]

    def _load_images(self):
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
