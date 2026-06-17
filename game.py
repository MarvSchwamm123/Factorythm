# ==============================
# Copyright (c) 2026 Marvin Sanzenbacher(germany-Baden Wüttemberg)
# All rights reserved.
# ==============================

import pygame
from states.home import HomeState
from states.game import GameState

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()

        self.state = HomeState(self)

        self.running = True

    def change_state(self, new_state):
        self.state = new_state

    def run(self):
        while self.running:
            self.state.handle_events()
            self.state.update()
            self.state.render(self.screen)

            pygame.display.flip()
            self.clock.tick(60)