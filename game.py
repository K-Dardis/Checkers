import pygame
from constants import *
from board import Board


class Game():

    def __init__(self, win):
        self.win = win
        self.board = Board()
        self.selected_piece = None
        
    def update(self):
        #Update the board
        self.board.draw_pieces(self.win)
        
        #Update the display
        pygame.display.update()
    
    def get_pos_on_board(self, pos):
        x, y = pos
        
        col = (x - WINDOW_OFFSET) // TILE_SIZE
        row = (y - WINDOW_OFFSET) // TILE_SIZE
        return row, col

    def select_tile(self, pos):
        #Check if have a piece selected
        row, col = self.get_pos_on_board(pos)
        if 0 <= row < ROWS and 0 <= col < COLS:
            self.select_piece(row, col)
    
    def select_piece(self, row, col):
        #Check if have a piece selected
        if self.selected_piece:
            if not self._move(row, col):
                self.selected_piece = None
                self.select_piece(row, col)

        #Select a piece if present
        piece = self.board.get_piece(row, col)
        if piece != 0:
            self.selected_piece = piece
            return True
        
        return False
    
    

    def _move(self, row, col):
        #check if you have a selected piece and the selected tile is free
        piece = self.board.get_piece(row, col)
        if piece == 0 and self.selected_piece:
            #Move piece to empty tile
            self.board.move_piece(self.selected_piece, row, col)
            return True
        return False
        