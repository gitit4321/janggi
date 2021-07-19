from .constants import SQUARE_SIZE, RED, BLUE, GREY
from .game_pieces import *


class GamePiece:
    """
    The GamePiece class provides all of the baseline data and functionality of all inheriting game piece subclasses. 
    It is an abstract base class and should never by instatiated itself.
    """
    def __init__(self, team, p_type, pos, x_offset, y_offset):
        """
        Initialize private data members.
        """
        self._team = team               # 'r' or 'b'
        self._type = p_type             # two letter abbreviation for the type of piece. (Ex: General = 'Ge', Chariot = 'Ch')
        self._pos = pos                 # tuple containing the column and row or the given GamePiece object (Ex: (2, 3) = column 2, row 3))
        self._name = f"{team}{p_type}"  # combines team letter and piece type creating a team/piece specific identifier

        if self._team == 'r':
            self._color = RED
        else:
            self._color = BLUE
        
        self._x_offset = x_offset
        self._y_offset = y_offset
        self._x = 0
        self._y = 0
        self.calc_pg_pos()

    def __str__(self):
        """
        Returns a human readable name and position for a given GamePiece object.
        """
        return f"Name: {self._name} | Pos: {self._pos}"

    def __repr__(self):
        """
        Returns the name of a given GamePiece object.
        """
        return f"'{self._name}'"

    def get_team(self):
        """
        Returns the GamePiece obects team ('r' or 'b').
        """
        return self._team

    def get_name(self):
        """
        Returns the GamePiece objects name (Ex: 'bCa')
        """
        return self._name
    
    def get_type(self):
        """
        Returns the GamePiece type (Ex: 'El')
        """
        return self._type
    
    def get_color(self):
        """
        Returns the GamePiece color (Ex: 'RED', 'BLUE')
        """
        return self._color

    def get_pos(self):
        """
        Returns the gameboard position of a given GamePiece object. (Ex: (2, 3) = column 2, row 3))
        """
        return self._pos

    def get_pg_pos(self):
        """
        Returns the x and y coordinates of the given GamePieces object. (Used for image rendering)
        """
        return self._x, self._y

    def set_pos(self, pos):
        """
        Assigns the gameboard position of a given GamePiece object. (Ex: (2, 3) = column 2, row 3))
        """
        self._pos = pos

    def calc_pg_pos(self):
        """
        Assigns the x and y coordinates for GamePiece object image rendering.
        """
        col, row = self._pos
        self._x = SQUARE_SIZE * col + SQUARE_SIZE // 2 + self._x_offset
        self._y = SQUARE_SIZE * row + SQUARE_SIZE // 2 + self._y_offset

    def move(self, pos):
        """
        'Moves' a GamePiece by updating its grid position and x-y coordinates.
        """
        self.set_pos(pos)
        self.calc_pg_pos()