import unittest
import pygame

from game_logic.level import Level


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

    def test_chording_works(self):
        self.assertEqual(self.level.tiles.sprites()[1].opened, False)
        self.assertEqual(self.level.tiles.sprites()[2].opened, False)
        self.assertEqual(self.level.tiles.sprites()[4].opened, False)
        self.assertEqual(self.level.tiles.sprites()[5].opened, False)
        self.level.click((50, 10), "left")
        self.assertEqual(self.level.tiles.sprites()[1].opened, True)
        self.assertEqual(self.level.tiles.sprites()[2].opened, True)
        self.assertEqual(self.level.tiles.sprites()[4].opened, True)
        self.assertEqual(self.level.tiles.sprites()[5].opened, True)

    def test_check_completion_incomplete(self):
        self.assertEqual(self.level.check_completion(), "incomplete")

    def test_check_completion_win(self):
        self.level.click((30, 10), "left")
        self.level.click((50, 10), "left")
        self.level.click((10, 30), "left")
        self.level.click((30, 30), "left")
        self.level.click((50, 30), "left")
        self.level.click((10, 50), "left")
        self.assertEqual(self.level.check_completion(), "win")

    def test_check_completion_loss(self):
        self.level.click((10, 10), "left")
        self.assertEqual(self.level.check_completion(), "loss")
