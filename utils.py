import pygame

def load_image(path):
    return pygame.image.load(path)

def draw_score(screen, score):
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

def draw_lives(screen, lives):
    font = pygame.font.Font(None, 36)
    lives_text = font.render(f'Lives: {lives}', True, (255, 255, 255))
    screen.blit(lives_text, (500, 10))