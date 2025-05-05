import pygame

pygame.init()

WIDTH, HEIGHT = 700, 500
BLACK = [0, 0, 0]
fps = 30
screen = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill(BLACK)

    pygame.display.flip()
    clock.tick(fps)

