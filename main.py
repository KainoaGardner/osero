import pygame
from settings import *
from display import display
from board import *
pygame.init()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mosPos = pygame.mouse.get_pos()
                if event.button == 1:
                    if MARGINSIZE < mosPos[0] < WIDTH - MARGINSIZE and MARGINSIZE < mosPos[1] < HEIGHT - MARGINSIZE:
                        tile = ((mosPos[0] - MARGINSIZE) // TILESIZE, (mosPos[1] - MARGINSIZE) // TILESIZE)
                        board.playPiece(tile)




        display()

    pygame.quit()

main()