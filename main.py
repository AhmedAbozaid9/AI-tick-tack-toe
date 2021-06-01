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
    global inputs, available
    inputs = ['','','','','','','','','']
    available = [0,1,2,3,4,5,6,7,8]

startGame()
#the game loop
def main():
    run = True
    isPlayerTurn = True
    global state
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
                if(isPlayerTurn): 
                    idx = mapCords.getIdx(mouseX,mouseY)
                    if (idx != None and idx in available):
                        inputs[idx] = 'X'
                        renderFigures(inputs,WIN)
                        state = getGameState(inputs)
                        available.remove(idx)
                        isPlayerTurn = False

                #add the ai     
                else: 
                    pass
                if(state == 'Tie' or state == 'X' or state == 'O'):
                    clearGame(state,WIN)
                    threading.Timer(1.0,startGame).start()
                    isPlayerTurn = True

        pygame.display.update()
        
if __name__ == "__main__":
    main()