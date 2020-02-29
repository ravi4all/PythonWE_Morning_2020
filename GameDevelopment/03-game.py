import pygame
pygame.init()

width, height = 1000, 500
screen = pygame.display.set_mode((width,height))

red = 255,0,0
white = 255,255,255
black = 0,0,0

screen.fill(white)

surface_1 = pygame.Surface((300,300))
surface_1.fill(red)
while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            # quit pygame
            pygame.quit()
            # quit python
            quit()

    screen.blit(surface_1,(100,100))
    pygame.draw.rect(surface_1, black, [0, 0, 50, 50])

    pygame.display.flip()
