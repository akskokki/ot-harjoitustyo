import pygame


class Clock:
    """A class for executing basic functions of the pygame Clock-object

    Attributes:
        clock: a pygame Clock-object
    """

    def __init__(self):
        """Constructor which creates the Clock-object
        """

        self.clock = pygame.time.Clock()

    def tick(self, fps):
        """Sets the framerate of the clock
        """

        self.clock.tick(fps)

    def wait(self, time):
        """Waits for the specified amount of time in milliseconds
        """
        pygame.time.wait(time)

    def get_ticks(self):
        """Gets the amount of ticks that have passed since the beginning of the game

        Returns:
            Integer: ticks passed since the beginning of the game
        """

        return pygame.time.get_ticks()
