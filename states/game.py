# ==============================
# Copyright (c) 2026 Marvin Sanzenbacher(germany-Baden Wüttemberg)
# All rights reserved.
# ==============================

import pygame

class GameState:
    def __init__(self, game):
        self.game = game
        self.impulses: list[Impulse] = []

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False

    def update(self):
        for i in self.impulses:
            i.update()

    def render(self, screen):
        screen.fill((0, 0, 0))

        font = pygame.font.SysFont("Arial", 40)
        text = font.render("GAME", True, (255, 255, 255))
        screen.blit(text, (500, 300))
        for i in self.impulses:
            i.draw(screen)
        
class Impulse:
    def __init__(self):
        self.x = 100
        self.y = 300
        self.note = "C"
        self.speed = 2

    def update(self):
        self.x += self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), 10)