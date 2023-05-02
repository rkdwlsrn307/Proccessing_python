# ball
x = 0
y = 0
diam = 30
xdir = 6
ydir = 6
ballColor = 0xffffff00

# pad
padX = 0
padY = 0
padWidth = 200
padColor = 0xff00ff00

# bricks
bColNo = 10
bWidth = 0
bHeight = 0
#bricks = [True for i in range(bColNo)]
bricks1 = [True] * 10
bricks2 = [True] * 10
bricks3 = [True] * 10

start = False

win_cnt = 0

level_up = False


def reset():
    global x, y, xdir, ydir
    global win_cnt, level_up
    global bricks1, bricks2, bricks3
    bricks1 = [True] * 10
    bricks2 = [True] * 10
    bricks3 = [True] * 10
    textAlign(CENTER)
    start = False
    level_up = False
    x = width / 2
    y = height / 2
    xdir = 6
    ydir = 6
    win_cnt = 0
    noLoop()

def setup():
    
    size(1400, 1000)
    global x, y, diam, xdir, ydir, ballColor
    global padX, padY, padWidth, padColor
    global bColNo, bWidth, bHeight
  
    x = width / 2
    y = height / 2
    diam = 50
    xdir = 6
    ydir = 6
    ballColor = 0xffffff00

    padX = width/2
    padY = height-20
    padWidth = 400
    padColor = 0xff00ff00
  
    bColNo = 10
    bWidth = width / bColNo
    bHeight = 30
  

def draw():
    
    background(255)
    
    global start
    if start == False:
        fill(0, 0 , 0)
        textAlign(CENTER)
        textSize(150)
        text("Click to start", width / 2, height / 2 - 100)
        noLoop()
    
    global x, y, diam, xdir, ydir, ballColor
    global padX, padY, padWidth, padColor
    global bColNo, bWidth, bHeight
    global win_cnt, level_up
    global bricks1, bricks2, bricks3
    
    # drawing a ball
    fill(ballColor)
    ellipse(x, y, diam, diam) 
    x += xdir
    y += ydir 
    
    # drawing racket...
    fill(ballColor)
    padX = mouseX - padWidth/2
    rect(padX, padY, padWidth, 20, 15)

    # drawing bricks
    fill(0, 255, 0) # brick color    
    for i, brick1 in enumerate(bricks1):
        if brick1:
            rect(i*bWidth, 0, bWidth, bHeight) # last parameter is for rounded rectangle  
    for i, brick2 in enumerate(bricks2):
        if brick2:
            rect(i*bWidth, bHeight, bWidth, bHeight) # last parameter is for rounded rectangle    
    for i, brick3 in enumerate(bricks3):
        if brick3:
            rect(i*bWidth, bHeight * 2, bWidth, bHeight)   
    
    # ball bouncing 
    if x - diam/2 < 0: # left side check
        xdir *= -1
        #padWidth = padWidth - 10
    
    if x + diam/2 > width: # right side check
        xdir *= -1
        #padWidth = padWidth - 20
    
    if y - diam/2 < 0: # up 
        ydir *= -1
    
    if y + diam/2 > height: # bottom
        ydir *= -1
    
    # checking collision with a pad
    if x > padX and x < padX + padWidth and y > padY-diam/2:
        ydir *= -1
        fill(0, 0, 0)
        rect(padX+2, padY+2, padWidth-4, 16, 15)
    
    # brick and ball collision detection
    if y - diam/2 < bHeight: # if the ball'x is in the region of bricks
        if bricks1[x // bWidth]: # when the ball'y hits the bricks
            ydir *= -1
            win_cnt += 1
            bricks1[x // bWidth] = False
    if y - diam/2 < (bHeight * 2):
        if bricks2[x // bWidth]: # when the ball'y hits the bricks
            ydir *= -1
            win_cnt += 1
            bricks2[x // bWidth] = False
    if y - diam/2 < (bHeight * 3):
        if bricks3[x // bWidth]: # when the ball'y hits the bricks
            ydir *= -1
            win_cnt += 1
            bricks3[x // bWidth] = False
    
    if win_cnt >= 15 and level_up == False :
        level_up = True
        xdir *= 2
        ydir *= 2
            
    if y + diam/2 >= height :
        reset()
        fill(255, 0 , 0)
        textSize(150)
        text("Game over", width / 2, height / 2)
        textSize(50)
        text("Click to restart", width / 2, height / 2 + 100)
    elif win_cnt == 30 :
        reset()
        fill(0, 0, 255)
        textSize(150)
        text("Victory", width / 2, height / 2)
        textSize(50)
        text("Click to restart", width / 2, height / 2 + 100)

def mouseClicked():
    global start
    start = True
    loop()
    
#  
        
