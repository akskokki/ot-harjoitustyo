import unittest
from game_logic.level_generator import LevelGenerator


class TestLevelGenerator(unittest.TestCase):
    def setUp(self):
        self.level_generator = LevelGenerator()
        self.width = 5
        self.height = 6
        self.mines = 7
        self.level_map = self.level_generator.generate_level(
            self.width, self.height, self.mines)

    def _count_mines_around_tile(self, x, y):
        mine_count = 0
        for num_x in range(x-1, x+2):
            for num_y in range(y-1, y+2):
                if num_x < 0 or num_x >= self.width or num_y < 0 or num_y >= self.height:
                    continue
                if self.level_map[num_y][num_x] == -1:
                    mine_count += 1
        return mine_count

    def test_level_dimensions(self):
        self.assertEqual(len(self.level_map[0]), 5)
        self.assertEqual(len(self.level_map), 6)

    def test_mine_count(self):
        mine_count = 0
        for y in range(self.height):
            for x in range(self.width):
                if self.level_map[y][x] == -1:
                    mine_count += 1
        self.assertEqual(mine_count, self.mines)

    def test_correct_digits(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.level_map[y][x] == -1:
                    continue
                self.assertEqual(self._count_mines_around_tile(
                    x, y), self.level_map[y][x])
