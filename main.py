import pygame
import sys
import random
import math
from pygame.locals import *

pygame.init()

W_WIDTH = 800
W_HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCORE_VAL = 0
SCORE_POS = [5, 5]

frame_rate = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 20)
game_over_font = pygame.font.Font('freesansbold.ttf', 64)

# player
playerImage = pygame.image.load('data/spaceship.png')
player_pos = [370, 523]
player_speed = [0, 0]

# Invader
invader_picture = pygame.image.load('data/alien.png')
invader_picture = pygame.transform.scale(invader_picture, (70, 50))
invaderImage = []
invader_pos = []
invader_speed = []
no_of_invaders = 8

for i in range(0, no_of_invaders):
    invaderImage.append(invader_picture)
    invader_pos.append([random.randint(64, 737), random.randint(30, 180)])
    invader_speed.append([0.5, 20])

# Glont
# 0 - glontul nu se misca (nu este pe ecran)
# 1 - glontul se misca
bulletImage = pygame.image.load('data/bullet.png')
bullet_pos = [0, 500]
bullet_speed = [0, 3]
bullet_state = 0


# pos_in = pozitiile pe OX si OY ale primului obiect
# pos_out = pozitiile pe OX si OY ale celui de al doilea obiect
def isCollision(pos_in, pos_out):
    distance = math.sqrt((math.pow(pos_in[0] - pos_out[0], 2)) +
                         (math.pow(pos_in[1] - pos_out[1], 2)))
    if distance <= 50:
        return True
    else:
        return False


def show_score(window, pos):
    score = font.render("Points: " + str(SCORE_VAL), True, WHITE)
    window.blit(score, (pos[0], pos[1]))


def game_over(window):
    game_over_text = game_over_font.render("GAME OVER",
                                           True, WHITE)
    window.blit(game_over_text, (190, 250))


def player(window, pos):
    window.blit(playerImage, (pos[0] - 16, pos[1] + 10))


def invader(window, pos, i):
    window.blit(invaderImage[i], (pos[0], pos[1]))


def bullet(window, pos):
    global bullet_state
    window.blit(bulletImage, (pos[0], pos[1]))
    bullet_state = 1


class Game:
    def __init__(self):
        self.window = pygame.display.set_mode((W_WIDTH, W_HEIGHT))
        pygame.display.set_caption("Space Invaders")

    def run(self):
        global bullet_state, SCORE_VAL

        self.window.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_speed[0] = -1.7
                if event.key == pygame.K_RIGHT:
                    player_speed[0] = 1.7
                if event.key == pygame.K_SPACE:
                    if bullet_state == 0:
                        bullet_pos[0] = player_pos[0]
                        bullet(self.window, bullet_pos)
            if event.type == pygame.KEYUP:
                player_speed[0] = 0

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        player_pos[0] += player_speed[0]
        for i in range(0, no_of_invaders):
            invader_pos[i][0] += invader_speed[i][0]
        if bullet_pos[1] <= 0:
            bullet_pos[1] = 600
            bullet_state = 0
        if bullet_state == 1:
            bullet(self.window, bullet_pos)
            bullet_pos[1] -= bullet_speed[1]

        for i in range(0, no_of_invaders):
            if invader_pos[i][1] >= 450:
                if abs(player_pos[0] - invader_pos[i][0]) < 60: 
                    for j in range(no_of_invaders):
                        invader_pos[j][1] = 2000

                    game_over(self.window)
                    break
            # invaderul sa nu iasa din fereastra ci sa se miste in jos
            if invader_pos[i][0] >= 735 or invader_pos[i][0] <= 0:
                invader_speed[i][0] *= -1
                invader_pos[i][1] += invader_speed[i][1]

            collision = isCollision(bullet_pos, invader_pos[i])
            if collision:
                SCORE_VAL += 1
                bullet_pos[1] = 600
                bullet_state = 0
                invader_pos[i][0] = random.randint(64, 736)
                invader_pos[i][1] = random.randint(30, 200)
                invader_speed[i][0] *= -1

            invader(self.window, invader_pos[i], i)

        # limite pentru nava sa nu iasa din fereastra
        if player_pos[0] <= 16:
            player_pos[0] = 16
        elif player_pos[0] >= 750:
            player_pos[0] = 750

        player(self.window, player_pos)
        show_score(self.window, SCORE_POS)

        pygame.display.update()

        frame_rate.tick(60)


def main():
    battle = Game()
    while True:
        battle.run()


main()
