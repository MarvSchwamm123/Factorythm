# ==============================
# Copyright (c) 2026 Marvin Sanzenbacher(germany-Baden Wüttemberg)
# All rights reserved.
# ==============================

import pygame
from states.game import Game_State
from enum import Enum

class MENU_BUTTON(Enum):
    START = 1
    LOAD = 2
    SETTINGS = 3
    QUIT = 4

class Home_State:
    def __init__(self, game):
        self.game = game
        

        self.logo = pygame.image.load("pictures/theme.png").convert_alpha()
        self.button_img = pygame.image.load("pictures/button.png").convert_alpha()
        
        self.logo_scale = 1.0

        screen_width = game.screen.get_width()

        target_width = int(screen_width * 0.75)

        # Originalgröße holen
        original_rect = self.logo.get_rect()
        scale_factor = target_width / original_rect.width

        target_height = int(original_rect.height * scale_factor)

        self.logo = pygame.transform.scale(
            self.logo,
            (target_width, target_height)
        )
        self.button_img = pygame.transform.scale(
            self.button_img, 
            (400, 120)
        )
        
        self.button_names = {
            MENU_BUTTON.START: "New Game",
            MENU_BUTTON.LOAD: "Load Game",
            MENU_BUTTON.SETTINGS: "Settings",
            MENU_BUTTON.QUIT: "Quit"
        }
        
        self.menu_items = [
            MENU_BUTTON.START,
            MENU_BUTTON.LOAD,
            MENU_BUTTON.SETTINGS,
            MENU_BUTTON.QUIT
        ]
        self.selected_index = 0
        self.button_scales = [1.0 for _ in self.menu_items]
        self.scale_speed = 0.15
        
        
        self.phase = "intro" # intro/menu

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.running = False
                    
                if event.key == pygame.K_UP:
                    self.selected_index = max(0, self.selected_index - 1)

                if event.key == pygame.K_DOWN:
                    self.selected_index = min(
                        len(self.menu_items) - 1,
                        self.selected_index + 1
                    )

                if event.key == pygame.K_RETURN:

                    if self.phase == "intro":
                        self.phase = "menu"

                    else:
                        selected = self.menu_items[self.selected_index]

                        if selected == MENU_BUTTON.START:
                            self.game.state = Game_State(self.game)

                        elif selected == MENU_BUTTON.LOAD:
                            print("Load")

                        elif selected == MENU_BUTTON.SETTINGS:
                            print("Settings")

                        elif selected == MENU_BUTTON.QUIT:
                            self.game.running = False
                    

    def update(self):
        if self.phase == "menu":
            self.logo_scale -= 0.02
            if self.logo_scale < 0.3:
                self.logo_scale = 0.3

    def render(self, screen):
        screen.fill((10, 20, 60))

        screen_width = screen.get_width()

        width = int(screen_width * self.logo_scale)
        ratio = self.logo.get_height() / self.logo.get_width()
        height = int(width * ratio)

        logo = pygame.transform.scale(self.logo, (width, height))

        logo_rect = logo.get_rect()

        if self.phase == "intro":
            logo_rect.center = (screen.get_width() // 2, screen.get_height() // 2)
        else:
            logo_rect.center = (screen.get_width() // 2, 120)

        screen.blit(logo, logo_rect)
        
        if self.phase == "menu":
            self.update_menu()
            self.draw_menu(screen)

    def draw_menu(self, screen):
        font = pygame.font.SysFont("Arial", 30)

        for i, item in enumerate(self.menu_items):

            x = screen.get_width() // 2
            y = 300 + i * 100

            scale = self.button_scales[i]

            button = pygame.transform.scale(
                self.button_img,
                (
                    int(self.button_img.get_width() * scale),
                    int(self.button_img.get_height() * scale)
                )
            )

            rect = button.get_rect(center=(x, y))
            screen.blit(button, rect)

            text = font.render(
                self.button_names[item],
                True,
                (255, 255, 255)
            )
            text_rect = text.get_rect(center=(x, y))
            screen.blit(text, text_rect)
            
    def update_menu(self):
        for i in range(len(self.menu_items)):

            target = 1.1 if i == self.selected_index else 1.0

            self.button_scales[i] += (target - self.button_scales[i]) * self.scale_speed