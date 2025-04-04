import pygame
import sys
from datetime import datetime

# --- Настройки экрана ---
WIDTH, HEIGHT = 1000, 800
CENTER = (WIDTH // 2, HEIGHT // 2)

# --- Инициализация Pygame ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")
clock = pygame.time.Clock()

# --- Загрузка изображений ---
# Убедись, что все файлы в одной папке с этим скриптом
body = pygame.image.load("mickey_body.png").convert_alpha()
left_hand = pygame.image.load("left_hand.png").convert_alpha()
right_hand = pygame.image.load("right_hand.png").convert_alpha()

# --- Функция вращения изображения вокруг центра ---
def rotate_image(image, angle, pivot):
    rotated = pygame.transform.rotate(image, -angle)  # -angle = по часовой
    rect = rotated.get_rect(center=pivot)
    return rotated, rect

# --- Главный цикл ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Получаем текущее время
    now = datetime.now()
    sec_angle = now.second * 6      # 360 / 60
    min_angle = now.minute * 6

    # --- Отрисовка ---
    screen.fill((255, 255, 255))  # белый фон

    # Тело
    body_rect = body.get_rect(center=CENTER)
    screen.blit(body, body_rect)

    # Левая рука (секунды)
    left_rotated, left_rect = rotate_image(left_hand, sec_angle, CENTER)
    screen.blit(left_rotated, left_rect)

    # Правая рука (минуты)
    right_rotated, right_rect = rotate_image(right_hand, min_angle, CENTER)
    screen.blit(right_rotated, right_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
