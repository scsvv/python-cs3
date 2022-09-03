import pygame
from pygame.locals import *
from sys import exit 
from random import randint

# initialization 
pygame.init()

# global var
size = (1080, 720)
HEAD = Rect(400, 300, 30, 30)
COLOR = (255, 255, 255)
SPEED = 10
DIRECTION = [SPEED, 0]
FPS = pygame.time.Clock()

# params
pygame.display.set_caption("Snake game")
screen = pygame.display.set_mode(size)

# defs
def rand_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


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
    
    # snake.top snake.bottom snake.left snake.right
    if snake.right > 1080: 
        DIRECTION = [-SPEED, 0]
        COLOR = rand_color()
    elif snake.left < 0:
        DIRECTION = [SPEED, 0]
        COLOR = rand_color()

    snake.move_ip(DIRECTION)

while True: 
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT: 
            pygame.quit()
            exit()
    
    KEYS = pygame.key.get_pressed()
    pygame.draw.rect(screen, COLOR, HEAD)
    move(HEAD)
    pygame.display.update()
    FPS.tick(30)