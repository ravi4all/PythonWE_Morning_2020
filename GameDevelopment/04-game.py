import pygame
pygame.init()

width, height = 1000, 500
screen = pygame.display.set_mode((width,height))

red = 255,0,0
white = 255,255,255
black = 0,0,0

x,y = 0,0
moveX = 1
moveY = 0.5
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)
    pygame.draw.rect(screen,red,[x,y,50,50])
    x += moveX
    y += moveY

    if x > width - 50:
        moveX = -1
    elif x < 0:
        moveX = 1
    elif y > height - 50:
        moveY = -0.5
    elif y < 0:
        moveY = 0.5

    pygame.display.flip()

