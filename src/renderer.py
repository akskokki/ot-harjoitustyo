import pygame

class Renderer:
    def __init__(self, level, display):
        self.level = level
        self.display = display
    
    def render(self):
        self.level.all_sprites.draw(self.display)
        pygame.display.flip()