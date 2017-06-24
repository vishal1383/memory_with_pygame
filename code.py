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

def main():
            global FPSCLOCK,DISPLAYSURF  #Had to initialie to global becaus we'll use them in other funcrions too
            pygame.init()
            FPSCLOCK=pygame.time.CLock()
            DISPLAYSURF=pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
            DISPLAYSURF=pygame.display.set_caption('Memory Game')
            mousex,mousey=0,0# set the x and y coordinates of the mouse
            mainBoard=getRandomizedBoard() #generate the randomized board data structure which corresponds to the 2D tuple
            revealedBoxes=generateRevealedBoxesData(Flase)# check the revealed boxes data
            firstSelection=None #set initially to none type
            #fill the board
            DISPLAYSURF.fill(BGCOLOR)
            while TRUE:#Main game loop
                        mouseCLicked=False
                        DISPLAYSURF.fill(BGCOLOR)# destroy the previous board  and draw the current new board for the new iteration
                        drawBoard(mainBoard,DISPLAYSURF)
                        #event handling
                        for event in pygame.event.get():
                                    if event.type==QUIT:
                                                pygame.quit()
                                                sys.exit()
                                    elif event.type==MOUSEMOTION: #a constant found in the pygame
                                                mousex,mousey=event.pos
                                    elif event.type==MOUSEBUTTONUP:
                                                mousex,mousey=event.pos
                                                mouseClicked=True
                        boxx,boxy=getBoxAtPixel(mousex,mousey)
                        #After getting the box at th position we must be able to tell whether it is clicked or not
                        if boxx!=None and boxy!=None:
                                    if revealedBoxes[boxx][boxy]==False:
                                                drawHighlightBox(boxx,boxy)
                                    if not revealedBoxes[boxx][boxy] and mouseCLicked:
                                                revealeBoxesAnimation(mainBoard,[(boxx,boxy)])
                                                revealedBoxes[boxx][boxy]=True
                                    if firstSelection==None:
                                                            firstSelection=(boxx,boxy)
                                    else:#current box was second
                                                icon1shape,icon1color=getShapeAndColor(mainBoard,firstSelection[0],
                                                                                       firstSelection[1])
                                                icon2shape,icon2shape=getShapeAndColor(mainBoard,boxx,boxy)
                                                #check if they are equal or not
                                                if icon1color!=icon2color or icon1shape!=icon2shape:
                                                            #do somthing to pass th e time so that
                                                            #the player could view the boxes
                                                            pygame.time.wait(1000)
                                                            coverBoxesAnimation(mainBoard,[(firstSelection[0],firstSelection[1]),(boxx,boxy)])
                                                            revealedBoxes[firstSelection[0]][firstSelection[1]]=False
                                                            revealedBoxes[boxx][boxy]=False
                                                elif hasWon(revealedBoxes):#the player has won 
                                                            gameWonAnimation(mainBoard)
                                                            pygme.time.wait(2000)
                                                            #start again
                                                            mainBoard=getRandomBoard()
                                                            revealedBoxes=generateRevealedBoxesData(False)
                                                            drawBoard(mainBoard,revealedBoxes)
                                                            pygame.display.update()
                                                            pygame.time.wait(1000)
                                                firstSelection=None
                        pygame.display.update()#the function that update the display objec tclass onto the sreen
                        FPSCLOCK.tick(FPS)
                                                                                       
                                                                                       
            


            
            
            
