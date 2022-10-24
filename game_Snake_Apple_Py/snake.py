import pygame
import random
from pygame.locals import *

WINDOW_SIZE = (600, 600)
pixel_size = 20
cabeca_r = pygame.image.load(r'game\img\cabeca_r.png')
rabo_r = pygame.image.load(r'game\img\tail_r.png')
passaro_r = pygame.image.load(r'game\img\apple_25px.png')
img_grama = pygame.image.load(r'game\img\grama.jpg')
angle = 0
points = 0


def collision(posi1, posi2):
    # print(f'Maçã: {posi1} x Cabeça: {posi2}')
    return posi1 == posi2


def limit_size(pos):
    if 0 <= pos[0] < WINDOW_SIZE[0] and 0 <= pos[1] < WINDOW_SIZE[1]:
        return False
    else:
        return True


def random_apple_position():
    x = random.randint(0, WINDOW_SIZE[0])
    y = random.randint(0, WINDOW_SIZE[1])
    x = x // pixel_size * pixel_size
    y = y // pixel_size * pixel_size
    return x, y


pygame.init()


screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Snake')

snake_pont = [(440, 260), (460, 260), (480, 260)]
snake_direction = K_LEFT


apple_surface = pygame.Surface((pixel_size, pixel_size))
apple_pos = random_apple_position()


def start_reset():
    global snake_pont
    global apple_pos
    global snake_direction
    global angle
    global points

    snake_pont = [(440, 60), (460, 60), (480, 60)]
    snake_direction = K_LEFT
    apple_pos = random_apple_position()
    angle = 0
    points = 0

    pygame.time.wait(3000)


while True:

    pygame.time.Clock().tick(12)

    screen.blit(img_grama, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key in [K_UP, K_DOWN, K_RIGHT, K_LEFT]:
                if snake_direction == K_RIGHT and event.key == K_LEFT or \
                        snake_direction == K_LEFT and event.key == K_RIGHT:
                    continue
                elif snake_direction == K_UP and event.key == K_DOWN or \
                        snake_direction == K_DOWN and event.key == K_UP:
                    continue
                else:
                    snake_direction = event.key

    if collision(apple_pos, snake_pont[0]):
        snake_pont.append((-20, -20))
        apple_pos = random_apple_position()
        points += 1

    for pos in snake_pont:
        #screen.blit(rabo_r, pos)
        screen.blit(pygame.transform.rotate(
            rabo_r, angle=angle), (pos))

    for corpo in range(len(snake_pont)-1, 0, -1):
        if snake_pont[0] == snake_pont[corpo]:
            start_reset()
            snake_pont[corpo] = snake_pont[corpo+1]

        snake_pont[corpo] = snake_pont[corpo-1]

    if limit_size(snake_pont[0]):
        start_reset()

    if snake_direction == K_UP:
        snake_pont[0] = (snake_pont[0][0], snake_pont[0][1] - pixel_size)
        angle = 270

    elif snake_direction == K_DOWN:
        snake_pont[0] = (snake_pont[0][0], snake_pont[0][1] + pixel_size)
        angle = 90

    elif snake_direction == K_RIGHT:
        snake_pont[0] = (snake_pont[0][0] + pixel_size, snake_pont[0][1])
        angle = 180

    elif snake_direction == K_LEFT:
        snake_pont[0] = (snake_pont[0][0] - pixel_size, snake_pont[0][1])
        angle = 0

    font = pygame.font.SysFont(None, 34)
    texto = font.render(f'Score: {points}', True, 'Red')
    screen.blit(texto, (20, 20))

    screen.blit(pygame.transform.rotate(
        cabeca_r, angle=angle), (snake_pont[0]))

    screen.blit(rabo_r, (snake_pont[-1]))

    screen.blit(passaro_r, (apple_pos))

    pygame.display.update()
