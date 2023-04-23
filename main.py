import pygame
from board import Board
from constants import BLUE, TITLE, ICON, WIDTH, HEIGHT

#Initialise pygame
pygame.init()

#Create Window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#Set Title and Icon
pygame.display.set_caption(TITLE)
pygame.display.set_icon(ICON)

#create game board
Board = Board()

#Create Game loop
running = True
while running:
    
    for event in pygame.event.get():
        #Check if the Window has been closed
        if event.type == pygame.QUIT:
            running = False
    #fill in the background as blue for now.
    WIN.fill(BLUE)
    #draw the board onto the window
    Board.draw_board(WIN)
    Board.draw_pieces(WIN)
    #Update the display
    pygame.display.update()

pygame.quit()
