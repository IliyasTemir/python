import pygame
import math


pygame.init()


WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Draw Shapes")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


current_color = RED


clock = pygame.time.Clock()


def draw_square(screen, color, position, size):
    rect = pygame.Rect(position[0], position[1], size, size)
    pygame.draw.rect(screen, color, rect)


def draw_right_triangle(screen, color, position, base, height):
    p1 = position
    p2 = (position[0] + base, position[1])  
    p3 = (position[0], position[1] - height) 
    points = [p1, p2, p3]
    pygame.draw.polygon(screen, color, points)


def draw_equilateral_triangle(screen, color, position, size):
    height = math.sqrt(3) * size / 2
    p1 = position  
    p2 = (position[0] + size, position[1]) 
    p3 = (position[0] + size / 2, position[1] - height) 
    points = [p1, p2, p3]
    pygame.draw.polygon(screen, color, points)


def draw_rhombus(screen, color, position, size):
    half_diag = size / math.sqrt(2)
    p1 = (position[0], position[1] - half_diag)  
    p2 = (position[0] + half_diag, position[1])  
    p3 = (position[0], position[1] + half_diag)  
    p4 = (position[0] - half_diag, position[1])  
    points = [p1, p2, p3, p4]
    pygame.draw.polygon(screen, color, points)


def main():
    global current_color
    running = True
    mode = "square"  

    while running:
        screen.fill(BLACK)  

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:  
                    mode = "square"
                elif event.key == pygame.K_t:  
                    mode = "right_triangle"
                elif event.key == pygame.K_e:  
                    mode = "equilateral_triangl"
                elif event.key == pygame.K_r:  
                    mode = "rhombus"
                elif event.key == pygame.K_y:  
                    current_color = YELLOW
                elif event.key == pygame.K_b: 
                    current_color = BLUE
                elif event.key == pygame.K_w:  
                    current_color = WHITE
                elif event.key == pygame.K_d: 
                    current_color = RED
                elif event.key == pygame.K_g:  
                    current_color = GREEN

        
        position = (200, 200)  
        size = 100  

        if mode == "square":
            draw_square(screen, current_color, position, size)
        elif mode == "right_triangle":
            draw_right_triangle(screen, current_color, position, size, size)
        elif mode == "equilateral_triangle":
            draw_equilateral_triangle(screen, current_color, position, size)
        elif mode == "rhombus":
            draw_rhombus(screen, current_color, position, size)

        pygame.display.flip() 

        clock.tick(60)  

    pygame.quit()


main()

