import pygame
from pygame.locals import *
import os
import sys
import random
import Background
import Tools
import Sprites
import Levels
from common import *


def run_game():
    
    # Game parameters
    pygame.mouse.set_visible(1)
    pygame.display.set_caption('lianliankan') 
    pygame.key.set_repeat(20,50)
    background = Background.background.init()
    screen.blit(background, [0, 0])  
#    pygame.draw.line(background,(255,255,255),(0,0),(200,400),2)
#    screen.blit(background, [0, 0]) 
    pygame.display.flip()

    
    # init data
    clock = pygame.time.Clock()
    _running = True


    # level control .. including map initiate
    #Sprites.baseSprite.baseSprite(loc,MAPS[loc])
    init_map()
    
    # sprite
    group_pattern = pygame.sprite.RenderUpdates()
    group_background = pygame.sprite.RenderUpdates()

    # sprite instances
    #
    for sprite in MAPS.values():
        group_pattern.add(sprite)
    
    
    timebar = Background.timebar.timeBar()
    group_background.add(timebar)
    
    while _running:
        # Limit frame speed to 50 FPS
        #
        time_passed = clock.tick(25)
#        pygame.time.delay(10)
    
        if(len(CORNER_POS)!=0):

           group_background.add(Background.connectline.connectLine(CORNER_POS))
           del CORNER_POS[:]
           
           
        group_background.update()
        rectlist = group_background.draw(screen)
        pygame.display.update(rectlist)
        group_background.clear(screen,background)

        
        group_pattern.update()
        rectlist = group_pattern.draw(screen)
        pygame.display.update(rectlist)
        group_pattern.clear(screen,background)
        
        

        
        
        #check whether game over
        if(timebar.pasttime > timebar.LEFTTIME):
            pass

        #check win or not
        
        
        #check whether there is anther pair
        
        
    
    

    
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                position = ((position[0]-80)/40,(position[1]-40)/40)
                if(MAPS.has_key(position)):
                    sprite = MAPS[position]
                    if(not sprite.focus):
                        sprite.select()
                        if(SELECT_SPRITES.count(sprite) == 0):
                            SELECT_SPRITES.append(sprite)
                    else:
                        sprite.unselect()
                        if(len(SELECT_SPRITES)>0):
                            SELECT_SPRITES.pop()
                    if(len(SELECT_SPRITES) ==2 ):
                        SELECT_SPRITES.reverse()
                        sprite1 = SELECT_SPRITES.pop()
                        sprite1.unselect()
                        if(sprite1.compareTo(SELECT_SPRITES[0])):
                            group_pattern.remove(sprite1,SELECT_SPRITES.pop())
                            timebar.reset()
                            
            elif event.type == KEYDOWN:
                if(event.key == K_ESCAPE or event.key ==K_RETURN ):
                    pause_game(timebar);
                
                
def init_map():
    Levels.levels.level1()    
    
    
def pause_game(timebar):
    timebar.pause()
    
    
def game_over():
    pass




if(__name__ == '__main__'):
    
    run_game();
    
    
    
    
    
    
    
    
    
    
    