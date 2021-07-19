# from ..maps import Map
from ..piece import GamePiece


class Horse(GamePiece):
    """
    Represents the 'Horse' game piece.
    """
    def __init__(self, team, p_type, pos, x_offset, y_offset):
        super().__init__(team, p_type, pos, x_offset, y_offset)
        
    def get_img_offset(self):
        return self._x_offset, self._y_offset

    def get_valid_moves(self, board):
        """
        Returns a list of all valid moves the Horse GamePiece can make from its current position. Specifically, positions will be 
        added to the list that can be reached with valid movement and are either empty or occupied by an opposing team's GamePiece. 
        Spaces on the game board that are occupied by a GamePiece of the same team will not be added to the valid moves list.
        """
        pos = self.get_pos()                        # algebraic notation string representation (Ex: '1a')
        col, row = pos                              # unpacked tuple containing piece's grid prosition on the game board (Ex: 0, 0)
        valid_moves = []

        for i in range(-2, 3, 4):                   # length of move
            for j in range(-1, 2, 2):               # width of move
                for k in range(2):
                    if k % 2 == 0:                  # flips reference to rows and cols to calculate move at mirrored location
                        x, y = i, j
                    else: x, y = j, i
                
                    if col + x in board.board_ranges()[0] and row + y in board.board_ranges()[1]:
                        if x == i:
                            potential_block = board.get_space_contents((col + (i // 2), row))
                        else:
                            potential_block = board.get_space_contents((col, row + (i // 2)))
                        if potential_block == '---':
                            destination_space = board.get_space_contents((col + x, row + y))
                            if (isinstance(destination_space, GamePiece) and destination_space.get_team() != self.get_team()) or destination_space == '---':
                                valid_moves.append((col + x, row + y))

        return valid_moves

