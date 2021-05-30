import pygame

WIDTH, HEIGHT = 800,900
FPS = 30
#colors
backGround = (51,51,51)
grid = (106,107,107)

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Tick Tack Toe")

WIN.fill(backGround)
pygame.display.update()

def drawGrid():
    pygame.draw.line(WIN, grid,(300,250),(300,850),12)
    pygame.draw.line(WIN, grid,(500,250),(500,850),12)
    pygame.draw.line(WIN, grid,(100,450),(700,450),12)
    pygame.draw.line(WIN, grid,(100,650),(700,650),12) 

def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = False

        drawGrid()
        pygame.display.update()
    pygame.QUIT()

if __name__ == "__main__":
    main()