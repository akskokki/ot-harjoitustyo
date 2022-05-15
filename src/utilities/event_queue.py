import pygame


class EventQueue:
    """Class for the simple purpose of fetching the pygame event list
    """

    def get(self):
        """Gets the pygame event list

        Returns:
            List: the list of all pygame events in the queue
        """
        return pygame.event.get()
