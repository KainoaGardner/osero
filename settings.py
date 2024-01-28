import pygame
pygame.init()

TILESIZE = 100
MARGINSIZE = TILESIZE

WIDTH = MARGINSIZE * 2 + TILESIZE * 8
HEIGHT = MARGINSIZE * 2 + TILESIZE * 8
FPS = 60

screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

font = pygame.font.SysFont("Calibri",50,True)
toumei = pygame.surface.Surface((TILESIZE,TILESIZE))
toumei.fill("#27ae60")
toumei.set_alpha(150)
