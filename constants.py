import pygame

#create games Titl and Icon
TITLE = "Checkers"
ICON = pygame.image.load("Resources/Images/Checkers-Logo.png")

#create the board dimensions
COLS, ROWS = 8, 8 #common board is 8 x 8
TILE_SIZE = 100
WIDTH, HEIGHT = COLS * TILE_SIZE, ROWS * TILE_SIZE
WINDOW_OFFSET = 0


#create colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 0)

#create piece images
RED_PIECE = pygame.image.load("Resources/Images/Red-Piece.png")
RED_KING_PIECE = pygame.image.load("Resources/Images/Red-King-Piece.png")
BLACK_PIECE = pygame.image.load("Resources/Images/Black-Piece.png")
BLACK_KING_PIECE = pygame.image.load("Resources/Images/Black-King-Piece.png")