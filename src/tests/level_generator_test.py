import unittest
from level_generator import LevelGenerator

class TestLevelGenerator(unittest.TestCase):
    def setUp(self):
        self.level_generator = LevelGenerator()

    def test_level_dimensions(self):
        level_map = self.level_generator.generate_level(5, 6, 7)
        self.assertEqual(len(level_map[0]), 5)
        self.assertEqual(len(level_map), 6)