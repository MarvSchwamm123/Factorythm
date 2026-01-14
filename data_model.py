import pygame
import math
import os
import time

class factorythm:
    def __init__(self):
        self.width = 1680
        self.height = 1050
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

class board:
    def create_empty_grid(self, rows: int, cols: int) -> list[list[str]]:
        self.rows = 100
        self.cols = 100
        self.grid = [[" " for _ in range(cols)] for _ in range(rows)]
        return self.grid
    
    def add_impulse_machine(self, frequency: str, position: tuple[int, int], ):
        self.grid[position[0]][position[1]] = impulse_machine(frequency)

    def add_delay_machine(self, delay_ticks: int, position: tuple[int, int]):
        self.grid[position[0]][position[1]] = delay_machine(delay_ticks)

    def remove_machine(self, position: tuple[int, int]):
        self.grid[position[0]][position[1]] = " "

    def get_machine(self, position: tuple[int, int]):
        return self.grid[position[0]][position[1]]

class entities:
    def __init__(self):
        self.entities_list = []

def send_impulse(tick):
    pass

class impulse_machine: # I Impulse Machine
    def __init__(self, frequency: int):
        self.frequency = frequency
        self.last_impulse_time = time.time()
        self.name = "I"

    def check_and_send_impulse(self, tick: int):
        if tick % self.frequency == 0:
            send_impulse(tick)

class delay_machine:
    def __init__(self, delay_ticks: int):
        self.delay_ticks = delay_ticks
        self.queue = []

    def add_impulse(self, tick):
        self.queue.append(tick + self.delay_ticks)

    def update(self, tick):
        # Sende Impulse, deren Tick erreicht ist
        ready = [t for t in self.queue if t <= tick]
        for t in ready:
            send_impulse(t)
            self.queue.remove(t)
