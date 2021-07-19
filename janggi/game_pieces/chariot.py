# from ..maps import Map
from ..piece import GamePiece


class Chariot(GamePiece):
    """
    Represents the 'Chariot' game piece.
    """
    def __init__(self, team, p_type, pos, x_offset, y_offset):
        super().__init__(team, p_type, pos, x_offset, y_offset)

    def get_img_offset(self):
        return self._x_offset, self._y_offset

    def get_valid_moves(self, board):
        """
        Returns a list of all valid moves the Chariot GamePiece can make from its current position. Specifically, positions will be 
        added to the list that can be reached with valid movement and are either empty or occupied by an opposing team's GamePiece. 
        Spaces on the game board that are occupied by a GamePiece of the same team will not be added to the valid moves list.
        """
        pos = self.get_pos()                 # algebraic notation string representation (Ex: '1a')
        col, row = pos                       # unpacked tuple containing piece's grid prosition on the game board (Ex: 0, 0)
        valid_moves = []

        # orthogonal traversals
        positive_traverse_range = range(1, 10)
        negative_traverse_range = range(-1, -10, -1)

        for i in range(2):                           # negative and positive traversal loop
            if i == 0:
                traverse = negative_traverse_range
            else:
                traverse = positive_traverse_range

            for j in range(2):                       # loop through rows (1st iteration) and columns (2nd iteration)
                if j == 0:
                    x = col
                    board_range = 0
                else:
                    x = row
                    board_range = 1

                for k in traverse:                                          
                    if x + k not in board.board_ranges()[board_range]:   
                        break
                    else:
                        if j == 0:
                            move_var = (x + k, row)
                        if j == 1:
                            move_var = (col, x + k)

                        space_contents = board.get_space_contents(move_var)
                        if (isinstance(space_contents, GamePiece)):
                            if space_contents.get_team() == self.get_team():
                                break
                            else:
                                valid_moves.append(move_var)
                                break
                        valid_moves.append(move_var)

        # diagonal fortress movement from corner positions
        for i in range(1, 3):
            coord_tup = None

            if pos == (3, 0) or pos == (3, 7):
                coord_tup = (col + i, row + i)
            if pos == (5, 0) or pos == (5, 7):
                coord_tup = (col - i, row + i)
            if pos == (3, 2) or pos == (3, 9):
                coord_tup = (col + i, row - i)
            if pos == (5, 2) or pos == (5, 9):
                coord_tup = (col - i, row - i)

            if coord_tup == None:
                break
            else:
                space_contents = board.get_space_contents(coord_tup)
                if (isinstance(space_contents, GamePiece) and space_contents.get_team() == self.get_team()):
                    break
                elif (isinstance(space_contents, GamePiece) and space_contents.get_team() != self.get_team()):
                    valid_moves.append(coord_tup)
                    break
                else:
                    valid_moves.append(coord_tup)

        # diagonal fortress movement from center of fortress
        if pos == (4, 1) or pos == (4, 8):
            for i in range(-1, 2, 2):
                for j in range(-1, 2, 2):
                    space_contents = board.get_space_contents((col + j, row + i))
                    if isinstance(space_contents, GamePiece) and space_contents.get_team() == self.get_team():
                        continue
                    valid_moves.append((col + j, row + i))

        return valid_moves
