# ==============================
# Copyright (c) 2026 Marvin Sanzenbacher(germany-Baden Wüttemberg)
# All rights reserved.
# ==============================

import pygame
from typing import List

class Game_State:
    def __init__(self, game):
        self.game = game
        self.impulses: List["Impulse"] = []
        self.game = game
        self.grid_surface = self.create_grid_surface(
            game.screen.get_size(),
            40
        )
        self.dragging = False
        self.last_mouse = (0, 0)
        self.camera_x = 0
        self.camera_y = 0
        
        self.world_width = 2000
        
        screen_width = self.game.screen.get_width()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 2:  # Mausrad gedrückt
                    self.dragging = True
                    self.last_mouse = event.pos
                else:
                    self.dragging = False

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 2:
                    self.dragging = False

    def update(self):
        print("UPDATE")
        for i in self.impulses:
            i.update()
        
        if self.dragging:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            dx = mouse_x - self.last_mouse[0]
            dy = mouse_y - self.last_mouse[1]

            self.camera_x += dx
            self.camera_y += dy

            self.last_mouse = (mouse_x, mouse_y)
            print("dragging")

    def render(self, screen):
        font = pygame.font.SysFont("Arial", 40)
        text = font.render("GAME", True, (255, 255, 255))
        screen.blit(text, (500, 300))
        
        self.draw_background(screen)
        self.draw_grid(screen)
        
        for i in self.impulses:
            i.draw(screen)
            
    def draw_background(self, screen):
        screen.fill((48, 87, 225))  # blaues Blueprint-Feld
        
    def create_grid_surface(self, size, grid_size):
        surface = pygame.Surface(size)
        surface.fill((10, 20, 60))

        grid_color = (220, 220, 220)

        width, height = size

        for x in range(0, width, grid_size):
            pygame.draw.line(surface, grid_color, (x, 0), (x, height))

        for y in range(0, height, grid_size):
            pygame.draw.line(surface, grid_color, (0, y), (width, y))

        return surface
    
    def draw_grid(self, screen):
        grid_color = (220, 220, 220)
        grid_size = 40

        width, height = screen.get_size()

        offset_x = self.camera_x % grid_size
        offset_y = self.camera_y % grid_size

        for x in range(-grid_size, width + grid_size, grid_size):
            pygame.draw.line(
                screen,
                grid_color,
                (x + offset_x, 0),
                (x + offset_x, height)
            )

        for y in range(-grid_size, height + grid_size, grid_size):
            pygame.draw.line(
                screen,
                grid_color,
                (0, y + offset_y),
                (width, y + offset_y)
            )
        
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