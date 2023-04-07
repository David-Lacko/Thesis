# pygame
import numpy as np
import pygame
from bot.can_moove import *
from bot.config import *
from Kamera.functions import *
from Main_cam import *
import cv2
from bot.min_max import *
import time


def window(board):
    board = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 4, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 2], [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 2, 0, 0], [0, 0, 0, 0, 0, 0, 2, 0], [0, 0, 0, 0, 0, 2, 0, 0]]
    pygame.init()
    screen = pygame.display.set_mode((top, bottom))
    pygame.display.set_caption("Pygame")
    running = True
    figure = "w"
    moved = 0
    jump = []
    next = False
    zero_board = np.zeros((8, 8), np.uint8)


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        chessboard(screen)
        # jump = move(screen,moved,next,jump)
        checkers(screen,np.transpose(board))
        pygame.display.flip()
        if figure == "b":

            score, moved = min_max(copy.deepcopy(board), figure, True, 3, "deterministic")
            if moved == None:
                board = False
            else:
                board = make_move(board, moved)
        else:
            score, moved = min_max(copy.deepcopy(board), figure, True, 5, "deterministic")
            if moved == None:
                board = False
            else:
                board = make_move(board, moved)
        if board == False:
            # restart game
            if figure == "w":
                print("AI win")
            else:
                print("AI lose")
            figure = "w"
            running = False
        if figure == "w":
            figure = "b"
        else:
            figure = "w"
        # time.sleep(1)
    pygame.quit()

top = 800
bottom = 800


# load img/queen.png image
# queenB = pygame.image.load("../Img/BQ.png")
# queenW = pygame.image.load("../Img/WQ.png")
# W = pygame.image.load("../Img/W.png")
# B = pygame.image.load("../Img/B.png")
queenB = pygame.image.load("./Img/BQ.png")
queenW = pygame.image.load("./Img/WQ.png")
W = pygame.image.load("./Img/W.png")
B = pygame.image.load("./Img/B.png")
# set image size
queenB = pygame.transform.scale(queenB, (80, 80))
queenW = pygame.transform.scale(queenW, (80, 80))
W = pygame.transform.scale(W, (80, 80))
B = pygame.transform.scale(B, (80, 80))

#drow move on board
def move(screen,moved,next,jump):
    if moved != 0:
        jump.append(moved)
        for i in range(len(jump)):
            pygame.draw.circle(screen, (255, 0, 0), (int(jump[i][0]) * 100 + 50, int(jump[i][1]) * 100 + 50), 20)
    if not next:
        jump = []
    return jump





def chessboard(screen):
    for x in range(0, top, 100):
        for y in range(0, bottom, 100):
            if (x + y) % 200 == 0:
                pygame.draw.rect(screen, (255, 255, 255), (x, y, 100, 100))
            pygame.draw.rect(screen, (100, 100, 100), (x, y, 100, 100), 1)

#drow checkers
def checkers(screen,bord):
    for x in range(0, top, 100):
        for y in range(0, bottom, 100):
            if bord[x//100][y//100] == 1:
                screen.blit(W, (x+10, y+10))
            elif bord[x//100][y//100] == 2:
                screen.blit(B, (x+10, y+10))
            elif bord[x//100][y//100] == 3:
                screen.blit(queenB, (x+25, y+30))

            elif bord[x//100][y//100] == 4:
                screen.blit(queenW, (x+25, y+30))
            elif bord[x//100][y//100] == 5:
                pygame.draw.circle(screen, (255, 0, 0), (x+50, y+50), 10)
if __name__ == '__main__':
    window(board_start)

def move():
    # bord = copy.deepcopy(test_board)
    testboard = [[0, 0, 0, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 4, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 1, 0], [0, 0, 0, 2, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 2, 0], [0, 2, 0, 2, 0, 2, 0, 2]]


    bord = testboard
    pygame.init()
    screen = pygame.display.set_mode((top, bottom))
    pygame.display.set_caption("Pygame")
    running = True
    figure = "b"
    moves = need_move(bord, figure)
    print(moves)
    while running:
        # select random move
        bord = copy.deepcopy(testboard)
        # run(bord, figure)
        for move in moves:
            if len(move) > 4:
                x2 = int(move[-2])
                y2 = int(move[-1])
                bord[x2][y2] = 5
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        chessboard(screen)
        checkers(screen, np.transpose(bord))
        pygame.display.flip()
        time.sleep(2)

# move()
