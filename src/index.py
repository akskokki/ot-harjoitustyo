from sprites.tile import Tile
from level_generator import LevelGenerator
from level import Level
from event_queue import EventQueue
from game_loop import GameLoop
from renderer import Renderer
import pygame

def main():
    level_generator = LevelGenerator()
    level_map = level_generator.generate_level(9, 9, 10)

    width = len(level_map[0])
    height = len(level_map)
    screen = pygame.display.set_mode([width*20,height*20])

    pygame.display.set_caption("Minesweeper")

    level = Level(level_map)

    event_queue = EventQueue()
    renderer = Renderer(level, screen)
    clock = pygame.time.Clock

    game_loop = GameLoop(level, renderer, event_queue, clock)

    pygame.init()
    game_loop.start()
        
    pygame.quit()

if __name__ == "__main__":
    main()