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

    def move(self):
        angle = random.uniform(0, 2*np.pi)
        self.x += np.cos(angle) * self.speed
        self.y += np.sin(angle) * self.speed
        self.energy -= 0.3 * (1 + self.speed)

        self.x %= WIDTH
        self.y %= HEIGHT

    def seek_food(self, foods):
        for food in foods:
            dist = np.hypot(self.x - food.x, self.y - food.y)
            if dist < self.vision:
                dx, dy = food.x - self.x, food.y - self.y
                mag = np.hypot(dx, dy)
                if mag > 0:
                    self.x += dx / mag * self.speed
                    self.y += dy / mag * self.speed
                break

    def eat(self, foods):
        for food in foods[:]:
            if np.hypot(self.x - food.x, self.y - food.y) < 6:
                self.energy += 40 * self.efficiency
                foods.remove(food)

    def reproduce(self):
        if self.energy > 160:
            self.energy -= 60
            child_dna = self.dna + np.random.normal(0, 0.08, size=3)
            return Creature(self.x, self.y, np.clip(child_dna, 0, 1))
        return None

    def alive(self):
        return self.energy > 0
class Food:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)

# ---------- SIMULATION ----------

creatures = [Creature(random.randint(0, WIDTH), random.randint(0, HEIGHT))
             for _ in range(CREATURE_COUNT)]
foods = [Food() for _ in range(FOOD_COUNT)]

font = pygame.font.SysFont(None, 22)