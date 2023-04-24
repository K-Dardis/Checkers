import pygame
from constants import *
from board import Board


class Game():

    def __init__(self, win):
        self.win = win
        self.board = Board()
        self.selected_piece = None
        self.player = RED
        self.valid_moves = {}
        
    def update(self):
        #Update the board
        self.board.draw_pieces(self.win)
        self.draw_moves(self.valid_moves)
        
        #Update the display
        pygame.display.update()

    def reset(self):
        self.board.set_board()
        self.selected_piece = None
        self.player = RED
        self.valid_moves = {}

    def select_tile(self, pos):
        #Check if have a piece selected
        x, y = pos
        col = (x - WINDOW_OFFSET) // TILE_SIZE
        row = (y - WINDOW_OFFSET) // TILE_SIZE
        if 0 <= row < ROWS and 0 <= col < COLS:
            self.select_piece(row, col)
    
    def select_piece(self, row, col):
        #Check if have a piece selected
        if self.selected_piece:
            result = self._move(row, col)
            if not result:
                self.selected_piece = None
                self.select_piece(row, col)

        #Select a piece if present
        piece = self.board.get_piece(row, col)
        if piece != None and piece != 0 and piece.colour == self.player:
                self.selected_piece = piece
                self.valid_moves = self.board.get_valid_moves(piece)
                return True
            
        return False
    
    def _move(self, row, col):
        #check if you have a selected piece and the selected tile is free
        piece = self.board.get_piece(row, col)
        if self.selected_piece and piece == 0 and (row, col) in self.valid_moves:
            #Move piece to empty tile
            self.board.move_piece(self.selected_piece, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove_piece(skipped)
            self.change_player()
            return True
        return False
    
    def draw_moves(self, moves):
        for move in moves:
            row, col = move
            self.win.blit(BORDER, (col * TILE_SIZE + WINDOW_OFFSET, row * TILE_SIZE + WINDOW_OFFSET))
    
    def change_player(self):
        self.valid_moves = {}
        if self.player == BLACK:
            self.player = RED
        else:
            self.player = BLACK