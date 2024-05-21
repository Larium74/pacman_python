import pygame
from utils import load_image

class PacMan:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.original_image_open = load_image('imgs/pacbocaabierta.png')
        self.original_image_closed = load_image('imgs/pacbocaabierta.png')
        self.image_open = pygame.transform.scale(self.original_image_open, (32, 32))  # Ajusta el tamaño a 32x32 píxeles
        self.image_closed = pygame.transform.scale(self.original_image_closed, (32, 32))  # Ajusta el tamaño a 32x32 píxeles
        self.image = self.image_open
        self.animation_counter = 0
        self.animation_speed = 10
        self.open = True

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed
        self.animate()

    def animate(self):
        self.animation_counter += 1
        if self.animation_counter % self.animation_speed == 0:
            self.open = not self.open
            self.image = self.image_open if self.open else self.image_closed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def reset_position(self):
        self.x = 100
        self.y = 100

    def collides_with(self, ghost):
        return self.x < ghost.x + 32 and self.x + 32 > ghost.x and self.y < ghost.y + 32 and self.y + 32 > ghost.y