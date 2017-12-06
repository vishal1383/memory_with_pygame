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
                        pygame.display.update()#the function that update the display object class onto the sreen
                        FPSCLOCK.tick(FPS)
def generateRevealedBoxesData(var):
            revealeBoxes=False
            for i in range(BOARDWIDTH):
                        revealedBoxes.append([var]*BOARDHEIGHT)
            return revealedBoxes
def getRandomizedBoard():
            icons=[]                   #icons are basically a tuple of shape and the color accompanying them
            for shape in ALLSHAPES:
                        for color in ALLCOLORS:
                                    icons.append((shape,color))
            random.shuffle(icons)
            numIconsused=int((BOARDHEIGHT*BOARDWIDTH)/2)#explicit typecast to prevent the abuse
            icons=icons[:numIconsused]*2  #as we need a copy of the others
            random.shuffle(icons)
            #just this is to create the random tuples of the 2-D list
            #now to insert them to boxes
            boxes=[]   #this code is the some of the times that you notice the difference between c and python
            for colomn in range(BOARDHEIGHT):
                        colomn=[]
                        for y in range(BOARDWIDTH):
                                    colomn.append(icons[0])  #continuosly adding and eleent and after that deleting 
                                    del icons[0]              #it in the second line
                        board.append(colomn)                                                                                  
            return board  
def splitIntoGroups(groupSize,theList):
            #to return a list of lists divided into corresponding group sizes
            result=[]
            for i in range(0,len(theList),groupSize):
                        result.append(theList[i:i+groupSize])
            return result
def leftTopCordsOfBox(boxx,boxy):
#this funciton is for translating between the box coordinates and the general pixels
#this is helpful for us as the box that is 3rd from left and 1st from top is more 
#convienently represented as (1,3) rther than some pixel values
#so this takes the coordinates of the box in that fashion and return the pixel coordinates
#it is a good programming practice to name variables correctly
            left=boxx*(GAPSIZE+BOXWIDTH)+XMARGIN
            #XMARGIN is margin along X axis
            top=boxy*(GAPSIZE+BOXHEIGHT)+YMARGIN
            # same logic applies for Y also
            return (left,top)
#as left is the distance from the left which will be the x axis distance
# now the previous one was for changing the box coordinatres to pixel ones
#but this one will be for changing the one to pixels from box coordinates
#the texhnicalities of the issue would be  pygame.Recct(left_top_coordinates,height,width) is the format of the one to be accepted
def getBoxAtPixel(x,y):# input is the x and y coordimnates of the box
            for boxx in range(BOARDWIDTH):
                        for boxy in range(BOARDHEIGHT):
                                    left,top=leftTopCordsOfBox(boxx,boxy)
                                    boxrect=pygame.draw.Rect(left,top,BOXSIZE,BOXSIZE)                                    
                                    if(boxrect.collidepoint(x,y)):
                                                return (boxx,boxy)
            return (None,None)    
#the code must be maximum self evident as all
def drawIcon(shape,color,boxx,boxy):
            quarter=int(BOXSIZE*0.25)   #just to increse the readibility of the code
            half=int(BOXSIZE*0.1)
            
            left,top=leftTopCoordsOfBox(box,boxy)  #get pixel  co-ordinates
            
            if shape==DONUT:
                        pygame.draw.circle(DISLAYSURF,color,(left+half,top+half),half-5)
                        pygame.draw.circle(DISPLAYSURF,BGCOLOR,(left+half,top+half),quarter-5)
            elif shape==SQUARE:
                        pygame.draw.Rect(DISPLAYSURF,color,(left+quarter,top+quarter,BOXSIZE-half,BOXSIZE-half)
            elif shape==LINES:
                        for i in range(0,BOXSIZE,4):
                                         pygame.draw.line(DISPLAYSURF,color,(left+i,top),(top+i,left))
            elif shape==OVAL:                
                        pygame.draw.ellipse(DISPLAYSURF, color, (left, top + quarter, BOXSIZE, half))    
def getShapeAndColor(board,boxx,boxy):
            return (board[boxx][boxy][0],board[boxx][boxy][1])
# it is a single line of function it could have been easily replaced by that in the code but I choose not ot to improv the readability of the code

#The snell's law is always valid 
                                         
                                         
                                         
            
            
