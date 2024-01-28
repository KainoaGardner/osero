from settings import *
from board import *

def display():
    screen.fill("#c19a6b")
    board.update()
    pygame.display.update()
    clock.tick(FPS)