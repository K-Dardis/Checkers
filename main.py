import pygame

#Initialise pygame
pygame.init()

#Create Window
WIN = pygame.display.set_mode((800, 800))

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

pygame.quit()
