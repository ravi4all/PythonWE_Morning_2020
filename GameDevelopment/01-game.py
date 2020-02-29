# pip install pygame
import pygame
pygame.init()

width, height = 1000, 500
screen = pygame.display.set_mode((width,height))

red = 255,0,0
white = 255,255,255
black = 0,0,0

screen.fill(white)

# update screen with all the changes
pygame.display.flip()
