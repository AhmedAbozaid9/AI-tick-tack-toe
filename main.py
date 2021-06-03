import pygame
import threading
from gameStatus import getGameState
import mapCords
from AI import computerChoice
from renderGame import renderFigures, renderGrid,renderHeader,clearGame,background

pygame.init()

WIDTH, HEIGHT = 800,800
FPS = 5

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Tick Tack Toe")

#the game rules

#the game 
def startGame():
    WIN.fill(background)
    renderHeader("you've been defeated 0 times",WIN)
    renderGrid(WIN)
    global board
    board = ['','','','','','','','','']

def checkWin(state):
    if(state == 'Tie' or state == 'X' or state == 'O'):
            clearGame(state,WIN)
            threading.Timer(1.0,startGame).start()

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

            if(event.type == pygame.MOUSEBUTTONDOWN and isPlayerTurn):
                mouseX = event.pos[0] 
                mouseY = event.pos[1]
                #add player input
                idx = mapCords.getIdx(mouseX,mouseY)
                if (idx != None and board[idx] == ''):
                    board[idx] = 'X'
                    renderFigures(board,WIN)
                    state = getGameState(board)
                    isPlayerTurn = False
                    checkWin(state)
        #add the ai     
        if(not isPlayerTurn): 
            idx = computerChoice(board)
            board[idx] = 'O'
            renderFigures(board,WIN)
            state = getGameState(board)
            checkWin(state)
            isPlayerTurn = True
            
        pygame.display.update()
        
if __name__ == "__main__":
    main()