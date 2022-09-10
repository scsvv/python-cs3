import pygame
from pygame.locals import *
from sys import exit 
from random import randint
import time

# initialization 
pygame.init()

# global var
size = (1080, 720)
COLOR = (255, 255, 255)
SCORE = 0
SPEED = 30
DIRECTION = [SPEED, 0]
FPS = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)
# params
pygame.display.set_caption("Snake game")
screen = pygame.display.set_mode(size)

# defs
def game_over(): 
    global snake, head_rect

    for el in snake[1:]:
        if head_rect.colliderect(el):
            return True
    
    return False 

def load_img(src, x, y):
    image = pygame.image.load(src).convert()
    image = pygame.transform.scale(image, (30, 30))
    rect  = image.get_rect(center=(x, y))
    transparent = image.get_at((0, 0))
    image.set_colorkey(transparent)
    return image, rect 

def pickup():
    global apple_rect, head_rect, SCORE, snake

    if head_rect.colliderect(apple_rect):
        apple_rect.x = randint(40, 1000)
        apple_rect.y = randint(40, 680)
        snake.append(snake[1].copy())
        SCORE += 1

def score():
    global SCORE, COLOR
    text = font.render(f'Очки: {SCORE}', True, COLOR)
    text_rect = text.get_rect(center=(540,700))
    screen.blit(text, text_rect)

def move(obj, body): 
    global DIRECTION, SPEED, COLOR, KEYS

    if (KEYS[K_UP] or KEYS[K_w]) and DIRECTION[1] == 0: 
        DIRECTION = [0, -SPEED]
    elif (KEYS[K_DOWN] or KEYS[K_s]) and DIRECTION[1] == 0:
        DIRECTION = [0, SPEED]
    elif (KEYS[K_RIGHT] or KEYS[K_d]) and DIRECTION[0] == 0: 
        DIRECTION = [SPEED, 0]
    elif (KEYS[K_LEFT] or KEYS[K_a]) and DIRECTION[0] == 0: 
        DIRECTION = [-SPEED, 0]
    
    if obj.right > 1080: 
        obj.right = 30
    elif obj.left < 0:
        obj.left = 1050
    elif obj.bottom > 720:
        obj.bottom = 30
    elif obj.top < 0:
        obj.top = 700

    for el in range( (len(body) - 1), 0, -1): 
        body[el].x = body[el-1].x
        body[el].y = body[el-1].y
    
    obj.move_ip(DIRECTION)



# variables 
head_image, head_rect = load_img('./img/head.png', 400, 300)
apple_image, apple_rect = load_img('./img/apple.png', 200, 200)
body_image, body_rect = load_img('./img/body.png', 370, 300)

snake = [head_rect, body_rect] 

while True: 
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT: 
            pygame.quit()
            exit()
    
    KEYS = pygame.key.get_pressed()
    screen.blit(apple_image, apple_rect)
    screen.blit(head_image, head_rect)
    for el in snake[1:]:
        screen.blit(body_image, el)
    move(head_rect, snake)
    pickup()
    score()

    if game_over():
        text = font.render(f'U LOSER', True, COLOR)
        text_rect = text.get_rect(center=(540,360))
        screen.blit(text, text_rect)
        SPEED = 0

    pygame.display.update()
    FPS.tick(15)