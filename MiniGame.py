import pygame
import random
import numpy as np

WIDTH, HEIGHT = 900, 600
CREATURE_COUNT = 80
FOOD_COUNT = 120

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()