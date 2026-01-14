import pygame 
import os 
import time 
import math
from data_model import data_model

class pygame_demo:
    def __init__(self):
        self.data_model = data_model()
        self.running = True
        self.TPS = 60
        self.clock = pygame.time.Clock()
        self.tick = 0
        self.last_time = time.time()

    def main(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
            self.data_model.screen.fill((0, 0, 0))
            now = time.time()
            if now - self.last_time >= 1 / self.TPS:
                self.last_time = now
                self.tick += 1
                