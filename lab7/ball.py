import pygame
import sys

# Инициализация
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Red-Green Ball")

# Параметры мяча
radius = 25
x, y = 300, 300
speed = 20
color = (255, 0, 0)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Движение — без ограничений
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    
    touching_wall = (
        x - radius <= 0 or
        x + radius >= 600 or
        y - radius <= 0 or
        y + radius >= 600
    )

    color = (0, 255, 0) if touching_wall else (255, 0, 0)

    
    x = max(radius, min(600 - radius, x))
    y = max(radius, min(600 - radius, y))

    
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, color, (x, y), radius)
    pygame.display.flip()
    clock.tick(60)
