import pygame
import threading
from gameStatus import getGameState
import mapCords
from renderGame import renderFigures, renderGrid,renderHeader,clearGame,background

pygame.init()

WIDTH, HEIGHT = 800,800
FPS = 30

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Tick Tack Toe")

#the game rules

#the game 
def startGame():
    WIN.fill(background)
    renderHeader("you've been defeated 0 times",WIN)
    renderGrid(WIN)
    global inputs 
    inputs = ['','','','','','','','','']

startGame()
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
                
                state = getGameState(inputs)
                if(state == 'Tie' or state == 'X' or state == 'O'):
                    clearGame(state,WIN)
                else:
                    #add player input
                    if(isPlayerTurn): 
                        idx = mapCords.getIdx(mouseX,mouseY)
                        if (idx != None):
                            inputs[idx] = 'X'
                            renderFigures(inputs,WIN)
                    #add the ai     
                    else: 
                        pass

        pygame.display.update()
if __name__ == "__main__":
    main()