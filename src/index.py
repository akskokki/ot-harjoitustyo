import sys
from tkinter import Tk
import pygame
from level_generator import LevelGenerator
from level import Level
from event_queue import EventQueue
from game_loop import GameLoop
from renderer import Renderer
from clock import Clock
from ui.ui import UI


def main():
    # work in progress; will be refactored later
    difficulty_select = Tk()
    difficulty_select.title("Minesweeper")

    difficulty_ui = UI(difficulty_select)
    difficulty_ui.start()

    difficulty_select.resizable(False, False)
    difficulty_select.mainloop()

    if difficulty_ui.selection == 1:
        level_width = 9
        level_height = 9
        level_mines = 10
    elif difficulty_ui.selection == 2:
        level_width = 16
        level_height = 16
        level_mines = 40
    elif difficulty_ui.selection == 3:
        level_width = 30
        level_height = 16
        level_mines = 99
    else:
        sys.exit()

    level_generator = LevelGenerator()
    level_map = level_generator.generate_level(
        level_width, level_height, level_mines)
    cell_size = 20

    width = len(level_map[0])
    height = len(level_map)
    screen = pygame.display.set_mode([width*cell_size, height*cell_size])

    pygame.display.set_caption("Minesweeper")

    level = Level(level_map, cell_size)

    event_queue = EventQueue()
    renderer = Renderer(level, screen)
    clock = Clock()

    game_loop = GameLoop(level, renderer, event_queue, clock)

    pygame.init()
    game_loop.start()

    pygame.quit()


if __name__ == "__main__":
    main()
