import pygame
from constants import *
from piece import Piece



piece = Piece(1, 1, RED)
piece2 = Piece(2, 2, BLACK)

#Draw the board, at offset position
def draw_board(win, offset):
    pygame.draw.rect(win, WHITE, (offset, offset, WIDTH, HEIGHT))
    for row in range(ROWS):
        for col in range(row % 2, COLS, 2):
            pygame.draw.rect(win, BLACK, (row * TILE_SIZE + offset, col * TILE_SIZE + offset,  TILE_SIZE,  TILE_SIZE))

def draw_pieces(win):
    piece.draw(win)
    piece2.king_piece()
    piece2.draw(win)
