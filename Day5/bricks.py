# bricks game

import pygame
import sys
import random
import math

# from .ball import *

# game colors
grey = pygame.Color(178, 178, 178)
red = pygame.Color(244, 27, 63)
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)
green = pygame.Color(38, 156, 100)
blue = pygame.Color(35, 110, 255)
lila = pygame.Color(230, 0, 255)
cyan = pygame.Color(21, 178, 211)
orange = pygame.Color(255, 100, 0)
yellow = pygame.Color(255, 215, 0)

brick_colors = [red, green, blue, lila, cyan, orange]


# print text on the screen (optionally with scores, lives etc.)
def text(message, color, x_coord, y_coord, font_size=20, smth=None):
    fontObj = pygame.font.SysFont('arial', font_size)
    if smth is None:
        textSurfaceObj = fontObj.render(f'{message}', True, color)
    else:
        textSurfaceObj = fontObj.render(f'{message} {smth}', True, color)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (x_coord, y_coord)
    game.screen.blit(textSurfaceObj, textRectObj)


bricks_vert = 7
bricks_horiz = 14
brick_width = 40
brick_height = 20

fpsClock = pygame.time.Clock()

states = ['pause', 'play', 'resume', 'reset', 'game_over']


class Game:
    ball = None
    ship = None
    FPS = 90
    lives = 1
    user_score = 0
    state = 'start'
    ball_lost = False
    logs = True
    check_line = 0
    ball_velocity = 5

    def __init__(self, width, height):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Arkanoid')
        self.bricks = []

    def init_bricks(self):
        for i in range(1, bricks_horiz + 1):
            for j in range(1, bricks_vert + 1):
                hits = random.randint(1, 2)
                if hits == 1:
                    color = green
                elif hits == 2:
                    color = red
                new_brick = Brick(i * (brick_width + 12) - 10, j * (brick_height + 10) - 10, color, hits)
                new_brick.id = len(self.bricks)
                # print(new_brick.x, new_brick.y)
                self.bricks.append(new_brick)
        self.check_line = self.bricks[-1].y + 50
        return self.bricks

    def update_bricks(self, ball):
        # print("next iteration")
        if ball.y < self.check_line:
            for brick in self.bricks:
                collided_side = brick.collided(ball)
                if collided_side:
                    if collided_side in ['top', 'bottom']:
                        ball.stepy = - ball.stepy
                    elif collided_side in ['left', 'right']:
                        ball.stepx = - ball.stepx
                    elif collided_side in ['inside', 'corner']:
                        ball.stepx = - ball.stepx
                        ball.stepy = - ball.stepy
                    brick.color = green
                    brick.hits_to_beat -= 1
                    self.user_score += 1

                    if self.logs:
                        print(f'Brick #{brick.id} was collided from {collided_side} side')
                        print(f'Ball new speed is ({ball.stepx}, {ball.stepy})')
                    if brick.hits_to_beat == 0:
                        self.bricks.remove(brick)

    def draw_bricks(self):
        for brick in self.bricks:
            pygame.draw.rect(self.screen, grey, pygame.Rect(brick.x, brick.y, brick.bwidth + 3, brick.bheight + 3))
            pygame.draw.rect(self.screen, brick.color, pygame.Rect(brick.x, brick.y, brick.bwidth, brick.bheight))
            # text(brick.id, white, brick.x + 20, brick.y + 10)

    def reset_game(self):
        self.state = 'start'
        self.ship.start_position()
        self.ball.start_position()
        self.lives = 3
        self.user_score = 0
        self.init_bricks()

    def handle_input(self):

        # ship movement
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_LEFT]:
            self.ship.direction = "left"
        if keys_pressed[pygame.K_RIGHT]:
            self.ship.direction = "right"

        # changing states
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.state == 'running':
                        self.state = 'pause'
                    elif self.state == 'start':
                        self.state = 'running'
                        self.ball.stepx, self.ball.stepy = -self.ball_velocity, self.ball_velocity
                    elif self.state == 'pause':
                        self.state = 'running'
                if event.key == pygame.K_r:
                    if self.state in ['start', 'running', 'pause']:
                        self.reset_game()
                if event.key == pygame.K_y:
                    if self.state == 'gameover':
                        self.reset_game()
                elif event.key == pygame.K_n:
                    pygame.quit()
                    sys.exit()

    def run(self):
        self.ship = Ship(0.5 * (self.width - 100), self.height - 40, yellow)
        self.ball = Ball(int(self.width / 2), self.height - 2 * self.ship.sheight - 10, 10, 0, 0)
        self.bricks = self.init_bricks()
        start_time = pygame.time.get_ticks()

        while True:
            self.handle_input()
            time_passed = (pygame.time.get_ticks() - start_time) / 1000
            #print(int(time_passed) % 10)
            if self.state == 'gameover':
                text("Game over...", grey, self.width / 2, 50 + self.height / 2, font_size=40)
                text("Do you want to play again?(y/n)", grey, self.width / 2, 100 + self.height / 2, font_size=40)
            else:
                self.screen.fill(black)

                # controls
                text("Controls: Arrow Keys ", grey, self.width - 100, self.height - 60)
                text("Pause/Resume: Space", grey, self.width - 100, self.height - 40)
                text("Reset: R", grey, self.width - 100, self.height - 20)

                # scores and lives
                text("Score: ", grey, 50, self.height - 40, 20, self.user_score)
                text("Lives: ", red, 50, self.height - 20, 20, self.lives)

                # change_state('pause')
                if self.state == 'running':
                    self.ship.update()
                    self.ball.update()
                    self.ball.collide_with_ship(self.ship)
                    self.update_bricks(self.ball)
                elif self.state == 'start':
                    text("Hit Space to start", grey, self.width / 2, 50 + self.height / 2)
                    self.ship.start_position()
                    self.ball.start_position()
                self.ship.draw()
                self.ball.draw()
                self.draw_bricks()
            pygame.display.update()
            fpsClock.tick(self.FPS)


class Brick:
    def __init__(self, x, y, color, hits_to_beat):
        self.x = x
        self.y = y
        self.bwidth = 40
        self.bheight = 20
        self.color = color
        self.hits_to_beat = hits_to_beat
        self.collide = False
        self.id = None

    def collided(self, ball):
        # check if inside brick:
        brick_side = ''
        brick_rect = pygame.Rect(self.x, self.y, self.bwidth, self.bheight)
        brick_rect_top = pygame.Rect(self.x, self.y - ball.radius, self.bwidth, ball.radius)
        brick_rect_bottom = pygame.Rect(self.x, self.y + self.bheight, self.bwidth, ball.radius)
        brick_rect_right = pygame.Rect(self.x + self.bwidth, self.y, ball.radius, self.bheight)
        brick_rect_left = pygame.Rect(self.x - ball.radius, self.y, ball.radius, self.bheight)
        corners = [(self.x, self.y), (self.x + self.bwidth, self.y), (self.x, self.y + self.bheight), (self.x + self.bwidth, self.y + self.bheight)]
        for corner in corners:
            if math.sqrt((corner[0] - ball.x) ** 2 + (corner[1] - ball.y) ** 2) < ball.radius:
                brick_side = 'corner'
        if brick_rect.collidepoint(ball.x, ball.y):
            brick_side = 'inside'
        elif brick_rect_top.collidepoint(ball.x, ball.y):
            brick_side = 'top'
        elif brick_rect_bottom.collidepoint(ball.x, ball.y):
            brick_side = 'bottom'
        elif brick_rect_right.collidepoint(ball.x, ball.y):
            brick_side = 'right'
        elif brick_rect_left.collidepoint(ball.x, ball.y):
            brick_side = 'left'

        return brick_side


class Ball:
    def __init__(self, x, y, radius, stepx, stepy):
        self.x = x
        self.y = y
        self.radius = radius
        self.direction = [5, 5]
        self.stepx = stepx
        self.stepy = stepy
        # self.direction = direction #tuple

    def update(self):
        self.x -= self.stepx
        self.y -= self.stepy
        if self.x - self.radius < 0 or self.x + self.radius > game.width:
            self.stepx = -self.stepx
        if self.y - self.radius < 0:
            self.stepy = -self.stepy
        if self.y > game.height:
            game.ball_lost = True
            game.lives -= 1
            self.start_position()
            game.state = 'start'
            if game.lives == 0:
                game.state = 'gameover'

    def draw(self):
        pygame.draw.circle(game.screen, blue, (int(self.x), int(self.y)), self.radius)
        pygame.draw.circle(game.screen, white, (int(self.x) + 3, int(self.y) - 2), self.radius - 8)

    def start_position(self):
        self.x = int(game.width / 2)
        self.y = game.height - 2 * 20 - 10
        self.stepx, self.stepy = 0, 0
        game.ball_lost = False

    def collide_with_ship(self, ship):
        if self.y + self.radius == ship.y and ship.x < self.x < ship.x + ship.swidth:
            self.stepy = -self.stepy


class Ship:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.swidth = 100
        self.sheight = 15
        self.direction = ""
        self.color = color
        self.step = 10

    def update(self):
        if self.direction == "left":
            self.x -= self.step
            self.direction = ""
        if self.direction == "right":
            self.x += self.step
            self.direction = ""

        if self.x + self.swidth > game.width:
            self.x = game.width - self.swidth
        if self.x < 0:
            self.x = 0

    def draw(self):
        pygame.draw.rect(game.screen, self.color, pygame.Rect(self.x, self.y, self.swidth, self.sheight))

    def start_position(self):
        self.x = 0.5 * (game.width - 100)
        self.y = game.height - 40
        self.direction = ""


if __name__ == "__main__":
    game = Game(800, 600)
    game.run()
