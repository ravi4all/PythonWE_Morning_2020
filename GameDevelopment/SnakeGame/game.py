import pygame
import random
pygame.init()

width, height = 1000, 500
screen = pygame.display.set_mode((width,height))

red = 255,0,0
white = 255,255,255
black = 0,0,0

frog_img = pygame.image.load("frog.png")
frogWidth = frog_img.get_width()
frogHeight = frog_img.get_height()
frogX = random.randint(0,width - frogWidth)
frogY = random.randint(0,height - frogHeight)

x,y = 0,0
moveX = 0
moveY = 0
snakew = 50
snakeh = 50
snakeLen = 1
snakeList = []

coinSound = pygame.mixer.Sound('point.wav')

count = 0

clock = pygame.time.Clock()
FPS = 100

def drawSnake(snakeList):
    for i in range(len(snakeList)):
        pygame.draw.rect(screen,red,[snakeList[i][0],snakeList[i][1],
                                     snakew,snakeh])

def score(counter):
    font = pygame.font.SysFont(None,30)
    text = font.render("Score : {}".format(counter),True,black)
    screen.blit(text,(10,10))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moveX = 3
                moveY = 0
            elif event.key == pygame.K_LEFT:
                moveX = -3
                moveY = 0
            elif event.key == pygame.K_DOWN:
                moveY = 3
                moveX = 0
            elif event.key == pygame.K_UP:
                moveY = -3
                moveX = 0

    screen.fill(white)
    snakeRect = pygame.draw.rect(screen,red,[x,y,snakew,snakeh])
    screen.blit(frog_img,(frogX,frogY))
    frogRect = pygame.Rect(frogX,frogY,frogWidth,frogHeight)
    x += moveX
    y += moveY

    snakeHead = []
    snakeHead.append(x)
    snakeHead.append(y)

    snakeList.append(snakeHead)

    if len(snakeList) > snakeLen:
        del snakeList[0]

    drawSnake(snakeList)

    if snakeRect.colliderect(frogRect):
        frogX = random.randint(0, width - frogWidth)
        frogY = random.randint(0, height - frogHeight)
        FPS += 10
        snakeLen += 10
        count += 1
        coinSound.play()

    score(count)

    if x > width:
        x = -50
    elif x < -50:
        x = width
    elif y > height:
        y = -50
    elif y < -50:
        y = height

    pygame.display.flip()
    clock.tick(FPS)
