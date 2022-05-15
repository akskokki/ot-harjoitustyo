import unittest
import pygame

from game_logic.level import Level
from game_logic.game_loop import GameLoop


class StubClock:
    def tick(self, fps):
        pass

    def wait(self, ms):
        pass

    def get_ticks(self):
        1


class StubEvent:
    def __init__(self, event_type, button, pos):
        self.type = event_type
        self.button = button
        self.pos = pos


class StubEventQueue:
    def __init__(self, events):
        self._events = events

    def get(self):
        return self._events


class StubRenderer:
    def render(self):
        pass


LEVEL_MAP = [[-1, 1, 0],
             [2, 3, 2],
             [1, -1, -1]]

CELL_SIZE = 20


class TestGameLoop(unittest.TestCase):
    def setUp(self):
        self.level = Level(LEVEL_MAP, CELL_SIZE)
    
    def test_level_win(self):
        events = [
            StubEvent(pygame.MOUSEBUTTONDOWN, 1, (50, 10)),
            StubEvent(pygame.MOUSEBUTTONDOWN, 1, (10, 30)),
            StubEvent(pygame.MOUSEBUTTONDOWN, 1, (10, 50))
        ]
        game_loop = GameLoop(self.level, StubRenderer(), StubEventQueue(events), StubClock())
        game_loop.start()
        self.assertEqual(self.level.check_completion(), "win")
    
    def test_level_loss(self):
        events = [
            StubEvent(pygame.MOUSEBUTTONDOWN, 1, (10, 10))
        ]
        game_loop = GameLoop(self.level, StubRenderer(), StubEventQueue(events), StubClock())
        game_loop.start()
        self.assertEqual(self.level.check_completion(), "loss")
    
    def test_flag_input_works(self):
        events = [
            StubEvent(pygame.MOUSEBUTTONDOWN, 3, (10, 10)),
            StubEvent(pygame.QUIT, 0, 0)
        ]
        self.assertEqual(self.level.tiles_grid[0][0].flagged, False)
        game_loop = GameLoop(self.level, StubRenderer(), StubEventQueue(events), StubClock())
        game_loop.start()
        self.assertEqual(self.level.tiles_grid[0][0].flagged, True)
