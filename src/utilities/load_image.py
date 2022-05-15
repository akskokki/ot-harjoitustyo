import os
import pygame

directory = os.path.dirname(__file__)


def load_image(file):
    """Loads the specified file form the assets-folder into pygame

    Args:
        file: the name of the file being loaded
    """

    return pygame.image.load(
        os.path.join(directory, "..", "assets", file)
    )
