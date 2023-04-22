import pygame

#create the board dimensions
COLS, ROWS = 8, 8 #common board is 8 x 8
TILE_SIZE = 100
WIDTH, HEIGHT = COLS * TILE_SIZE, ROWS * TILE_SIZE

#Draw the board, at offset position
def draw_board(win, offset):
    pygame.draw.rect(win, (255, 255, 255), (offset, offset, WIDTH, HEIGHT))
    for row in range(ROWS):
        for col in range(row % 2, COLS, 2):
            pygame.draw.rect(win, (0, 0, 0), (row * TILE_SIZE + offset, col * TILE_SIZE + offset,  TILE_SIZE,  TILE_SIZE))
