# pygame
import numpy as np
import pygame
from bot.can_moove import *
from bot.config import *
from Kamera.preproces import *
from Main_cam import *
import cv2
import time


def window(board):

    pygame.init()
    screen = pygame.display.set_mode((top, bottom))
    pygame.display.set_caption("Pygame")
    running = True
    figure = "w"
    moved = 0
    jump = []
    next = False

    zero_board = np.zeros((8, 8), np.uint8)

    # camera setup
    cap = load_webcam()
    first = True
    rows, black_rows = load_board(cap)
    ggg = True
    origional_board = board.copy()
    start = True
    while ggg:
        show(cap)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            get_color(cap, rows)
            ggg = False
    while running:
        while start:
            board= get_board(cap, rows, black_rows)
            if np.array_equal(origional_board, board):
                start = False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    figure = "b"
                    print("white")
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        chessboard(screen)
        # jump = move(screen,moved,next,jump)
        checkers(screen,np.transpose(board))
        pygame.display.flip()
        if figure == "b":
            board, next, moved = run(board, figure)
            board_temp = get_board(cap, rows, black_rows)
            while not np.array_equal(board_temp, board):
                board_temp = get_board(cap, rows, black_rows)
                screen.fill((0, 0, 0))
                chessboard(screen)
                checkers(screen, np.transpose(board))
                pygame.display.flip()
            print(board)
            print(next)
        else:
            while True:
                board_temp = get_board(cap, rows, black_rows)
                print(board_temp)
                if not np.array_equal(board_temp, zero_board):
                    if not np.array_equal(board_temp, board):
                        print(board)
                        print(next)
                        next = False
                        # weit one second
                        time.sleep(1)
                        board = get_board(cap, rows, black_rows)

                        break
                screen.fill((0, 0, 0))
                chessboard(screen)
                checkers(screen, np.transpose(board))
                pygame.display.flip()


        if next == False:
            if figure == "w":
                figure = "b"
            else:
                figure = "w"

    pygame.quit()

top = 800
bottom = 800


# load img/queen.png image
queenB = pygame.image.load("../Img/queenB.png")
queenW = pygame.image.load("../Img/queenW.png")
W = pygame.image.load("../Img/W.png")
B = pygame.image.load("../Img/B.png")
# set image size
queenB = pygame.transform.scale(queenB, (50, 40))
queenW = pygame.transform.scale(queenW, (50, 40))
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
                # pygame.draw.circle(screen, (144, 84, 47), (x+50, y+50), 35)
                screen.blit(W, (x+10, y+10))
            elif bord[x//100][y//100] == 2:
                # pygame.draw.circle(screen, (0, 0, 0), (x+50, y+50), 35)
                screen.blit(B, (x+10, y+10))

            elif bord[x//100][y//100] == 3:
                pygame.draw.circle(screen, (144, 84, 47), (x+50, y+50), 35)
                screen.blit(queenB, (x+25, y+30))

            elif bord[x//100][y//100] == 4:
                pygame.draw.circle(screen, (0, 0, 0), (x+50, y+50), 35)
                screen.blit(queenW, (x+25, y+30))

window(board_start)