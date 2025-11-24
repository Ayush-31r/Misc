import pygame
import random
import numpy as np

WIDTH, HEIGHT = 900, 600
CREATURE_COUNT = 80
FOOD_COUNT = 120

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# ---------- ENTITIES ----------

class Creature:
    def __init__(self, x, y, dna=None):
        self.x = x
        self.y = y
        self.energy = 100

        self.dna = dna if dna is not None else np.random.rand(3)
        self.speed = self.dna[0] * 2 + 0.5
        self.vision = self.dna[1] * 120 + 20
        self.efficiency = self.dna[2]