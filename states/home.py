# ==============================
# Copyright (c) 2026 Marvin Sanzenbacher(germany-Baden Wüttemberg)
# All rights reserved.
# ==============================

import pygame
from states.game import GameState

class HomeState:
    def __init__(self, game):
        self.game = game

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.game.change_state(GameState(self.game))

    def update(self):
        pass

    def render(self, screen):
        screen.fill((10, 10, 20))

        font = pygame.font.SysFont("Arial", 50)
        text = font.render("FACTORYTHM", True, (255, 255, 255))
        screen.blit(text, (400, 200))