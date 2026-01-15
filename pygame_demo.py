import pygame 
import os 
import time 
import math
from data_model import *

class pygame_demo:
    def __init__(self):
        self.factorythm = factorythm()
        self.running = True
        self.TPS = 60
        self.clock = pygame.time.Clock()
        self.tick = 0
        self.last_time = time.time()

    def main(self):
        while self.running:
            surface = pygame.display.get_surface()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
            self.data_model.screen.fill((0, 0, 0))
            now = time.time()
            if now - self.last_time >= 1 / self.TPS:
                self.last_time = now
                self.tick += 1
                if self.game_state == "in_world":
                    self.factorythm.update(self.tick)
                elif self.game_state == "home_screen":
                    pass
                elif self.game_state == "pause_menu":
                    pass
                elif self.game_state == "settings_menu":
                    pass
            pygame.display.flip()

            #show display
            
class button:
    def __init__(self, position: tuple[int, int], size: tuple[int, int], text: str):
        self.position = position
        self.size = size
        self.text = text

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), (self.position[0], self.position[1], self.size[0], self.size[1]))
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(self.position[0] + self.size[0] / 2, self.position[1] + self.size[1] / 2))
        surface.blit(text_surface, text_rect)
    
    def is_hovering_over(self) -> bool:
        mouse_pos = pygame.mouse.get_pos()
        if (self.position[0] <= mouse_pos[0] <= self.position[0] + self.size[0] and self.position[1] <= mouse_pos[1] <= self.position[1] + self.size[1]):
            return(self.is_clicked(from_hover=True))
            return 1
        else:
            return 0

    def is_clicked(self, from_hover=False) -> bool:
        if from_hover:
            if pygame.mouse.get_pressed()[0]:
                return True
        mouse_pos = pygame.mouse.get_pos()
        if (self.position[0] <= mouse_pos[0] <= self.position[0] + self.size[0] and self.position[1] <= mouse_pos[1] <= self.position[1] + self.size[1]):
            if pygame.mouse.get_pressed()[0]:
                return 2
        return 0