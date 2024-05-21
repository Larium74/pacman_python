import pygame
import random
from utils import load_image

class Coin:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(load_image('imgs/coin.png'), (16, 16))  # Tamaño ajustado a 16x16 píxeles

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def collides_with(self, pacman):
        return self.x < pacman.x + 32 and self.x + 16 > pacman.x and self.y < pacman.y + 32 and self.y + 16 > pacman.y