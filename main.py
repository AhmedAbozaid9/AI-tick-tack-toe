import pygame
import mapCords

pygame.init()

WIDTH, HEIGHT = 800,800
FPS = 30

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Tick Tack Toe")

#colors
backGround = (51,51,51)
gridColor = (106,107,107)
textColor = (255,172,65)
#the header text
def renderHeader(displayedText):
    font = pygame.font.SysFont('Helvetica',42)
    text = font.render(displayedText,True,textColor)
    text_rect = text.get_rect(center=(WIDTH/2, 50))
    WIN.blit(text,text_rect)
    
#make the grid
def renderGrid():
    pygame.draw.line(WIN, gridColor,(290,200),(290,790),12)
    pygame.draw.line(WIN, gridColor,(500,200),(500,790),12)
    pygame.draw.line(WIN, gridColor,(100,400),(700,400),12)
    pygame.draw.line(WIN, gridColor,(100,600),(700,600),12) 

#add the input to the grid
def renderFigures(inputs):
    for input in len(inputs):
        if(input == 'X'): addX()

def addX(idx):
    pass

def addX(idx):
    pass

WIN.fill(backGround)
renderHeader('Choose your first move')
renderGrid()
pygame.display.update()

#the game loop
def main():
    run = True
    isPlayerTurn = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = False

            if(event.type == pygame.MOUSEBUTTONDOWN):
                mouseX = event.pos[0] 
                mouseY = event.pos[1]
                #add player input
                if(isPlayerTurn): pass
                #add the ai
                else: pass

        
if __name__ == "__main__":
    main()