import pygame
import time
import random
import copy
pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((640,640))

#Snake body
snake_body = [[0,0]]
snake_x_change = 0
snake_y_change = 0
snake_head = snake_body[0]
snake_body_prev = [[0,0]]
def snake():
    for i in range(len(snake_body)):
        pygame.draw.rect(screen, (255,255,255), (*snake_body[i], 64,64), 3)

#Food

food_x = random.randint(0,9)*64
food_y = random.randint(0,9)*64
mryga = 0
def food(x, y, t):
    if t % 5 != 0:
        pygame.draw.rect(screen, (255,255,255), (x,y, 64, 64),0)
        t = False
    else:
        t = True
growth = False  

#Score
myfont = pygame.font.SysFont('Comic Sans MS', 30)
score = 0


#Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if len(snake_body) == 1:
                if event.key == pygame.K_w:
                    snake_x_change = 0
                    snake_y_change = -64
                    
                if event.key == pygame.K_s:
                    snake_x_change = 0
                    snake_y_change = 64
                    
                if event.key == pygame.K_a:
                    snake_y_change = 0
                    snake_x_change = -64
                  
                if event.key == pygame.K_d:
                    snake_y_change = 0
                    snake_x_change = 64
                    
            else:
                if event.key == pygame.K_w:
                    if snake_body[1][1] != snake_body[0][1] - 64:
                        snake_x_change = 0
                        snake_y_change = -64
                        
                if event.key == pygame.K_s:
                    if snake_body[1][1] != snake_body[0][1] + 64:
                        snake_x_change = 0
                        snake_y_change = 64
                        
                if event.key == pygame.K_a:
                    if snake_body[1][0] != snake_body[0][0] - 64:
                        snake_y_change = 0
                        snake_x_change = -64
                      
                if event.key == pygame.K_d:
                    if snake_body[1][0] != snake_body[0][0] + 64:    
                        snake_y_change = 0
                        snake_x_change = 64
    time.sleep(0.2)    
    screen.fill((0,0,0))
    for i in range(len(snake_body)):
        snake_body_prev[i] = copy.copy(snake_body[i])  #snake_body_prev == [[0,0]]

    snake_head[0] += snake_x_change
    snake_head[1] += snake_y_change

    j = len(snake_body) - 1
    while j > 0:
        snake_body[j] = copy.copy(snake_body_prev[j - 1])
        j -= 1

    if growth == True:
        snake_body.append(copy.copy(snake_body_prev[len(snake_body) - 1]))
        snake_body_prev.append([0,0])
        growth = False

    if snake_head[0] == -64:
        snake_head[0] = 576
    elif snake_head[0] == 640:
        snake_head[0] = 0
    if snake_head[1] == -64:
        snake_head[1] = 576
    elif snake_head[1] == 640:
        snake_head[1] = 0

    if [food_x, food_y] == snake_head:
        flag = True
        while flag:
            potential = [random.randint(0,9)*64,random.randint(0,9)*64]
            if potential in snake_body:
                continue
            food_x = potential[0]
            food_y = potential[1]
            growth = True
            score += 1
            break

    snake()
    food(food_x, food_y, mryga)
    if mryga != 5:
        mryga += 1
    else:
        mryga = 0

    if snake_head in snake_body[1:]:
        running = False
    screen.blit(myfont.render(str(score), False, (250, 250, 250)),(600,0))
    pygame.display.update()
    
    