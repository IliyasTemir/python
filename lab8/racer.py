import pygame
import random


pygame.init()

#loop variables

screen = pygame.display.set_mode((800,600))

running = True


#in game variables

targets = ((2,3,5),(7,11,13),(17,19,23),(29,31,37),(41,43,47),(53,59,61),(67,71,73),(79,83,89),(97,101,103))

level = 1

precedence = {
    "*":2,
    "/":2,
    "+":1,
    "-":1
}

dice = []

keys = "123456+-*/"

for die in range(1,level*2+2):
    dice.append(random.randrange(1,7))


text = ""

def count_check(text,rolls):
    text_count = {
        "1":0,
        "2":0,
        "3":0,
        "4":0,
        "5":0,
        "6":0,
        "other":0
    }

    rolls_count = {
        "1":0,
        "2":0,
        "3":0,
        "4":0,
        "5":0,
        "6":0,
        "other":0
    }

    tokens = text.split()

    for token in tokens:
        if token in precedence:
            continue
        elif token in text_count:
            text_count[token]+=1
        else:
            text_count["other"]+=1

    for die in rolls:
        if str(die) in rolls_count:
            rolls_count[str(die)]+=1

    return text_count == rolls_count

def game_over(font,size,color):
    global running
    screen.fill((0,0,0))
    font = pygame.font.SysFont(font, size)
    render = font.render("Game Over, your final level was: " + str(level),True,color)    

    screen.blit(render,(400-render.get_width()//2,300-render.get_height()//2))
    pygame.display.update()

    pygame.time.delay(4000)
    running = False

def shunt_yard_eval(text):
    tokens = text.split()
    polish = []
    ops = []

    for token in tokens:
        if token in precedence:
            if ops:
                while precedence[token]<=precedence[ops[-1]]:
                    op = ops.pop()
                    polish.append(op)
                    if not ops:
                        break
            ops.append(token)
        else:
            polish.append(token)
    
    while ops:
        polish.append(ops.pop())

    result = []
    for tok in polish:
        if tok not in precedence:
            result.append(tok)
        else:
            if tok == "*":
                right = float(result.pop())
                left = float(result.pop())
                result.append(left*right)
            if tok == "/":
                right = float(result.pop())
                left = float(result.pop())
                result.append(left/right)
            if tok == "+":
                right = float(result.pop())
                left = float(result.pop())
                result.append(left+right)
            if tok == "-":
                right = float(result.pop())
                left = float(result.pop())
                result.append(left-right)
    return result




while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.unicode in keys:
                text+=event.unicode+" "
            if event.key == pygame.K_RETURN:
                if not count_check(text,dice):
                    game_over("times new roman",30,(255,0,0))
                if shunt_yard_eval(text)[0] in targets[level-1]:
                    level+=1
                    #update stuff
                    print("got here")
                else:
                    game_over("times new roman",30,(255,0,0))
                    print("got there")    
                

    screen.fill((0,0,0))
    #target numbers are ...

    font_prompt = pygame.font.SysFont("times new roman", 20)
    render_prompt = font_prompt.render("Welcome to level "+str(level)+". The target numbers are:"+str(targets[level-1]),True,(255,255,255))    

    screen.blit(render_prompt,(0,0))

    font_dice = pygame.font.SysFont("times new roman", 20)
    render_dice = font_dice.render("The rolled dice are"+str(dice),True,(255,255,255))    

    screen.blit(render_dice,(0,30))

    
    font_input = pygame.font.SysFont("times new roman", 20)
    render_input = font_input.render(text,True,(255,255,255))    

    screen.blit(render_input,(0,60))

    pygame.display.flip()



pygame.quit()
 