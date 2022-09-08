import pygame
from pygame.locals import *
from sys import exit 
from random import randint

# initialization 
pygame.init()

# global var
size = (1080, 720)
COLOR = (255, 255, 255)
SCORE = 0
SPEED = 10
DIRECTION = [SPEED, 0]
FPS = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)
# params
pygame.display.set_caption("Snake game")
screen = pygame.display.set_mode(size)

# defs
def load_img(src, x, y):
    image = pygame.image.load(src).convert()
    image = pygame.transform.scale(image, (30, 30))
    rect  = image.get_rect(center=(x, y))
    transparent = image.get_at((0, 0))
    image.set_colorkey(transparent)
    return image, rect 

def pickup():
    global apple_rect, head_rect, SCORE

    if head_rect.colliderect(apple_rect):
        apple_rect.x = randint(40, 1000)
        apple_rect.y = randint(40, 680)
        SCORE += 1

def score():
    global SCORE, COLOR
    text = font.render(f'Очки: {SCORE}', True, COLOR)
    text_rect = text.get_rect(center=(540,700))
    screen.blit(text, text_rect)

def move(snake): 
    global DIRECTION, SPEED, COLOR, KEYS

    if KEYS[K_UP] or KEYS[K_w]: 
        DIRECTION = [0, -SPEED]
    elif KEYS[K_DOWN] or KEYS[K_s]:
        DIRECTION = [0, SPEED]
    elif KEYS[K_RIGHT] or KEYS[K_d]: 
        DIRECTION = [SPEED, 0]
    elif KEYS[K_LEFT] or KEYS[K_a]: 
        DIRECTION = [-SPEED, 0]
    
    if snake.right > 1080: 
        DIRECTION = [-SPEED, 0]
    elif snake.left < 0:
        DIRECTION = [SPEED, 0]
    elif snake.bottom > 720:
        snake.bottom = 30
    elif snake.top < 0:
        snake.top = 700

    snake.move_ip(DIRECTION)

# variables 
head_image, head_rect = load_img('./img/head.png', 400, 300)
apple_image, apple_rect = load_img('./img/apple.png', 200, 200)
body_image, body_rect = load_img('./img/body.png', 370, 300)

while True: 
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT: 
            pygame.quit()
            exit()
    
    KEYS = pygame.key.get_pressed()
    screen.blit(head_image, head_rect)
    screen.blit(apple_image, apple_rect)
    move(head_rect)
    pickup()
    score()
    pygame.display.update()
    FPS.tick(30)