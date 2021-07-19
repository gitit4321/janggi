import pygame

from .board import Board
from .constants import GREEN, SQUARE_SIZE
from .game_pieces import *
from .piece import GamePiece



class JanggiGame:
    """
    Represents a Janggi game board. Includes overall game data such as current player turn and the current game state.
    """
    def __init__(self, win):
        """
        Initialize private data member '_board'. It is first populated with the 'board' class variable's empty list and then populated by class method 
        'populate_board' which takes the 'initialize_pieces_list' class method as a parameter. The latter creates a list of GamePiece objects and then the 
        former places them in the proper location for the start of a game.
        """
        self._init()
        self._win = win

    def update(self):
        self._board.draw(self._win)
        self.draw_valid_moves(self._valid_moves)
        pygame.display.update()

    def _init(self):
        self._turn = 'b'                                # 'b' or 'r' (Blue or Red)
        self._selected = None
        self._game_state = 'UNFINISHED'                 # 'UNFINISHED', 'RED_WON', or 'BLUE_WON'
        self._board = Board()
        self._valid_moves = []

    def reset(self):
        self._init()

    def select(self, pos):
        # is game already over?
        if self.get_game_state() != 'UNFINISHED':
            return False

        if self._selected:
            result = self._move(pos)
            if not result:
                self._selected = None
                self.select(pos)

        piece = self._board.get_space_contents(pos)
        if piece != '---' and piece.get_team() == self._turn:
            self._selected = piece
            self._valid_moves = self._board.get_valid_moves(piece)
            return True

        return False

    def _move(self, pos):
        space_contents = self._board.get_space_contents(pos)
        if self._selected and pos in self._valid_moves:
            if self._board.make_move(self._selected.get_pos(), pos):
                self._board.move(self._selected, pos)
                if self._board.get_checkmate():
                    self.set_game_state(self._board.get_winner())
                else:
                    self.set_next_turn()
        else:
            return False
        
        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            col, row = move
            pygame.draw.circle(self._win, GREEN, ((col * SQUARE_SIZE + SQUARE_SIZE // 2), (row * SQUARE_SIZE + SQUARE_SIZE // 2)), 10)

    def get_board(self):
        """
        Return raw board representation. (For use by program).
        """
        return self._board

    def get_game_state(self):
        """
        Returns th game state. ('UNFINISHED', 'RED_WON', or 'BLUE_WON').
        """
        return self._game_state

    def get_turn(self):
        """
        Returns which players turn it currently is.
        """
        return self._turn

    def set_next_turn(self):
        """
        Updates the '_turn' after a valid move.
        """
        if self.get_turn() == 'r':
            self._turn = 'b'
        else:
            self._turn = 'r'
        self._valid_moves = []

    def set_game_state(self, winner):
        """
        Updates the game state to show which team won in the event of a checkmate.
        """
        if winner == 'red':
            self._game_state = "RED_WON"
        else:
            self._game_state = "BLUE_WON"






# remove??
    # def get_moves_dict(self):
    #     """
    #     Creates and returns a dictionary composed of two nested dicitonaries containing all poissble moved for both teams. 
    #     Dictionary keys are board spaces (Ex: (3, 5)) and values are a list of all objects that can reach that space with a 
    #     valid move (Ex: [bEl, bSo, bCa]).
    #     """
    #     moves_dict = {}
    #     moves_dict['red'] = {}
    #     moves_dict['blue'] = {}
    #     board = self.get_board()
        
    #     for i in range(2):
    #         if i == 0:
    #             team = 'red'
    #         else:
    #             team = 'blue'
    #         for piece in board.get_pieces_on_board()[i]:
    #             for space in piece.get_valid_moves(self):
    #                 if space not in moves_dict[team]:
    #                     moves_dict[team][space] = [piece]
    #                 else:
    #                     moves_dict[team][space].extend([piece])
        
    #     return moves_dict
