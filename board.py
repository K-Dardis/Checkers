import pygame
from constants import *
from piece import Piece


class Board():

    def __init__(self):
        self.boards_pieces = []
        self.set_board()

    #Draw the board, at offset position
    def draw_board(self, win):
        pygame.draw.rect(win, WHITE, (WINDOW_OFFSET, WINDOW_OFFSET, WIDTH, HEIGHT))
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, BLACK, (row * TILE_SIZE + WINDOW_OFFSET, col * TILE_SIZE + WINDOW_OFFSET,  TILE_SIZE,  TILE_SIZE))

    def set_board(self):
        for row in range(ROWS):
                self.boards_pieces.append([])
                for col in range(COLS):
                    if col % 2 == ((row +  1) % 2):
                        if row < 3:
                            self.boards_pieces[row].append(Piece(row, col, WHITE))
                        elif row > ROWS - 4:
                            self.boards_pieces[row].append(Piece(row, col, RED))
                        else:
                            self.boards_pieces[row].append(0)
                    else:
                        self.boards_pieces[row].append(0)


    def draw_pieces(self, win):
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.boards_pieces[row][col]
                if piece != 0:
                    piece.draw(win)