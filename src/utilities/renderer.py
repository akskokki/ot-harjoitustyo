import pygame


class Renderer:
    """Class for rendering the game into pygame

    Attributes:
        level: the level being rendered
        display: the display which the level is being rendered on
    """

    def __init__(self, level, display):
        """Constructor which sets the level and display being used

        Args:
            level: the level being rendered
            display: the display which the level is being rendered on
        """
        self.level = level
        self.display = display

    def render(self):
        """Renders all sprites from the level onto the display
        """
        self.level.all_sprites.draw(self.display)
        pygame.display.flip()
