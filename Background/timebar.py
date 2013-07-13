import pygame
import time
import math
from common import *

class timeBar(pygame.sprite.Sprite):
    
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)     
        self.pasttime = 0;
        self.lasttime = time.time();    
        self.LEFTTIME = 30;#seconds
        self.pause_start = 0;
        self.pause_end = 0;
        self.image = pygame.Surface([640,15]);  
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.topleft = (80,440)
    
    def update(self):
        
        self.pasttime = time.time() - self.lasttime - (self.pause_end - self.pause_start)
        
        start_x = (1 - float(self.pasttime) / self.LEFTTIME) * 630
        if(start_x <= 5 ):
            return
        self.image.fill((255,255,255))
        
        pygame.draw.line(self.image, 
                         (0,0,0),
                         (start_x,7),
                         (635,7),
                            11)





    def reset(self):
        self.lasttime = time.time()
        self.pasttime = 0;

    
    def pause(self):
        self.pause_start = time.time()
    
    
    def recover(self):
        self.pause_end = time.time()
    
    
    
    
    
    
    
    
    
    
    
    