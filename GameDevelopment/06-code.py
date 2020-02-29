import pygame
pygame.init()

width, height = 1000, 500
screen = pygame.display.set_mode((width,height))

red = 255,0,0
white = 255,255,255
black = 0,0,0

img = pygame.image.load("football.png")

x,y = 0,0
moveX = 1
moveY = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)
    screen.blit(img,(x,y))
    x += moveX
    y += moveY

    if x > width - 100:
        moveX = -1
    elif x < 0:
        moveX = 1
    elif y > height - 100:
        moveY = -1
    elif y < 0:
        moveY = 1

    pygame.display.flip()

