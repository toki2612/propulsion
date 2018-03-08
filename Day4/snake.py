# snake game

import pygame
import sys
import random

pygame.init()
width, height = 400, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('MyGame')

red = pygame.Color(255, 0, 0)
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)


def text(message, color, x_coord, y_coord, smth=None):
    fontObj = pygame.font.SysFont('arial', 20)
    if smth is None:
        textSurfaceObj = fontObj.render(f'{message}', True, color)
    else:
        textSurfaceObj = fontObj.render(f'{message} {smth}', True, color)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (x_coord, y_coord)
    screen.blit(textSurfaceObj, textRectObj)


screen.fill(white)
FPS = 10
x = width / 2
y = height / 2
step = 10
snake_body = [[x, y]]  # list of lists
body_part_size = 10
user_score = 0
snake_speed = 0
lives = 3

fpsClock = pygame.time.Clock()

state_direction = ""
prev_direction = ""

food_x = random.randint(0, width / step) * step
food_y = random.randint(0, height / step) * step
print(food_x, food_y)


def draw_food(x, y, size):
    pygame.draw.rect(screen, red, pygame.Rect(x, y, size, size))


def game_over():
    global lives, snake_body, x, y, state_direction, user_score
    # print([xc, yc])
    # print(snake_body)

    if x > width or x < 0 or y > height or y < 0 or [x, y] in snake_body[1:]:
        x, y = width / 2, height / 2
        state_direction = ""
        user_score = 0
        if lives > 0:
            lives -= 1
            print(f"Lives left: {lives}")
            snake_body = [[x, y]]

    return lives == 0


def eat_food(body):
    global user_score
    global food_x, food_y
    last = body[-1]
    if body[0] == [food_x, food_y]:
        user_score += 1
        body.append(last)
        food_x = random.randint(step, (width - step)/ step) * step
        food_y = random.randint(step, (height - step)/ step) * step


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            prev_direction = state_direction
            if event.key == pygame.K_LEFT:
                if prev_direction == "right":
                    state_direction = "right"
                else:
                    state_direction = "left"
            if event.key == pygame.K_RIGHT:
                if prev_direction == "left":
                    state_direction = "left"
                else:
                    state_direction = "right"
            if event.key == pygame.K_UP:
                if prev_direction == "down":
                    state_direction = "down"
                else:
                    state_direction = "up"
            if event.key == pygame.K_DOWN:
                if prev_direction == "up":
                    state_direction = "up"
                else:
                    state_direction = "down"

    if state_direction == "left":
        x -= step
    if state_direction == "right":
        x += step
    if state_direction == "up":
        y -= step
    if state_direction == "down":
        y += step

    snake_body.pop()
    snake_body.insert(0, [x, y])

    screen.fill(white)
    draw_food(food_x, food_y, body_part_size)

    if game_over():
        text("Game over!!!", red, width / 2, height / 2)
    else:
        text("Score: ", black, 50, 20, user_score)
        text("Speed: ", black, 50, 40, snake_speed)
        text("Lives: ", red, 50, 60, lives)

    for part in snake_body:
        # print(x, y)
        pygame.draw.rect(screen, black, pygame.Rect(part[0], part[1],
                                                    body_part_size, body_part_size))
    eat_food(snake_body)
    pygame.display.update()
    fpsClock.tick(FPS)
