#Practic game for invent with python

import pygame,random,sys
from pygame.locals import *

FPS=30#for frames per seond check
WINDOWWIDTH=640
WINDOWHEIGHT= 480 #size of window's height in pixels
REVEALSPEED=8
BOXSIZE=40
GAPSIZE=10
BOARDWIDTH=10
BOARDHEIGHT=7
#For good software engineeering sanity check we must have the assert statement with us
assert (BORARDWIDTH*BOARDHEIGHT)%2==0,'Error the no of tiles are even so both odd not possible'
