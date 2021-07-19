# from ..maps import Map
from ..piece import GamePiece


class Soldier(GamePiece):
    """
    Represents the 'Soldier' game piece.
    """
    def __init__(self, team, p_type, pos, x_offset, y_offset):
        super().__init__(team, p_type, pos, x_offset, y_offset)
    
    def get_img_offset(self):
        return self._x_offset, self._y_offset

    def get_valid_moves(self, board):
        """
        Returns a list of all valid moves the Soldier GamePiece can make from its current position. Specifically, positions will be 
        added to the list that can be reached with valid movement and are either empty or occupied by an opposing team's GamePiece. 
        Spaces on the game board that are occupied by a GamePiece of the same team will not be added to the valid moves list.
        """
        pos = self.get_pos()                 # algebraic notation string representation (Ex: '1a')
        col, row = pos                       # unpacked tuple containing piece's grid prosition on the game board (Ex: 0, 0)
        valid_moves = []

        if self.get_team() == 'r':
            row_range = range(0, 2)             
            fortress_rows = 2                   # blue fortress
        else:
            row_range = range(0, -2, -1)
            fortress_rows = 1                   # red fortress

        for i in row_range:                     # row range of piece movement (postive for red team, negative for blue)
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if (col + j in board.board_ranges()[0]) and (row + i in board.board_ranges()[1]):
                    if (i > 0 and j != 0) or (i < 0 and j != 0):        # diagonals
                        if (col in board.fortress_ranges()[0] and row in board.fortress_ranges()[fortress_rows]) and (col + j in board.fortress_ranges()[0] and row + i in board.fortress_ranges()[fortress_rows]):
                            if pos == (3, 1) or pos == (5, 1) or pos == (4, 2) or pos == (4, 7) or pos == (3, 8) or pos == (5, 8):
                                continue
                        else:
                            continue
                    space_contents = board.get_space_contents((col + j, row + i))
                    if isinstance(space_contents, GamePiece) and space_contents.get_team() == self.get_team():
                        continue
                    valid_moves.append((col + j, row + i))

        return valid_moves
