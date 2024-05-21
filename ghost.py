import pygame
import random
from utils import load_image

class Ghost:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 2
        self.original_image = load_image('imgs/fant.png')
        self.image = pygame.transform.scale(self.original_image, (32, 32))  # Ajusta el tamaño a 32x32 píxeles

    def move_towards(self, pacman_x, pacman_y):
        if pacman_x < self.x:
            self.x -= self.speed
        elif pacman_x > self.x:
            self.x += self.speed
        if pacman_y < self.y:
            self.y -= self.speed
        elif pacman_y > self.y:
            self.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))