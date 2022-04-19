import pygame


class GameLoop:
    def __init__(self, level, renderer, event_queue, clock):
        self.level = level
        self.renderer = renderer
        self.event_queue = event_queue
        self.clock = clock

        self.running = True

    def start(self):
        while self.running:
            self._handle_events()
            self.level.update()
            result = self.level.check_completion()
            print(result)
            if result in ("win", "loss"):
                return result
            self.renderer.render()
        return "quit"

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                buttons = pygame.mouse.get_pressed()
                if buttons[0] is True:
                    self.level.click(event.pos, "left")
                elif buttons[2] is True:
                    self.level.click(event.pos, "right")
