#Practic game for invent with python

import pygame,random,sys
from pygame.locals import *
# here I DEFINE ALL THE constant that would be used by me in the process of the routine
FPS=30#for frames per seond check
WINDOWWIDTH=640
WINDOWHEIGHT= 480 #size of window's height in pixels
REVEALSPEED=8   #Speed of boxes sliding and revealing the corners
BOXSIZE=40      #
GAPSIZE=10
BOARDWIDTH=10 # NO OF COLOUMNS OF ICON
BOARDHEIGHT=7 #NO OF ROWS OF ICON
#For good software engineeering sanity check we must have the assert statement with us
assert (BORARDWIDTH*BOARDHEIGHT)%2==0,'Error the no of tiles are even, so both odd not possible'
#EXPRESSION FOR MARGIN
XMARGIN=int(WINDOWWIDTH-((BOARDWIDTH*(GAPSIZE+BOXSIZE))/2))
YMARGIN=int(WINDOWHEIGHT-((BOARDHEIGHT*(GAPSIZE+BOXSIZE))/2))
#colors definition
#        R    G     B
GRAY    =(100,100,100)
NAVYBLUE =( 60,60,100)
WHITE    =(255,255,255)
RED      =(255,0,0)
GREEN   =(0,255,0)
BLUE    =(0,0,255)
YELLOW  =(255,255,0)
ORANGE  =(255,128,0)
PURPLE  =(255,0,255)
CYAN   =(0,255,255)

BGCOLOR=NAVYBLUE  #Background color set to navy blue
LIGHTBGCOLOR=GRAY
BOXCOCLOR=WHITE
HIGHLIGHTCOLOR=BLUE
#For the shapes of the icons we"ll store them later as a TUPLE
DONUT='donut'
SQUARE='square'
LINES='lines'
OVAL='oval'
ALLCOLORS=(RED,GREEN,BLUE,YELLOW,ORANGE,PURPLE,CYAN)#COLOR TUPLE
ALLSHAPES=(DONUT,SQUARE,DIAMOND,LINES,OVAL)
assert len(ALLCOLORS)*len(ALLSHAPES)*2>=BOARDWIDTH*BOARDHEIGHT,"Board is too big "



            
            
            
