import pygame
import threading
import mapCords
from gameStatus import getGameState

#colors
background = (51,51,51)
gridColor = (106,107,107)
textColor = (135,167,179)
player1Color = (3, 177,252)
player2Color = (219,11,49)

#the header text
def renderHeader(displayedText,WIN):
    font = pygame.font.SysFont('Helvetica',42)
    text = font.render(displayedText,True,textColor)
    textRect = text.get_rect(center=(800/2, 50))
    WIN.blit(text,textRect)
    
#make the grid
def renderGrid(WIN):
    pygame.draw.line(WIN, gridColor,(290,200),(290,790),12)
    pygame.draw.line(WIN, gridColor,(500,200),(500,790),12)
    pygame.draw.line(WIN, gridColor,(100,400),(700,400),12)
    pygame.draw.line(WIN, gridColor,(100,600),(700,600),12) 

#show figures on the screen
def renderFigures(inputs,WIN):
    font = pygame.font.SysFont('Helvetica',150)
    for idx in range(0,9):
        if(inputs[idx] == 'X'):
            text = font.render('X',True,player1Color)
            textRect = text.get_rect(center = (mapCords.getCenter(idx)[0],mapCords.getCenter(idx)[1]))
            WIN.blit(text,textRect)
        elif(inputs[idx] == 'O'):
            text = font.render('O',True,player2Color)
            textRect = text.get_rect(center = (mapCords.getCenter(idx)[0],mapCords.getCenter(idx)[1]))
            WIN.blit(text,textRect)

def clearGame(state,WIN):
    WIN.fill(background)
    if(state == 'X' or state == 'O'): state += ' Wins'
    renderHeader(state,WIN)


