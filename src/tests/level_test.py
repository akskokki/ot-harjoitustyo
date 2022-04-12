import unittest
import pygame
from level import Level


LEVEL_MAP = [[-1, 1, 0],
             [2, 3, 2],
             [1, -1, -1]]

CELL_SIZE = 20


class TestLevel(unittest.TestCase):
    def setUp(self):
        self.level = Level(LEVEL_MAP, CELL_SIZE)

    def _click_middle(self, button):
        self.level.click((30, 30), button)

    def _opened_middle(self):
        return self.level.tiles.sprites()[4].opened

    def _flagged_middle(self):
        return self.level.tiles.sprites()[4].flagged

    def test_left_click_opens_tile(self):
        self.assertEqual(self._opened_middle(), False)
        self._click_middle("left")
        self.assertEqual(self._opened_middle(), True)

    def test_right_click_flags_tile(self):
        self.assertEqual(self._flagged_middle(), False)
        self._click_middle("right")
        self.assertEqual(self._flagged_middle(), True)

    def test_cant_open_flagged_tile(self):
        self._click_middle("right")
        self.assertEqual(self._opened_middle(), False)
        self._click_middle("left")
        self.assertEqual(self._opened_middle(), False)
