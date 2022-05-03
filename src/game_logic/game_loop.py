import pygame


class GameLoop:
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
            self._handle_events()
            self.level.update()
            result = self.level.check_completion()
            if result == "win":
                return self.clock.get_ticks()
            if result == "loss":
                return -1
            self.renderer.render()
            self.clock.tick(60)
        return 0

    def _handle_events(self):
        """Event handler that responds to the user's clicks on the minefield
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                buttons = pygame.mouse.get_pressed()
                if buttons[0] is True:
                    self.level.click(event.pos, "left")
                elif buttons[2] is True:
                    self.level.click(event.pos, "right")
