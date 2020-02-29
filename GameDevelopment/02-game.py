import pygame
pygame.init()

width, height = 1000, 500
screen = pygame.display.set_mode((width,height))

red = 255,0,0
white = 255,255,255
black = 0,0,0

screen.fill(white)
rect = pygame.Rect(0,0,50,50)
while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            # quit pygame
            pygame.quit()
            # quit python
            quit()

    pygame.draw.rect(screen,red,[0,0,50,50])
    # pygame.draw.rect(screen, red, rect)
    pygame.draw.circle(screen,red,[200,200],50)

    pygame.display.flip()
