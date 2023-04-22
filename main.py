import pygame

#Initialise pygame
pygame.init()

#Create Window
WIN = pygame.display.set_mode((800, 800))

#Create Game loop
running = True
while running:
    for event in pygame.event.get():
        #Check if the Window has been closed
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
