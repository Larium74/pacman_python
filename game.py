import pygame
import sys
import random
from pacman import PacMan
from ghost import Ghost
from coin import Coin
from utils import draw_score, draw_lives, load_image

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption('Pac-Man')
        self.clock = pygame.time.Clock()
        self.pacman = PacMan(100, 100)
        self.ghost = Ghost(400, 300)
        self.score = 0
        self.lives = 4
        self.coins = [Coin(random.randint(0, 624), random.randint(0, 464)) for _ in range(20)]  # Genera 20 monedas en posiciones aleatorias

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            self.pacman.move(keys)
            self.ghost.move_towards(self.pacman.x, self.pacman.y)

            # Colisión con fantasma
            if self.pacman.collides_with(self.ghost):
                self.lives -= 1
                if self.lives == 0:
                    self.reset_game()

            # Colisión con monedas
            self.coins = [coin for coin in self.coins if not self.collect_coin(coin)]

            self.draw()

            pygame.display.update()
            self.clock.tick(30)

    def collect_coin(self, coin):
        if coin.collides_with(self.pacman):
            self.score += 10
            return True
        return False

    def reset_game(self):
        self.pacman.reset_position()
        self.lives = 4
        self.score = 0
        self.coins = [Coin(random.randint(0, 624), random.randint(0, 464)) for _ in range(20)]

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.pacman.draw(self.screen)
        self.ghost.draw(self.screen)
        for coin in self.coins:
            coin.draw(self.screen)
        draw_score(self.screen, self.score)
        draw_lives(self.screen, self.lives)