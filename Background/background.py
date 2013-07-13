import pygame
from common import  *

def init():
    background = pygame.Surface([SCREEN_WIDTH, SCREEN_HEIGHT])
    return background

def draw_corner(background):
    length = len(CORNER_POS)
    for i in xrange(length):
        if(i != length -1):
            pygame.draw.line(background,(255,255,255),CORNER_POS[i],CORNER_POS[i+1],1)
    
#    return background
    