import pygame
from constants import *

class Piece:
    def __init__(self, row, col, colour):
        self.row = row
        self.col = col
        self.colour = colour
        self.king = False
        self.x = TILE_SIZE * self.col + 15
        self.y = TILE_SIZE * self.row + 15
    
    def king_piece(self):
        self.king = True

    def draw(self, win):
        if self.colour == RED:
            if self.king == True:
                win.blit(RED_KING_PIECE, (self.x , self.y))    
            win.blit(RED_PIECE, (self.x , self.y))
        elif self.king == True:
            win.blit(BLACK_KING_PIECE, (self.x , self.y))
        else:
            win.blit(BLACK_PIECE, (self.x , self.y))
