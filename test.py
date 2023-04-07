values = {(((0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 1, 0, 0, 0, 0), (0, 0, 2, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0)), (6, 2, 4, 4)): 89.0, (((0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 1, 0, 0, 0, 0), (0, 0, 2, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0)), (6, 2, 5, 1)): 0.0, (((0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 2, 0, 1, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0)), (5, 3, 6, 2)): 0.0, (((0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 2, 0, 1, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0)), (5, 3, 6, 4)): 0.0}
from GUI.OLD import *
# strat pygame and set up the window
def testwindow(board):
    print(board)
    pygame.init()
    screen = pygame.display.set_mode((top, bottom))
    pygame.display.set_caption("Pygame")
    running = True
    screen.fill((0, 0, 0))
    chessboard(screen)
    # jump = move(screen,moved,next,jump)
    checkers(screen,np.transpose(board))
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()


for eatch in values:
    print(eatch[1])
    print(values[eatch])
    testwindow(eatch[0])