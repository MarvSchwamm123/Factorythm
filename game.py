# ==============================
# Copyright (c) 2026 Marvin Sanzenbacher(germany-Baden Wüttemberg)
# All rights reserved.
# ==============================

import pygame
import os
from states.home import Home_State
from states.game import Game_State

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        
        self.HomeState = Home_State(self)
        self.GameState = Game_State(self)

        self.state = self.HomeState

        self.running = True

    def change_state(self, new_state):
        self.state = new_state

    def run(self):
        while self.running:
            self.state.handle_events()
            self.state.update()
            self.state.render(self.screen)
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_ESCAPE:
                        running = False

            pygame.display.flip()
            self.clock.tick(60)