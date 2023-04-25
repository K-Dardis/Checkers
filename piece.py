import pygame
from constants import *

class Piece:
    def __init__(self, row, col, colour):
        self.row = row
        self.col = col
        self.colour = colour
        self.king = False
        self.x = TILE_SIZE * self.col + WINDOW_OFFSET
        self.y = TILE_SIZE * self.row + WINDOW_OFFSET
    
    def king_piece(self):
        self.king = True

    def draw(self, win):
        if self.colour == RED:
            win.blit(RED_PIECE, (self.x , self.y))
            if self.king == True:
                win.blit(RED_KING_PIECE, (self.x , self.y))                    
        else:
            win.blit(BLACK_PIECE, (self.x , self.y))
            if self.king == True:
                win.blit(BLACK_KING_PIECE, (self.x , self.y))
        

    def move_piece(self, row, col):
        self.row = row
        self.col = col
        self.x = TILE_SIZE * self.col + WINDOW_OFFSET
        self.y = TILE_SIZE * self.row + WINDOW_OFFSET
    
    def __repr__(self):
        return str(self.color)

