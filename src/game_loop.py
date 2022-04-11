import pygame

class GameLoop:
    def __init__(self, level, renderer, event_queue, clock):
        self.level = level
        self.renderer = renderer
        self.event_queue = event_queue
        self.clock = clock

        self.running = True
    
    def start(self):
        while (self.running):
            self._handle_events()
            self.level.update()

            self.renderer.render()
    
    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.level.click(event.pos)