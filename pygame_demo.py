import pygame 
import os 
import time 
import math
from data_model import *

class pygame_demo:
    def __init__(self, game_state="home_screen"):
        self.width = 1680
        self.height = 1050
        self.board = board()
        self.factorythm = data_model()
        self.running = True
        self.surface = pygame.display.set_mode((self.width, self.height))
        self.TPS = 60
        self.clock = pygame.time.Clock()
        self.tick = 0
        self.last_time = time.time()
        self.game_state = game_state
        self.new_game_button = button((300, 400), (100, 50), "New Game")
        self.resume_game_button = button((100, 500), (100, 50), "Resume Game")
        self.save_game_button = button((500, 600), (100, 50), "Save Game")
        self.load_game_button = button((500, 700), (100, 50), "Load Game")
        self.settings_button = button((800, 700), (100, 50), "Settings")

    def main(self):
        while self.running:
            surface = self.surface
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
            now = time.time()
            if now - self.last_time >= 1 / self.TPS:
                self.last_time = now
                self.tick += 1
                if self.game_state == "in_world":
                    self.factorythm.update(self.tick, self.board)
                    surface.fill((0, 0, 200))
                elif self.game_state == "home_screen":
                    surface.fill((0, 0, 0))
                    self.new_game_button.draw(surface)
                    self.resume_game_button.draw(surface)
                    new_game_button_return = self.new_game_button.is_hovering_above()
                    resume_game_button_return = self.resume_game_button.is_hovering_above()
                    load_game_button_return = self.load_game_button.is_hovering_above()
                    settings_button_return = self.settings_button.is_hovering_above()

                    if new_game_button_return[1]:
                        self.game_state = "in_world"
                    if resume_game_button_return[1]:
                        self.game_state = "in_world"
                    if load_game_button_return[1]:
                        pass
                    if settings_button_return[1]:
                        self.game_state = "settings_menu"

                elif self.game_state == "pause_menu":
                    pass
                elif self.game_state == "settings_menu":
                    pass

            #screen = scaled surface on real display
            display_info = pygame.display.Info()
            screen_width = display_info.current_w
            screen_height = display_info.current_h
            screen = pygame.Surface((screen_width, screen_height))    
            scaled_surface = pygame.transform.scale(surface, (screen_width, screen_height))
            screen.blit(scaled_surface, (0, 0))
            pygame.display.get_surface().blit(screen, (0, 0))

            pygame.display.flip()
        END()
            
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
    
    def is_hovering_above(self) -> bool:
        state = []
        mouse_pos = pygame.mouse.get_pos()
        if (self.position[0] <= mouse_pos[0] <= self.position[0] + self.size[0] and self.position[1] <= mouse_pos[1] <= self.position[1] + self.size[1]):
            state.append(True)
            state.append(self.is_clicked(from_hover=True))
        else:
            state.append(False)
            state.append(False)
        return state

    def is_clicked(self, from_hover=False) -> bool:
        if from_hover:
            if pygame.mouse.get_pressed()[0]:
                return True
        mouse_pos = pygame.mouse.get_pos()
        if (self.position[0] <= mouse_pos[0] <= self.position[0] + self.size[0] and self.position[1] <= mouse_pos[1] <= self.position[1] + self.size[1]):
            if pygame.mouse.get_pressed()[0]:
                return 2
        return 0
    
def save_game():
    pass

def END():
    save_game()
    pygame.quit()
    os._exit(0)