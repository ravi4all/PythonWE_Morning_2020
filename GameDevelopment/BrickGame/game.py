import pygame
pygame.init()

width, height = 1000, 500
screen = pygame.display.set_mode((width,height))

red = 255,0,0
white = 255,255,255
black = 0,0,0

def main():
    barWidth = 100
    barHeight = 10
    barX = 0
    barY = 0
    barMoveX = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    barMoveX = 1
                elif event.key == pygame.K_LEFT:
                    barMoveX = -1

            else:
                barMoveX = 0

        screen.fill(white)
        pygame.draw.rect(screen,red,[barX,barY,50,50])
        barX += barMoveX

        if barX > width - 50:
            barMoveX = -1
        elif barX < 0:
            barMoveX = 1

        pygame.display.flip()

