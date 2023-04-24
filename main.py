import pygame
from game import Game
from constants import BLUE, TITLE, ICON, WIDTH, HEIGHT, WINDOW_OFFSET, TILE_SIZE

#Initialise pygame
pygame.init()

#Create Window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#Set Title and Icon
pygame.display.set_caption(TITLE)
pygame.display.set_icon(ICON)



def main():
    #fill in the background as blue for now.
    WIN.fill(BLUE)

    #initilise game
    game = Game(WIN)
    
    #Create Game loop
    running = True
    while running:
        
        for event in pygame.event.get():
            #Check if the Window has been closed
            if event.type == pygame.QUIT:
                running = False
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                game.select_tile(pygame.mouse.get_pos())

        #Exit if escape key is pressed
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_ESCAPE]:
            running = False
        if key_pressed[pygame.K_r]:
            game.reset()
        
        game.update()

    pygame.quit()

main()