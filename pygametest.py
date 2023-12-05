
import pygame
import sys
import random
# 初始化Pygame
'''

'''
weith=1000
height=600
globalVolume=0.25
bulletSpeedX=4
bulletSpeedY=-30
enemyBulletSpeed=10
starSpeed=5
bulletMaxNum=1000
bulletradius=10
indexnum=0
starIndexNum=0
musicIndexNum=1
musicStatus=0
enemyHeath=5
playerHeath=10
presstimes=0
score=0
expSizeX=300
expSizeY=25
isBegin=0
ispause=0
isOver=0
is_hovered=False
is_clicked=False
isFire=0
isHit=0
startButton=pygame.Rect(weith/2-100, height/2+10, 207, 55)
startButtonColor=(255,255,255)
startTextColor=(0,255,255)
exitColor=(0,0,0)
exitTextColor=(0,255,255)
restartColor=(0,0,0)
restartTextColor=(0,255,255)
pauseImage=pygame.image.load('assert/pause.png')
pauseImageFill=pygame.image.load('assert/pause_fill.png')
pauseImageEnd=pygame.image.load('assert/pause.png')
pauseImageBig=pygame.image.load('assert/pause_big.png')
pauseImageBigFill=pygame.image.load('assert/pause_big_fill.png')
pauseImageBigEnd=pygame.image.load('assert/pause_big.png')
pauseButton=pygame.Rect(weith-50, 0, 50, 50)
pauseButtonBig=pygame.Rect(weith/2-150, height/2-150, 300, 300)
directionImage=pygame.image.load('assert/direction.png')
directionRect=pygame.Rect(weith/2+100, height/2-150, 400, 400)
#enemyimage=pygame.image.load('enemy00.png')
enemyImage=[]
enemyImage.append(pygame.image.load('assert/enemy00.png'))
enemyImage.append(pygame.image.load('assert/enemy01.png'))
enemyImage.append(pygame.image.load('assert/enemy02.png'))
enemyImage.append(pygame.image.load('assert/enemy03.png'))
enemyImage.append(pygame.image.load('assert/enemy04.png'))
enemyImage.append(pygame.image.load('assert/enemy05.png'))
startSceneImage=pygame.image.load('assert/starScene.png')
bulletImage=pygame.image.load('assert/bullet.png')
enemyBulletImage=pygame.image.load('assert/enemyBullet.png')
starImage=[]
starImage.append(pygame.image.load('assert/smallstar.png'))
starImage.append(pygame.image.load('assert/star.png'))
starImage.append(pygame.image.load('assert/bigstar.png'))
iconImage=pygame.image.load('assert/player.png')
pygame.display.set_icon(iconImage)
#for i in range(len(starImage)):
#    starImage[i].set_alpha(200)
timeNum=0
enemyBulletNum=0
pygame.init()
#music

startSceneMusic=pygame.mixer.Sound('assert/加纳战机 - 01.开场.mp3')
endMusic=pygame.mixer.Sound('assert/加纳战机 - 17.游戏结束.mp3')
pauseMusic=pygame.mixer.Sound('assert/加纳战机 - 02.补给基地.mp3')
isendMusic=0
ispauseMusic=0
isplayingMusic=0
startSceneMusic.set_volume(globalVolume)
endMusic.set_volume(globalVolume)
pauseMusic.set_volume(globalVolume)
fireMusic=pygame.mixer.Sound('assert/fire.mp3')
hitMusic=pygame.mixer.Sound('assert/hit.mp3')
playSceneMusic=[]
playSceneMusic.append(pygame.mixer.Sound('assert/加纳战机 - 03.月球.mp3'))
playSceneMusic.append(pygame.mixer.Sound('assert/加纳战机 - 04.火星.mp3'))
playSceneMusic.append(pygame.mixer.Sound('assert/加纳战机 - 05.水星.mp3'))
playSceneMusic.append(pygame.mixer.Sound('assert/加纳战机 - 06.木星.mp3'))
playSceneMusic.append(pygame.mixer.Sound('assert/加纳战机 - 07.金星.mp3'))
playSceneMusic.append(pygame.mixer.Sound('assert/加纳战机 - 08.土星.mp3'))
playSceneMusic.append(pygame.mixer.Sound('assert/加纳战机 - 09.日星.mp3'))
playSceneMusic.append(pygame.mixer.Sound('assert/加纳战机 - 10.日星内部.mp3'))
playSceneMusic.append(pygame.mixer.Sound('assert/加纳战机 - 11.BOSS战1.mp3'))
playSceneMusic.append(pygame.mixer.Sound('assert/加纳战机 - 12.BOSS战2.mp3'))

musicStatus=random.randint(0,len(playSceneMusic)-1)
playSceneMusicActual=playSceneMusic[musicStatus]
startSceneMusic.play()
class player():   
    def __init__(self):
        self.listx=[]
        self.listy=[]
        self.moveSpeedX=[]
        self.level=1
        self.exp=0
        self.heath=playerHeath
        x,y=(weith/2,height/2+100)
        self.image=pygame.image.load('assert/player.png')
        self.rect=self.image.get_rect(center=(x,y))
    def move(self,numx,numy):
        if 0<self.rect.x+numx+self.rect.width/2<weith and 0<self.rect.y+numy+self.rect.height/2<height:
            self.rect.move_ip(numx,numy)
    def getkey(self,keys):
        global enemy,ispause
        if not ispause:
            if keys[pygame.K_DOWN]:#
                self.move(0,20)
            if keys[pygame.K_UP]:#
                self.move(0,-20)
            if keys[pygame.K_LEFT]:#
                self.move(-20,0)
            if keys[pygame.K_RIGHT]:#
                self.move(20,0)           
            if keys[pygame.K_SPACE]:#
                for i in range(self.level):
                    self.addxy() 
            if keys[pygame.K_KP0]:#                 
                enemy.add()    
    def getkeyonce(self,keys):
        global ispause,star,playerHeath,playSceneMusicActual,isplayingMusic
        if keys[pygame.K_KP1]:#    
            self.exp=0                    
            self.heath+=int(self.level/5)+1
            self.level+=1            
        if keys[pygame.K_KP2]:# 
            playSceneMusicActual.stop()
            isplayingMusic=0               
            playSceneMusicActual=playSceneMusic[random.randint(0,len(playSceneMusic)-1)]
        if keys[pygame.K_KP3]:# 
            initGame()
        if keys[pygame.K_ESCAPE]:
            ispause=1-ispause
    def addxy(self):
        global presstimes,isFire   
        isFire=1  
        if len(self.listx)>=bulletMaxNum+1:
            self.listx=self.listx[1:]
            self.listy=self.listy[1:]
        if self.rect.x not in self.listx or self.rect.y not in self.listy:
            self.listx.append(self.rect.x+self.rect.width/2-bulletImage.get_width()/2)  
            self.listy.append(self.rect.y+self.rect.height/2-bulletImage.get_height()/2)
            presstimes=(presstimes+1)%self.level
            if self.level%2==1 and presstimes==self.level-1:
                self.moveSpeedX.append(int(0))     
            else:
                self.moveSpeedX.append((int(presstimes/2)+1)*(-1)**presstimes*bulletSpeedX)        
    def bulletfly(self):
        if not ispause:
            for i in range(len(self.listx)):
                
                self.listx[i] += self.moveSpeedX[i]
                self.listy[i] += bulletSpeedY
            
            '''
            if self.level%2==1:
                if self.moveSpeedX[i]==self.level-1:
                    self.listx[i]+=0
            else:
                self.listx[i]=self.listx[i]+(-1)**(self.moveSpeedX[i])*4*(self.moveSpeedX[i]/2+1)
            self.listy[i] += bulletSpeedY
            
            if  self.moveMode[i]==0:
                self.listx[i] += bulletSpeedX
                self.listy[i] += bulletSpeedY
            elif self.moveMode[i]==1:
                self.listx[i] -= bulletSpeedX
                self.listy[i] += bulletSpeedY
            elif self.moveMode[i]==2:
                self.listx[i] += 0
                self.listy[i] += bulletSpeedY
            '''
    def drawbullet(self):
        global screen
        if self.listx:
            for i,j in zip(self.listx,self.listy):
                #pygame.draw.circle(screen,(255,255,255),(i+self.rect.width/2,j+self.rect.height/2),bulletradius)
                bulletRect=(i,j,bulletImage.get_width(),bulletImage.get_height())
                screen.blit(bulletImage,bulletRect)
    def hitcheck(self):
        global enemy,isHit
        needtodel=[]
        for j in range(enemy.number):
            for i in range(len(self.listx)):
                if enemy.rect[j].colliderect((self.listx[i], self.listy[i], bulletImage.get_width(), bulletImage.get_height())):
                    needtodel.append(int(i))
                    isHit=1
                    enemy.heath[j]-=1
        for i in range(len(self.listx)):
            if self.listy[i]<0 or self.listx[i]<0 or self.listx[i]>weith:
                needtodel.append(int(i))
        self.listx=[self.listx[i] for i in range(len(self.listx)) if i not in needtodel]
        self.listy=[self.listy[i] for i in range(len(self.listy)) if i not in needtodel]
        self.moveSpeedX=[self.moveSpeedX[i] for i in range(len(self.moveSpeedX)) if i not in needtodel]
        '''
        for i in range(len(needtodel)):
            if needtodel[i]<=len(self.listx):
                del self.listx[needtodel[i]]
                del self.listy[needtodel[i]] 
        '''  
    def playerCheck(self):
        global enemy,isOver
        needtodel=[]
        for j in range(enemy.number):
            if enemy.rect[j].colliderect(self.rect):
                isOver=1
        for i in range(len(enemy.bulletRect)):
            if self.rect.colliderect(enemy.bulletRect[i]):
                self.heath-=1
                needtodel.append(i)
                if self.heath<=0:
                    isOver=1
            if enemy.bulletRect[i].x<0 or enemy.bulletRect[i].y>height or enemy.bulletRect[i].x>weith:
                needtodel.append(i)
        enemy.bulletRect=[enemy.bulletRect[i] for i in range(len(enemy.bulletRect)) if i not in needtodel]
        enemy.bulletSpeedx=[enemy.bulletSpeedx[i] for i in range(len(enemy.bulletSpeedx)) if i not in needtodel]
    def init(self):
        self.exp=0
        self.level=1
        self.heath=playerHeath
        self.listx=[]
        self.listy=[]
        self.moveSpeedX=[]
        self.rect=self.image.get_rect(center=(weith/2,height/2+100))
class enemy():
    def __init__(self):
        self.number=0
        self.rect=[]
        self.heath=[] 
        self.style=[]
        self.bulletRect=[]
        self.bulletSpeedx=[]     
    def add(self):
        if self.number<player.level*10:
            self.number+=1
            self.heath.append(int(enemyHeath))
            #rectindex=pygame.Rect(random.randint(0,weith),100,32,32)
            self.style.append(random.randint(0, len(enemyImage)-1)) 
            rectindex=enemyImage[self.style[-1]].get_rect(center=(random.randint(0,weith),random.randint(0,200)))
            self.rect.append(rectindex)     
    def drawEnemy(self):
        global screen
        for i in range(self.number):
            if isinstance(self.rect[i], pygame.Rect):
                #pygame.draw.rect(screen,self.color[i],self.rect[i])
                screen.blit(enemyImage[self.style[i]],self.rect[i])
        for i in range(len(self.bulletRect)):
            screen.blit(enemyBulletImage,self.bulletRect[i])
    def selfcheck(self):
        global score
        global player
        needtodel=[]
        for i in range(self.number):
            if self.rect[i].y>height:
                needtodel.append(int(i))
            if self.heath[i]<=0:
                needtodel.append(int(i))
                if not isOver:
                    score+=1
                player.exp+=1
                if player.exp>=player.level*10:
                    player.exp=0                    
                    player.heath+=int(player.level/5)+1
                    player.level+=1                   
        self.heath=[self.heath[i] for i in range(len(self.heath)) if i not in needtodel]
        self.rect=[self.rect[i] for i in range(len(self.rect)) if i not in needtodel]
        self.style=[self.style[i] for i in range(len(self.style)) if i not in needtodel]
        self.number-=len(needtodel)
        '''
        for j in range(len(needtodel)):
            if needtodel[j]<=self.number:
                del self.heath[needtodel[j]]
                del self.rect[needtodel[j]]
                self.number-=1
        '''
    def fire(self):
        if self.number-1:
            randomEnemy=random.randint(0,self.number-1)
            rectindex=enemyBulletImage.get_rect(bottom=self.rect[randomEnemy].bottom,left=self.rect[randomEnemy].x+self.rect[randomEnemy].width/2)
            self.bulletRect.append(rectindex)
            self.bulletSpeedx.append(random.randint(-player.level-1,player.level+1))
    def bulletfly(self):
        if not ispause:
            for i in range(len(self.bulletRect)):
                self.bulletRect[i].move_ip(self.bulletSpeedx[i],enemyBulletSpeed)
    def enemyMove(self):
        global starSpeed
        if not ispause:
            for i in range(int(self.number)):
                self.rect[i].y=self.rect[i].y+0  
    def init(self):
        self.number=0
        self.rect=[]
        self.heath=[] 
        self.style=[]
        self.bulletRect=[]
        self.bulletSpeedx=[]    
class star():
    def __init__(self):
        self.number=0
        self.mode=[]
        self.rect=[]
    def add(self):
        self.number+=1
        '''
        randomnum=random.randint(0,9)
        if randomnum==0:#大星星
            self.mode.append(2)
            print('大星星')
        if randomnum<5 and randomnum>1:#普通星星
            self.mode.append(1)
        if randomnum<=9 and randomnum>=5: #小星星
            self.mode.append(0)
        '''
        self.mode.append(random.randint(0,len(starImage)-1))
        rectindex=starImage[self.mode[-1]].get_rect(center=(random.randint(20,weith-20),0))
        self.rect.append(rectindex)
    def drawingstar(self):
        global screen
        for i in range(int(self.number)):
            if isinstance(self.rect[i], pygame.Rect):
                screen.blit(starImage[self.mode[i]],self.rect[i])
    def starMove(self):
        global starSpeed
        self.selfCheck()
        if not ispause:
            starSpeed=5+player.level
            for i in range(int(self.number)):
                self.rect[i].y=self.rect[i].y+starSpeed
    def selfCheck(self):
        needtodel=[]
        for i in range(self.number):
            if self.rect[i].y>height:
                needtodel.append(int(i))
                self.number-=1
        self.rect=[self.rect[i] for i in range(len(self.rect)) if i not in needtodel]
        self.mode=[self.mode[i] for i in range(len(self.mode)) if i not in needtodel]
    def init(self):
        self.number=0
        self.mode=[]
        self.rect=[]
def gameOverScene():
    global exitTextRect,restartTextRect
    screen.fill((255, 255, 255))
    gameOverText=pixelFontBig.render('Game Over',True,startTextColor)
    restartText=pixelFontBig.render('Restart Game',True,restartTextColor)
    restartTextRect=restartText.get_rect(center=(weith/2,height/2+200))
    exitText=pixelFontBig.render('Exit Game',True,exitTextColor)
    exitTextRect=exitText.get_rect(center=(weith/2,height/2+100))
    scoreText=pixelFontBig.render(f"score:{int(score):04d}",True,startTextColor)
    gameOverTextRect=gameOverText.get_rect(center=(weith/2,height/2-100))
    scoreTextRect=scoreText.get_rect(center=(weith/2,height/2))
    screen.blit(gameOverText,gameOverTextRect)
    screen.blit(scoreText,scoreTextRect)
    pygame.draw.rect(screen,exitColor,exitTextRect)
    pygame.draw.rect(screen,restartColor,restartTextRect)
    screen.blit(exitText,exitTextRect)
    screen.blit(restartText,restartTextRect)   
    pygame.display.update()
def drawing():
    global player,isfirst,startButton
    global screen
    global enemy
    screen.fill((0, 0, 0))
    # 绘制矩形
    #pygame.draw.circle(screen,(0,255,255),(200,200),50)
    if isBegin:
        star.drawingstar()    
        screen.blit(player.image,player.rect)
        player.drawbullet()
        enemy.drawEnemy()
        expRect=pygame.Rect(weith-expSizeX, height-expSizeY, expSizeX, expSizeY)       
        expRectN=pygame.Rect(weith-expSizeX, height-expSizeY, int(expSizeX*player.exp/(player.level*10)), expSizeY)
        heathRect=pygame.Rect(weith-expSizeX, height-2*expSizeY-10, expSizeX, expSizeY)
        heathRectN=pygame.Rect(weith-expSizeX, height-2*expSizeY-10, int(expSizeX*player.heath/(playerHeath+player.level-1)), expSizeY)  
        pygame.draw.rect(screen,(110,255,100),expRectN,0,5)  
        pygame.draw.rect(screen,(160,255,200),expRect,3,5)            
        pygame.draw.rect(screen,(255,45,45),heathRectN,0,5)
        pygame.draw.rect(screen,(234,155,155),heathRect,3,5)
        levelText=pixelFont.render(f"level:{int(player.level):02d}",True,(255,255,255))
        timeText=pixelFont.render(f"time:{int((pygame.time.get_ticks()-timeNum)/1000):04d}",True,(255,255,255))
        scoreText=pixelFont.render(f"score:{int(score):04d}",True,(255,255,255))
        heathText=pixelFont.render(f"Heath:{int(player.heath):02d}",True,(255,255,255))
        screen.blit(heathText,(weith-expSizeX-15*8,height-2*expSizeY-10))
        screen.blit(levelText,(weith-expSizeX-15*8,height-expSizeY))
        screen.blit(scoreText,(0,25))
        screen.blit(timeText,(0,0))
        #pygame.draw.rect(screen, pauseButtonColor, pauseButton)
        screen.blit(pauseImageEnd,pauseButton)
        if ispause:
            screen.blit(pauseImageBigEnd,pauseButtonBig)
            screen.blit(directionImage,directionRect)
            scoreText=pixelFontBig.render(f"score:{int(score):04d}",True,(255,255,255))
            screen.blit(scoreText,(15,200))
    else:
        
        startSceneRect=startSceneImage.get_rect(top=0,left=100)
        screen.blit(startSceneImage,startSceneRect)
        startText=pixelFontBig.render('start',True,startTextColor)
        startButton=startText.get_rect(center=(weith/2,height/2+100))
        pygame.draw.rect(screen, startButtonColor, startButton) #可以隐藏startButton        
        screen.blit(startText,startButton)
        
    #pygame.draw.circle(screen,(255,255,255),(260,180),50)
    # 刷新屏幕
    pygame.display.update()
# 设置窗口尺寸和标题
def StartMouseCheck():
    global is_clicked,is_hovered,isBegin,startButtonColor,timeNum,startTextColor
    if startButton.collidepoint(mouse_pos):
        is_hovered = True
        startButtonColor=(200,200,200)
        startTextColor=(0,188,188)
    else:
        is_hovered = False
        startButtonColor=(255,255,255)
        startTextColor=(0,255,255)
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if startButton.collidepoint(mouse_pos):
            is_clicked = True
            startButtonColor=(150,150,150)
            startTextColor=(0,100,100)
    elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:       
        if is_clicked and startButton.collidepoint(mouse_pos):
            # 在这里执行按钮点击后的操作
            isBegin=1
            timeNum=pygame.time.get_ticks()
            is_clicked = False
def pauseMouseCheck():
    global is_clicked,is_hovered,ispause,pauseButton,pauseImageEnd,pauseImageBigEnd
    rectindex=pygame.Rect(weith/2-90, height/2-150, 180, 300)
    if pauseButton.collidepoint(mouse_pos):
        is_hovered = True
        pauseImageEnd=pauseImageFill
    else:
        is_hovered = False
        pauseImageEnd=pauseImage
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if pauseButton.collidepoint(mouse_pos):
            is_clicked = True
            pauseImageEnd=pauseImageFill
    elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:       
        if is_clicked and pauseButton.collidepoint(mouse_pos):
            # 在这里执行按钮点击后的操作
            ispause=1-ispause
            is_clicked = False   
    if ispause:        
        if rectindex.collidepoint(mouse_pos):
            is_hovered = True
            pauseImageBigEnd=pauseImageBigFill
        else:
            is_hovered = False
            pauseImageBigEnd=pauseImageBig       
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if rectindex.collidepoint(mouse_pos):
                is_clicked = True
                pauseImageBigEnd=pauseImageBigFill
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:       
            if is_clicked and rectindex.collidepoint(mouse_pos):
            # 在这里执行按钮点击后的操作
                ispause=0
                is_clicked = False
def OverMouseCheck():
    global is_hovered,is_clicked,exitTextRect,exitColor,exitTextColor
    global restartTextRect,restartColor,restartTextColor
    if restartTextRect.collidepoint(mouse_pos):
        is_hovered = True
        restartColor=(50,50,50)
        restartTextColor=(0,205,205)
    else:
        is_hovered = False
        restartColor=(0,0,0)
        restartTextColor=(0,255,255)
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if restartTextRect.collidepoint(mouse_pos):
            is_clicked = True
            restartColor=(100,100,100)
            restartTextColor=(0,155,155)
    elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:       
        if is_clicked and restartTextRect.collidepoint(mouse_pos):
            # 在这里执行按钮点击后的操作
            initGame()
            print('ispressed')



    if exitTextRect.collidepoint(mouse_pos):
        is_hovered = True
        exitColor=(50,50,50)
        exitTextColor=(0,205,205)
    else:
        is_hovered = False
        exitColor=(0,0,0)
        exitTextColor=(0,255,255)
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if exitTextRect.collidepoint(mouse_pos):
            is_clicked = True
            exitColor=(100,100,100)
            exitTextColor=(0,155,155)
    elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:       
        if is_clicked and exitTextRect.collidepoint(mouse_pos):
            # 在这里执行按钮点击后的操作
            pygame.quit()
            sys.exit()
def autoAdd():
    global indexnum,starIndexNum,enemyBulletNum,isplayingMusic,playSceneMusicActual,musicIndexNum,musicStatus,isFire,isHit
    randomIndexNum=musicStatus
    if isBegin and not ispause:
        indexnum+=1
        starIndexNum+=1
        enemyBulletNum+=1
    if player.level<5:
        if indexnum>=7-player.level:
            enemy.add()
            indexnum=0
    else:
        if indexnum>=2:
            for i in range(int(player.level/5)):
                enemy.add()
            indexnum=0
    if starIndexNum>=5:
        star.add()
        if isFire==1:
            fireMusic.play()        
        starIndexNum=0
    if enemyBulletNum>=15:
        for i in range(player.level):
            enemy.fire()
        enemyBulletNum=0 
    if int(player.level/3)==musicIndexNum:
        musicIndexNum+=1
        playSceneMusicActual.stop()
        isplayingMusic=0
        while randomIndexNum==musicStatus:
            musicStatus=random.randint(0,len(playSceneMusic)-1)
        playSceneMusicActual=playSceneMusic[musicStatus]
    isFire=0
    isHit=0
def musicSelect():    
    global isendMusic,ispauseMusic,isplayingMusic
    if isBegin and pygame.mixer.get_busy():
        startSceneMusic.stop()
    if ispause and not ispauseMusic:
        pauseMusic.play(-1)
        ispauseMusic=1
    elif not ispause and ispauseMusic:
       pauseMusic.stop()
       ispauseMusic=0
    if isOver and not isendMusic:
        endMusic.play(-1)
        isendMusic=1
    if isBegin and not ispause and not isOver and not isplayingMusic:
        isplayingMusic=1
        playSceneMusicActual.set_volume(globalVolume)
        playSceneMusicActual.play(-1)
    elif (ispause or isOver) and isplayingMusic:
        isplayingMusic=0
        playSceneMusicActual.stop()
    if not ispause and not isOver and isBegin:
        if isHit==1:
            hitMusic.play()
    #if not isOver and not ispause and isBegin:
        #playingMusic(0)
player=player()
enemy=enemy()
star=star()
def initGame():
    global isOver,isBegin,ispause,enemyHeath
    player.init()
    star.init()
    enemy.init()
    isOver=0
    isBegin=0
    ispause=0
    enemyHeath=5
screen = pygame.display.set_mode((weith, height))
pygame.display.set_caption("雷霆战机 by 刘永洋")
pixelFont=pygame.font.SysFont("Algerian",25)
pixelFontBig=pygame.font.SysFont("Algerian",66)
# 创建一个Pygame时钟对象
clock = pygame.time.Clock()
# 设置目标帧率
target_fps = 30  # 这里设置为30帧/秒，可以根据需要调整
# 初始化矩形的位置和速度
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keysonce=pygame.key.get_pressed()
        player.getkeyonce(keysonce)
    mouse_pos = pygame.mouse.get_pos()
    if not isBegin:       
        StartMouseCheck() 
    else:
        pauseMouseCheck()
    if isOver:
        OverMouseCheck()
    # 检测键盘输入来移动矩形       
    #player.move()
    keys = pygame.key.get_pressed()
    player.getkey(keys)
    player.hitcheck()
    player.playerCheck()    
    enemy.selfcheck()
    enemy.enemyMove()
    player.bulletfly()
    enemy.bulletfly()
    star.starMove()
    musicSelect()
    autoAdd()
    if isOver:
        gameOverScene()
    else:
        drawing()
    clock.tick(target_fps)
# 退出Pygame
pygame.quit()
sys.exit()
