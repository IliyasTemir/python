import pygame
import random
import time


pygame.init()


WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
cols = WIDTH // CELL_SIZE
rows = HEIGHT // CELL_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game with Levels")


WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)


clock = pygame.time.Clock()
initial_speed = 10


font = pygame.font.SysFont("Arial", 24)


snake = [(5, 5)]
direction = (1, 0)


def generate_food():
    while True:
        pos = (random.randint(0, cols - 1), random.randint(0, rows - 1))
        if pos not in snake:
            weight = random.randint(1, 3)  
            timer = random.randint(5, 10)  
            return pos, weight, time.time(), timer  


food, food_weight, food_start_time, food_timer = generate_food()

score = 0
level = 1
speed = initial_speed


eat_sound = pygame.mixer.Sound("eat.wav")


running = True
while running:
    clock.tick(speed)

    
    if time.time() - food_start_time > food_timer:
        food, food_weight, food_start_time, food_timer = generate_food() 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, 1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN and direction != (0, -1):
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and direction != (1, 0):
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                direction = (1, 0)

    
    head = snake[-1]
    new_head = (head[0] + direction[0], head[1] + direction[1])

    
    if new_head[0] < 0 or new_head[0] >= cols or new_head[1] < 0 or new_head[1] >= rows:
        print("Game Over: Hit wall!")
        running = False
        continue

   
    if new_head in snake:
        print("Game Over: Hit yoursef!")
        running = False
        continue

    snake.append(new_head)

   
    if new_head == food:
        score += food_weight  
        eat_sound.play()  

        
        food, food_weight, food_start_time, food_timer = generate_food()

        
        if score % 4 == 0:
            level += 1
            speed += 2 

    else:
        snake.pop(0)

    
    screen.fill(BLACK)

    
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    
    pygame.draw.rect(screen, RED, (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

 
    score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()



