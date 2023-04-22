import pygame
import board
from constants import BLUE

#Initialise pygame
pygame.init()

#Create Window
WIN = pygame.display.set_mode((1000, 1000))

#Set Title and Icon
win_title = "Checkers"
win_icon = pygame.image.load("Resources/Images/Checkers-Logo.png")

pygame.display.set_caption(win_title)
pygame.display.set_icon(win_icon)

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
    board.draw_board(WIN, 15)
    board.draw_pieces(WIN)
    #Update the display
    pygame.display.update()

pygame.quit()
