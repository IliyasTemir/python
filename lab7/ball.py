import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Red Ball Control")

radius = 25
x = 300
y = 300
speed = 20

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x - radius - speed >= 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x + radius + speed <= 600:
        x += speed
    if keys[pygame.K_UP] and y - radius - speed >= 0:
        y -= speed
    if keys[pygame.K_DOWN] and y + radius + speed <= 600:
        y += speed

    screen.fill((255, 255, 255)) 
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius) 
    pygame.display.flip()
    clock.tick(60)
