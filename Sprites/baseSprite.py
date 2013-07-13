import pygame
import math
import copy
from common import *

TYPE1 = load_image("1.jpg");
TYPE2 = load_image("2.jpg");
TYPE3 = load_image("3.jpg");
TYPE4 = load_image("4.jpg");
TYPE5 = load_image("5.jpg");
TYPE6 = load_image("6.jpg");
TYPE7 = load_image("7.jpg");
TYPE8 = load_image("8.jpg");
TYPE9 = load_image("9.jpg");
TYPE10 = load_image("10.jpg");
TYPE11 = load_image("11.jpg");
TYPE12 = load_image("12.jpg");
TYPE13 = load_image("13.jpg");
TYPE14 = load_image("14.jpg");
TYPE15 = load_image("15.jpg");
TYPE16 = load_image("16.jpg");
TYPE17 = load_image("17.jpg");
TYPE18 = load_image("18.jpg");
TYPE19 = load_image("19.jpg");
TYPE20 = load_image("20.jpg");
TYPE21 = load_image("21.jpg");
TYPE22 = load_image("22.jpg");
TYPE23 = load_image("23.jpg");
TYPE24 = load_image("24.jpg");
TYPE25 = load_image("25.jpg");
TYPE26 = load_image("26.jpg");
TYPE27 = load_image("27.jpg");

#use it by copy.cpoy
type_dict = {"TYPE1":TYPE1,
             "TYPE2":TYPE2,
             "TYPE3":TYPE3,
             "TYPE4":TYPE4,
             "TYPE5":TYPE5,
             "TYPE6":TYPE6,
             "TYPE7":TYPE7,
             "TYPE8":TYPE8,
             "TYPE9":TYPE9,
             "TYPE10":TYPE10,
             "TYPE11":TYPE11,
             "TYPE12":TYPE12,
             "TYPE13":TYPE13,
             "TYPE14":TYPE14,
             "TYPE15":TYPE15,
             "TYPE16":TYPE16,
             "TYPE17":TYPE17,
             "TYPE18":TYPE18,
             "TYPE19":TYPE19,
             "TYPE20":TYPE20,
             "TYPE21":TYPE21,
             "TYPE22":TYPE22,
             "TYPE23":TYPE23,
             "TYPE24":TYPE24,
             "TYPE25":TYPE25,
             "TYPE26":TYPE26,
             "TYPE27":TYPE27}


class baseSprite(pygame.sprite.Sprite):
    number = 0
    
    def __init__(self,loc,type):
        pygame.sprite.Sprite.__init__(self)
        
        self.loc = loc
        self.type = type
        self.focus = False

        self.image = copy.copy(type_dict["TYPE"+str(type)])
        
            
            
        self.rect = self.image.get_rect()
        self.rect.topleft = (loc[0]*40+80,loc[1]*40+40)
    
    def update(self):
        pass

    
    def select(self):
        self.rect.move_ip(5, -5)
        self.focus = True
            
    def unselect(self):
        self.rect.move_ip(-5, 5)
        self.focus = False

    def _locToposcenter(self):
        return (self.loc[0]*40+100,self.loc[1]*40+60)

    def _get_available_area(self):
        tlst = []
        #up
        up = self.loc[1]-1
        for y in xrange(up,-2,-1):
            if(MAPS.has_key((self.loc[0],y))):
                break;
            tlst.append((self.loc[0],y))
            
        #down
        down = up = self.loc[1]+1
        for y in xrange(down,9+1):
            if(MAPS.has_key((self.loc[0],y))):
                break;
            tlst.append((self.loc[0],y))
        #left
        left = self.loc[0]-1
        for x in xrange(left,-2,-1):
            if(MAPS.has_key((x,self.loc[1]))):
                break;
            tlst.append((x,self.loc[1]))
            
        #right    
        right = self.loc[0]+1
        for x in xrange(right,16+1):
            if(MAPS.has_key((x,self.loc[1]))):
                break;
            tlst.append((x,self.loc[1]))
        return tlst

    # 0 corner
    # 1 corner
    # 2 corners 
    def compareTo(self,sp):
        if(self.type != sp.type):
            return False
        
        #0 corner
        if(self.loc[0] == sp.loc[0]):
            check =  baseSprite._compare_samex(self.loc,sp.loc)
            if(check):
                del MAPS[self.loc]
                del MAPS[sp.loc]
                CORNER_POS.append(self._locToposcenter())
                CORNER_POS.append(sp._locToposcenter())
                return True
            
        if(self.loc[1] == sp.loc[1]):

            check = baseSprite._compare_samey(self.loc,sp.loc)
            if(check):
                del MAPS[self.loc]
                del MAPS[sp.loc]
                CORNER_POS.append(self._locToposcenter())
                CORNER_POS.append(sp._locToposcenter())
                return True
        
        
        #1 corner
        #(x1,y1) , (x2,y2) => x1,y2   x2,y1
        check = (not MAPS.has_key((self.loc[0],sp.loc[1])))\
                and baseSprite._compare_samex(self.loc,(self.loc[0],sp.loc[1])) \
                and baseSprite._compare_samey(sp.loc,(self.loc[0],sp.loc[1]))
        if(check):
            del MAPS[self.loc]
            del MAPS[sp.loc]
            CORNER_POS.append(self._locToposcenter())
            CORNER_POS.append((self.loc[0]*40+100,sp.loc[1]*40+60))
            CORNER_POS.append(sp._locToposcenter())
            return True
        
        check = (not MAPS.has_key((sp.loc[0],self.loc[1])))\
                and baseSprite._compare_samex(sp.loc,(sp.loc[0],self.loc[1])) \
                and baseSprite._compare_samey(self.loc,(sp.loc[0],self.loc[1]))
        if(check):
            del MAPS[self.loc]
            del MAPS[sp.loc]
            CORNER_POS.append(self._locToposcenter())
            CORNER_POS.append((sp.loc[0]*40+100,self.loc[1]*40+60))
            CORNER_POS.append(sp._locToposcenter())
            return True
        
        #2 corners
        #get available values
        lst1 = self._get_available_area()
        lst2 = sp._get_available_area()
        for loc1 in lst1:
            for loc2 in lst2:
                if(loc1[0] == loc2[0]):
                    check =  baseSprite._compare_samex(loc1,loc2)
                    if(check):
                        del MAPS[self.loc]
                        del MAPS[sp.loc]
                        
                        CORNER_POS.append(self._locToposcenter())
                        CORNER_POS.append(locTopos(loc1))
                        CORNER_POS.append(locTopos(loc2))
                        CORNER_POS.append(sp._locToposcenter())
                        return True
                elif(loc1[1] == loc2[1]):
                    check =  baseSprite._compare_samey(loc1,loc2)
                    if(check):
                        del MAPS[self.loc]
                        del MAPS[sp.loc]
                        
                        CORNER_POS.append(self._locToposcenter())
                        CORNER_POS.append(locTopos(loc1))
                        CORNER_POS.append(locTopos(loc2))
                        CORNER_POS.append(sp._locToposcenter())
                        return True
        
        return False
        
        
        
        
    @staticmethod
    def _compare_samey(loc1,loc2):
        start = loc1[0]
        end = loc2[0]
        if(start > end):
            start,end = end,start
        start +=1
        
        for i in xrange(start,end):
            if(MAPS.has_key((i,loc1[1])) ):
                return False

        return True
    
    @staticmethod
    def _compare_samex(loc1,loc2):
        start = loc1[1]
        end = loc2[1]
        if(start > end):
            start,end = end,start
        start +=1
        
        for i in xrange(start,end):
            if(MAPS.has_key((loc1[0],i)) ):
                return False
        
        return True
        
        