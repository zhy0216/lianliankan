import pygame
import time
import math
import random
import copy
from common import *



class connectLine(pygame.sprite.Sprite):
    
    
    def __init__(self,positions):
        pygame.sprite.Sprite.__init__(self)     
        
        max_x = max(positions)[0]
        min_x = min(positions)[0]
        tlist = map(lambda x:x[1],positions)
        max_y = max(tlist)
        min_y = min(tlist)
        
        max_pos = (max_x,max_y)
        min_pos = (min_x,min_y)
        size =(max_pos[0]-min_pos[0]+20, max_pos[1] - min_pos[1]+20)
        self.image = pygame.Surface(size);  
        
        self.rect = self.image.get_rect()
        self.rect.topleft = (min_pos[0]-10,min_pos[1]-10)
        self.positions = map(lambda x:(x[0]-self.rect.topleft[0],x[1]-self.rect.topleft[1]),positions)
        pygame.draw.lines(self.image, 
                  (255,255,255), 
                  False, 
                  self.positions, 
                  2)
        self.time = time.time()
        
        
    
    def update(self):
        if((time.time() - self.time) > 0.5  ):
            self.kill()
        
        self.image.fill([0,0,0])
#        length = len(self.positions)
#        for i in xrange(length):
#            if(i != length -1):
#                pygame.draw.line(self.image,(255,255,255),self.positions[i],self.positions[i+1],1)
        thelist = copy.copy(self.positions)
        thelist = connectLine.make_wave(thelist);
        pygame.draw.lines(self.image,
                          (58,95,205),
                          False,
                          thelist,
                           1)
        

    @staticmethod
    def make_wave(tlist):
        newlist = []
        length = len(tlist)
        for i in xrange(length):
            if(i >= length-1):
                break
            if(tlist[i][0] == tlist[i+1][0]):
                if(tlist[i][1] < tlist[i+1][1]):
                    iy = tlist[i][1]
                    end = tlist[i+1][1]
                    while(iy <= end):
                        ix = tlist[i][0] + random.randint(-8,8)
                        newlist.append((ix,iy))
                        iy += random.randint(0,10)
                else:
                    iy = tlist[i][1]
                    end = tlist[i+1][1]
                    while(iy >= end):
                        ix = tlist[i][0] + random.randint(-8,8)
                        newlist.append((ix,iy))
                        iy -= random.randint(0,10)
                    
            if(tlist[i][1] == tlist[i+1][1]):
                if(tlist[i][0] < tlist[i+1][0]):
                    ix = tlist[i][0]
                    end = tlist[i+1][0]
                    while(ix <= end):
                        iy = tlist[i][1]+ random.randint(-8,8)
                        newlist.append((ix,iy))
                        ix += random.randint(0,10)
                else:
                    ix = tlist[i][0]
                    end = tlist[i+1][0]
                    while(ix >= end):
                        iy = tlist[i][1]+ random.randint(-8,8)
                        newlist.append((ix,iy))
                        ix -= random.randint(0,10)
        return newlist
        
         
        
            
            
            
            
            
     





