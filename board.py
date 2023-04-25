import pygame
from constants import *
from piece import Piece


class Board():

    def __init__(self):
        self.boards_pieces = []
        self.red_pieces = 12
        self.black_pieces = 12
        self.set_board()

    #Draw the board, at offset position
    def draw_board(self, win):
        pygame.draw.rect(win, WHITE, (WINDOW_OFFSET, WINDOW_OFFSET, WIDTH, HEIGHT))
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, BLACK, (row * TILE_SIZE + WINDOW_OFFSET, col * TILE_SIZE + WINDOW_OFFSET,  TILE_SIZE,  TILE_SIZE))

    def set_board(self):
        #Remove all pieces from board
        self.boards_pieces = []
        #Set new pieces
        for row in range(ROWS):
                self.boards_pieces.append([])
                for col in range(COLS):
                    if col % 2 == ((row +  1) % 2):
                        if row < 3:
                            self.boards_pieces[row].append(Piece(row, col, BLACK))
                        elif row > ROWS - 4:
                            self.boards_pieces[row].append(Piece(row, col, RED))
                        else:
                            self.boards_pieces[row].append(0)
                    else:
                        #setting empty tiles that cant be used
                        self.boards_pieces[row].append(None )
    
    def get_piece(self, row, col):
        return self.boards_pieces[row][col]

    def move_piece(self, piece, row, col):
        self.boards_pieces[piece.row][piece.col], self.boards_pieces[row][col] = self.boards_pieces[row][col], self.boards_pieces[piece.row][piece.col]
        piece.move_piece(row, col)
        
        #If piece makes ot top the otherside of board they get Kinged
        if row == ROWS - 1 or row == 0:
            piece.king_piece()
    
    def remove_piece(self, pieces):
        for piece in pieces:
            self.boards_pieces[piece.row][piece.col] = 0
            if piece.colour == RED:
                self.red_pieces -= 1
            self.black_pieces -= 1

    def draw_pieces(self, win):
        self.draw_board(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.boards_pieces[row][col]
                if piece != 0 and piece != None:
                    piece.draw(win)
      
    def get_valid_moves(self, piece):
        moves = {}
        row = piece.row
        left = piece.col - 1
        right = piece.col + 1
        
        if piece.colour == RED or piece.king:
            moves.update(self._check_left(row - 1, max(row - 3, -1), -1, piece.colour, left))
            moves.update(self._check_right(row - 1, max(row - 3, -1), -1, piece.colour, right))
        if piece.colour == BLACK or piece.king:
            moves.update(self._check_left(row + 1, min(row + 3, ROWS), 1, piece.colour, left))
            moves.update(self._check_right(row + 1, min(row + 3, ROWS), 1, piece.colour, right))
    
        return moves
    
    def _check_left(self, start, stop, step, colour, left, skipped = []):
        moves = {}
        last = []
        for row in range(start, stop, step):
            if left < 0:
                break
            current = self.boards_pieces[row][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(row, left)] = last + skipped
                else:
                    moves[(row, left)] = last
                if last:
                    if step == -1:
                        new_stop = max(row-3, -1)
                    else:
                        new_stop = min(row+3, ROWS)
                    moves.update(self._check_left(row + step, new_stop, step, colour, left - 1, skipped = last))
                    moves.update(self._check_right(row + step, new_stop, step, colour, left + 1, skipped = last))
                break
            elif current.colour == colour:
                break
            else:
                last = [current]
            left -= 1
        return moves

    def _check_right(self, start, stop, step, colour, right, skipped = []):
        moves = {}
        last = []
        for row in range(start, stop, step):
            if right >= COLS:
                break
            current = self.boards_pieces[row][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(row, right)] = last + skipped
                else:
                    moves[(row, right)] = last
                if last:
                    if step == -1:
                        new_stop = max(row - 3, -1)
                    else:
                        new_stop = min(row + 3, ROWS)
                    moves.update(self._check_left(row + step, new_stop, step, colour, right - 1, skipped = last))
                    moves.update(self._check_right(row + step, new_stop, step, colour, right + 1, skipped = last))
                break
            elif current.colour == colour:
                break
            else:
                last = [current]
            right += 1
        return moves