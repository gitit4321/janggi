import pygame
from .board import Board
from .constants import DARK_GREEN, BLACK, WOOD, WIDTH, HEIGHT, SQUARE_SIZE
from .game_pieces import *


class JanggiGame:
    """
    Represents a Janggi game board.
    """
    def __init__(self, win):
        """
        Initialize game window (passed as param by calling funtion) and game data by calling 'init()' which has been 
        broken off into a separate class method to allow for the reseting of the game upon reaching end game. 
        """
        self._win = win
        self.init()

    def init(self):
        self._turn = 'b'                    # 'b' or 'r' (Blue or Red)
        self._selected = None               # will toggle between True and False once pieces have begun being selected
        self._game_state = 'UNFINISHED'     # 'UNFINISHED', 'RED_WON', or 'BLUE_WON'
        self._board = Board()               # initialize game board and game pieces
        self._valid_moves = []              # will hold valid moves for a selected piece (used to show valid moves for currently selected piece)

    def update(self):
        """
        Re-renders all board components, game pieces, and game state.
        """
        self._board.draw(self._win)
        self.draw_valid_moves(self._valid_moves)
        self.draw_game_state(self._win)
        pygame.display.update()

    def reset(self):
        """
        Resets the board to original 'start game' positions.
        """
        self.init()

    def select(self, pos):
        """
        Return True or False depending on if a piece is currently selected. 
        """
        # is game already over?
        if self.get_game_state() != 'UNFINISHED':
            return False

        # if a piece is currenlt selected, allows the option to select a different piece
        if self._selected:
            result = self.move(pos)
            if not result:
                self._selected = None
                self.select(pos)

        # set 'piece' to be the contents of the selected board space
        piece = self._board.get_space_contents(pos)

        # check that piece being selected is of the correct team and not an empty space
        if piece != '---' and piece.get_team() == self._turn:
            self._selected = piece
            self._valid_moves = self._board.get_valid_moves(piece)
            return True

        return False

    def move(self, pos):
        """
        Moves selected piece to desired location if it passes all game rules/logic and is valid.
        """
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
        """
        Renders all valid moves for the currently selected game piece to the screen as a small green dot.
        """
        for move in moves:
            col, row = move
            pygame.draw.circle(self._win, DARK_GREEN, ((col * SQUARE_SIZE + SQUARE_SIZE // 2), (row * SQUARE_SIZE + SQUARE_SIZE // 2)), 10)

    def draw_game_state(self, win):
        """
        Renders the current game state to the screen.
        """
        state = self.get_game_state()
        output = ''
        if state == 'UNFINISHED':
            turn = self.get_turn()
            if turn == 'b':
                player = 'Blue'
            else:
                player = 'Red'
            output = f"{player}'s Turn"
        elif state == 'RED_WON':
            output = 'Red Wins!'
        else:
            output = 'Blue Wins!'

        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(output, True, BLACK, WOOD)
        textRect = text.get_rect()
        textRect.center = (WIDTH//2, HEIGHT+45)
        win.blit(text, textRect)

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