from __future__ import with_statement
import os
import random
import Sprites
from common import *

randomlist = []

def level1():
    fullname = os.path.join('Levels', "level2.txt")
    number = 0
    with open(fullname) as f:
        j = -1
        for line in f:
            if(j==-1):
                number = int(line)
                changelist(number)
                j +=1
                continue
            i = 0
            listdata = map(int,line.split(" "))
            for isexsis in listdata:
                if(isexsis==1):
                    MAPS[(i,j)]=Sprites.baseSprite.baseSprite((i,j),randomlist.pop())
                i = i+1
            j = j+1

def changelist(number):
    global randomlist
    for i in xrange(number/2):
        randomlist.append(random.randint(1,27))
    randomlist = 2*randomlist
    random.shuffle(randomlist)
    
    
    
    
    
    