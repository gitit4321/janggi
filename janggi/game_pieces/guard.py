# from ..maps import Map
from ..piece import GamePiece


class Guard(GamePiece):
    """
    Represents the 'Guard' game piece.
    """
    def __init__(self, team, p_type, pos, x_offset, y_offset):
        super().__init__(team, p_type, pos, x_offset, y_offset)
    
    def get_img_offset(self):
        return self._x_offset, self._y_offset

    def get_valid_moves(self, board):
        """
        Returns a list of all valid moves the Guard GamePiece can make from its current position. Specifically, positions will be 
        added to the list that can be reached with valid movement and are either empty or occupied by an opposing team's GamePiece. 
        Spaces on the game board that are occupied by a GamePiece of the same team will not be added to the valid moves list.
        """
        pos = self.get_pos()                 # algebraic notation string representation (Ex: '1a')
        col, row = pos                       # unpacked tuple containing piece's grid prosition on the game board (Ex: 0, 0)
        valid_moves = []


        for i in range(-1, 2):                  # row range
            for j in range(-1, 2):              # column range

                if col + j in board.fortress_ranges()[0] and (row + i in board.fortress_ranges()[1] or row + i in board.fortress_ranges()[2]):
                    if (row + i , col + j) == (row, col):
                        continue
                    if (pos == (4, 2) or pos == (5, 1) or pos == (4, 9) or pos == (5, 8)) and (i == -1 and j == -1):
                        continue
                    if (pos == (4, 2) or pos == (3, 1) or pos == (4, 9) or pos == (3, 8)) and (i == -1 and j == 1):
                        continue
                    if (pos == (4, 0) or pos == (5, 1) or pos == (4, 7) or pos == (5, 8)) and (i == 1 and j == -1):
                        continue
                    if (pos == (4, 0) or pos == (3, 1) or pos == (4, 7) or pos == (3, 8)) and (i == 1 and j == 1):
                        continue
                    space_contents = board.get_space_contents((col + j, row + i))
                    if isinstance(space_contents, GamePiece) and space_contents.get_team() == self.get_team():
                        continue
                    valid_moves.append((col + j, row + i))

        return valid_moves
