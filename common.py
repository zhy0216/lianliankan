import pygame
import os

# for galaxy s
SCREEN_WIDTH, SCREEN_HEIGHT = 800,480 
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT],pygame.HWSURFACE | pygame.DOUBLEBUF)




# map: store (x,y):Sprite?
#x = i*40+80, y = i*40 + 40
# x * y = 9*16
MAPS = {}
SELECT_SPRITES = []
CORNER_POS = []

def init_MAP(level = 1):
    pass

def locTopos(loc):
    return (loc[0]*40+100,loc[1]*40+60)

#
def load_image(name,alpha = False):
    fullname = os.path.join('Data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    if(alpha):
        image = image.convert_alpha()
    else:
        image = image.convert()
    return image