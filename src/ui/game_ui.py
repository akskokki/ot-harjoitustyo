import pygame


from game_logic.level_generator import LevelGenerator
from game_logic.level import Level
from game_logic.game_loop import GameLoop
from utilities.event_queue import EventQueue
from utilities.renderer import Renderer
from utilities.clock import Clock


class GameUI:
    def __init__(self, level_width=0, level_height=0, level_mines=0):
        """Constructor which creates a LevelGenerator for generating a new level map and sets potential custom difficulty parameters

        Args:
            level_width, level_height, level_mines: optional parameters for a custom game
        """
        self.level_generator = LevelGenerator()
        self.level_width = level_width
        self.level_height = level_height
        self.level_mines = level_mines
        self.cell_size = 20

    def start(self, difficulty):
        """Creates the game display and starts the game loop

        Args:
            difficulty: previously chosen difficulty, used to generate an appropriate level
        
        Returns:
            time: passes on the result of the GameLoop
        """
        self._initialise_difficulty(difficulty)

        level_map = self.level_generator.generate_level(
            self.level_width, self.level_height, self.level_mines)

        width = len(level_map[0])
        height = len(level_map)
        screen = pygame.display.set_mode(
            [width*self.cell_size, height*self.cell_size])
        pygame.display.set_caption("Minesweeper")

        level = Level(level_map, self.cell_size)
        event_queue = EventQueue()
        renderer = Renderer(level, screen)
        clock = Clock()
        game_loop = GameLoop(level, renderer, event_queue, clock)

        pygame.init()
        time = game_loop.start()
        pygame.quit()

        return time

    def _initialise_difficulty(self, difficulty):
        """Sets the parameters of the level to match the chosen difficulty

        Args:
            difficulty: the difficulty level that has been chosen
        """
        if difficulty == 1:
            self.level_width = 9
            self.level_height = 9
            self.level_mines = 10
        elif difficulty == 2:
            self.level_width = 16
            self.level_height = 16
            self.level_mines = 40
        elif difficulty == 3:
            self.level_width = 30
            self.level_height = 16
            self.level_mines = 99
