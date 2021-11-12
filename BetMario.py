import pygame
pygame.init()  
pygame.display.set_caption("Mario")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

#CONSTANTS
LEFT=0
RIGHT=1
UP = 2
DOWN = 3
w = 4
a = 5
d = 6
s = 7

#MAP: 1 is grass, 2 is brick
map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0],
       [0, 0, 0, 0, 4, 4, 4, 4, 4, 0, 0, 0, 0 ,0 ,0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0],
       [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0],
       [0, 0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0 ,0 ,0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0 ,0 ,0, 0],
       [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0 ,0 ,0, 0],
       [0, 0, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0],
       [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,3, 0],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1, 1]]

mark = pygame.image.load('mark.png') #load your spritesheet
block = pygame.image.load('block.png') #load your spritesheet
Ash = pygame.image.load('ash.png') #load your spritesheet
Background = pygame.image.load('mario.png')
goomba = pygame.image.load('Goomba (1).png')
cloud = pygame.image.load('cloud.png')
options = pygame.image.load('options.png')

#player variables
xpos = 500 #xpos of player
ypos = 650 #ypos of player
vx = 0 #x velocity of player
vy = 0 #y velocity of player
keys = [False, False, False, False] #this list holds whether each key has been pressed
xpos2 = 200 #xpos of player
ypos2 = 650 #ypos of player
vx2 = 0 #x velocity of player
vy2 = 0
other = [False, False, False, False]
isOnGround = False #this variable stops gravity from pulling you down more when on a platform
isOnGround2 = False
#animation variables variables
frameWidth = 65
frameHeight = 65
RowNum = 0 #for left animation, this will need to change for other animations
frameNum = 0
ticker = 0
direction = DOWN

frameWidth2 = 32
frameHeight2 = 48
RowNum2 = 0 #for left animation, this will need to change for other animations
frameNum2 = 0
ticker2 = 0
direction2 = DOWN

while not gameover:
    clock.tick(60) #FPS
    
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
      
      #MO: biggest change was here- you need a down key press for all 3 buttons for BOTH characters (so six total)
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT]=True
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=True
            elif event.key == pygame.K_UP:
                keys[UP]=True
            if event.key == pygame.K_a:
                other[LEFT]=True
            elif event.key == pygame.K_d:
                other[RIGHT]=True
            elif event.key == pygame.K_w:
                other[UP]=True
           
                #MO: here too, you need a key up check for ALL SIX buttons you're usingj
        if event.type == pygame.KEYUP: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT]=False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=False
            elif event.key == pygame.K_UP:
                keys[UP]=False
            if event.key == pygame.K_a:
                other[LEFT]=False
            elif event.key == pygame.K_d:
                other[RIGHT]=False
            elif event.key == pygame.K_w:
                other[UP]=False

    #LEFT MOVEMENT
    if keys[LEFT]==True:
        vx=-3
        RowNum = 1
        direction = LEFT
    #RIGHT MOVEMENT
    elif keys[RIGHT] == True:
        vx = 3
        RowNum = 2
        direction = RIGHT
    #turn off velocity
    else:
        vx = 0
        #JUMPING
    if keys[UP] == True and isOnGround == True: #only jump when on the ground
        vy = -8
        RowNum = 3
        isOnGround = False
        direction = UP
        
        
    #Left movement
    if other[LEFT]==True:
        vx2=-3
        RowNum2 = 2
        direction2 = LEFT
    #RIGHT MOVEMENT
    elif other[RIGHT] == True:
        vx2 = 3
        RowNum2 = 3
        direction2 = RIGHT
    #turn off velocity
    else:
        vx2 = 0
        #JUMPING
    if other[UP] == True and isOnGround2 == True: #only jump when on the ground
        vy2 = -8
        RowNum2 = 1
        isOnGround2 = False
        
        direction2 = UP
    
        
    xpos+=vx #update player xpos
    ypos+=vy
    xpos2+=vx2 #update player xpos
    ypos2+=vy2
    
    
    #COLLISION
    
    #collision with feetsies
    if map[int((ypos+frameHeight)/50)][int((xpos+frameWidth/2)/50)]==1 or map[int((ypos+frameHeight)/50)][int((xpos+frameWidth/2)/50)]==2 or map[int((ypos+frameHeight)/50)][int((xpos+frameWidth/2)/50)]==3:
        isOnGround = True
        vy=0
    else:
        isOnGround = False
    
    if map[int((ypos2+frameHeight2)/50)][int((xpos2+frameWidth2/2)/50)]==1 or map[int((ypos2+frameHeight2)/50)][int((xpos2+frameWidth2/2)/50)]==2 or map[int((ypos2+frameHeight2)/50)][int((xpos2+frameWidth2/2)/50)]==3:
        isOnGround2 = True #MO changed to isonground2
        vy2=0
        
    else:
        isOnGround2 = False #MO changed to isonground2
        
    
    #bump your head, ouch!
    if map[int((ypos)/50)][int((xpos+frameWidth/2)/50)]==1 or map[int((ypos)/50)][int((xpos+frameWidth/2)/50)]==2:
        vy=0
    if map[int((ypos2)/50)][int((xpos2+frameWidth2/2)/50)]==1 or map[int((ypos2)/50)][int((xpos2+frameWidth2/2)/50)]==2:
        vy2=0
        
    #left collision (it's extra long because we check both head and feets(well, knees) for left collision
    if (map[int((ypos+frameHeight-20)/50)][int((xpos+10)/50)]==1 or map[int((ypos)/50)][int((xpos+10)/50)]==1 or map[int((ypos+frameHeight-20)/50)][int((xpos+10)/50)]==2 or map[int((ypos)/50)][int((xpos+10)/50)]==2 ) and direction == LEFT:
        xpos+=3
    if (map[int((ypos2+frameHeight2-20)/50)][int((xpos2+10)/50)]==1 or map[int((ypos2)/50)][int((xpos2+10)/50)]==1 or map[int((ypos2+frameHeight2-20)/50)][int((xpos2+10)/50)]==2 or map[int((ypos2)/50)][int((xpos+10)/50)]==2 ) and direction2 == LEFT:
        xpos2+=3
        
    #right collision needed here
    if (map[int((ypos+frameHeight-20)/50)][int((xpos+10+frameWidth)/50)]==1 or map[int((ypos)/50)][int((xpos+10+frameWidth)/50)]==1 or map[int((ypos+frameHeight-20)/50)][int((xpos+10+frameWidth)/50)]==2 or map[int((ypos)/50)][int((xpos+10+frameWidth)/50)]==2 ) and direction == RIGHT:
        xpos-=3
        
        #MO changed one of the xpos to xpos2 in this line
    if (map[int((ypos2+frameHeight2-20)/50)][int((xpos2+10+frameWidth2)/50)]==1 or map[int((ypos2)/50)][int((xpos2+10+frameWidth2)/50)]==1 or map[int((ypos2+frameHeight2-20)/50)][int((xpos2+10+frameWidth2)/50)]==2 or map[int((ypos2)/50)][int((xpos2+10+frameWidth2)/50)]==2 ) and direction2 == RIGHT:
        xpos2-=3
        
    #stop moving if you hit edge of screen (will be removed for scrolling)
    if xpos+frameWidth > 800:
        xpos-=3
    if xpos<0:
        xpos+=3
    if xpos2+frameWidth2 > 800:
        xpos2-=3
    if xpos2<0:
        xpos2+=3
    
    #stop falling if on bottom of game screen
    if ypos > 800-frameHeight:
        isOnGround = True
        vy = 0
        ypos = 800-frameHeight
        
    if ypos2 > 800-frameHeight2:
        isOnGround2 = True #MO changed to 2
        vy2 = 0
        ypos2 = 800-frameHeight2
    #gravity
    if isOnGround == False:
        vy+=.2 #notice this grows over time, aka ACCELERATION
    if isOnGround2 == False: #MO changed to 2
        vy2+=.2 #notice this grows over time, aka ACCELERATION

        
    #ANIMATION-------------------------------------------------------------------
        
    # Update Animation Information

    if vx != 0: #animate when moving
        ticker+=1
        if ticker%10==0: #only change frames every 10 ticks
          frameNum+=1
        if frameNum>3: 
           frameNum = 0
           
    if vx2 != 0: #animate when moving
        ticker2+=1
        if ticker2%10==0: #only change frames every 10 ticks
          frameNum2+=1
        if frameNum2>3: 
           frameNum2 = 0
  
    # RENDER--------------------------------------------------------------------------------
    # Once we've figured out what frame we're on and where we are, time to render.
    screen.blit(Background, (0,0), (0, 0, 800, 800))
    
    #draw map
    for i in range (16):
        for j in range(16):
            
            if map[i][j]==1:
                screen.blit(block, (j*50, i*50), (0, 0, 50, 50))
            if map[i][j]==2:
                screen.blit(mark, (j*50, i*50), (0, 0, 50, 50))
            if map[i][j]==3:
                screen.blit(goomba, (j*50, i*50), (0, 0, 50, 50))
            if map[i][j]==4:
                screen.blit(cloud, (j*50, i*50), (0, 0, 50, 50))
        
    screen.blit(Ash, (xpos, ypos), (frameWidth*frameNum, RowNum*frameHeight, frameWidth, frameHeight))
    screen.blit(options, (xpos2, ypos2), (frameWidth2*frameNum2, RowNum2*frameHeight2, frameWidth2, frameHeight2)) 
    pygame.display.flip()#this actually puts the pixel on the screen
    print(keys) #MO used for testing
    
#end game loop------------------------------------------------------------------------------
pygame.quit()
