import pygame


class GameLoop:
    """Class which controls the game loop and responds to the user's actions

    Attributes:
        level: Level-object which represents the current level that is being played
        renderer: Renderer-object which handles rendering
        event_queue: EventQueue-object used to handle pygame-events
        clock: Clock-object based on pygame.time.Clock
        running: Boolean variable that determines whether the loop is running
    """

    def __init__(self, level, renderer, event_queue, clock):
        """Constructor which initialises the gameloop and the tools required for its functionality

        Args:
            level: Level-object which represents the current level that is being played
            renderer: Renderer-object which handles rendering
            event_queue: EventQueue-object used to handle pygame-events
            clock: Clock-object based on pygame.time.Clock
        """
        self.level = level
        self.renderer = renderer
        self.event_queue = event_queue
        self.clock = clock

        self.running = True

    def start(self):
        """Starts the gameloop

        Returns:
            -1 on loss
            0 on quit
            >0 (total game time) on win
        """

        while self.running:
            result = self.level.check_completion()
            self._handle_events()
            self.level.update()
            self.renderer.render()
            if result == "win":
                final_time = self.clock.get_ticks()
                self.clock.wait(2000)
                return final_time
            if result == "loss":
                self.clock.wait(2000)
                return -1
            self.clock.tick(60)
        return 0

    def _handle_events(self):
        """Event handler that responds to the user's clicks on the minefield
        """
        for event in self.event_queue.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.level.click(event.pos, "left")
                elif event.button == 3:
                    self.level.click(event.pos, "right")
