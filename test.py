import pygame
import sys

class bullet:
    def __init__(self,direction,x=200,y=200):
        self.direction=direction
        self.x=x
        self.y=y
    def drawbullet(self):
        pygame.draw.circle(screen,(0,255,255),(self.x,self.y),50)
# 初始化Pygame
pygame.init()

# 设置窗口尺寸和标题
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Pygame Example")
# 创建一个Pygame时钟对象
clock = pygame.time.Clock()
# 设置目标帧率
target_fps = 30  # 这里设置为30帧/秒，可以根据需要调整
# 初始化矩形的位置和速度
rect_x, rect_y = 400, 300
rect_speed = 10
bullets=[]
direction=0#左>0 右>1 上>2 下>3

def getkey(keys):
    global rect_x
    global rect_y
    global direction
    global bullets
    if keys[pygame.K_LEFT]:#左
        rect_x -= rect_speed
        direction=0
    if keys[pygame.K_RIGHT]:#右
        rect_x += rect_speed
        direction=1
    if keys[pygame.K_UP]:#上
        rect_y -= rect_speed
        direction=2
    if keys[pygame.K_DOWN]:#下
        rect_y += rect_speed
        direction=3
    if keys[pygame.K_SPACE]:#空格
        bullets.append(bullet(direction,int(rect_x),int(rect_y)))
def drawing():
    global bullets
    # 清屏
    screen.fill((0, 255, 0))
    # 绘制矩形
    pygame.draw.rect(screen, (255, 0, 0), (rect_x, rect_y, 50, 50))
    #pygame.draw.circle(screen,(0,255,255),(200,200),50)
    for obj in enumerate(bullets):
        if isinstance(obj, bullet):
            obj.drawbullet()
    # 刷新屏幕
    pygame.display.update()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # 检测键盘输入来移动矩形
    keys = pygame.key.get_pressed()
    getkey(keys)
    drawing()
    clock.tick(target_fps)

# 退出Pygame
pygame.quit()
sys.exit()
