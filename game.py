import pygame
from constants import *
from board import Board


class Game():

    def __init__(self, win):
        self.win = win
        self.board = Board()
        self.selected_piece = None
        self.player = RED
        
    def update(self):
        #Update the board
        self.board.draw_pieces(self.win)
        
        #Update the display
        pygame.display.update()

    def reset(self):
        self.board.set_board()
    
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
        if piece != None and piece != 0: 
            if piece.colour == self.player:
                self.selected_piece = piece
                return True
            
        return False
    
    def _move(self, row, col):
        #check if you have a selected piece and the selected tile is free
        piece = self.board.get_piece(row, col)
        if piece == 0 and self.selected_piece:
            #Move piece to empty tile
            if self.is_valid_move(self.selected_piece, row, col):
                self.board.move_piece(self.selected_piece, row, col)
                self.change_player()
                self.selected_piece = None
                return True
        return False
    
    def is_valid_move(self, piece, row, col):
        if self.selected_piece.colour == RED:
            if row == piece.row - 1 and (col == piece.col + 1 or col == piece.col - 1):
                return True
        if self.selected_piece.colour == BLACK:
            if row == piece.row + 1 and (col == piece.col + 1 or col == piece.col - 1):
                return True
        return False
    
    def change_player(self):
        if self.player == RED:
            self.player = BLACK
        else:
            self.player = RED