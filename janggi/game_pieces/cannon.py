# from ..maps import Map
from ..piece import GamePiece


class Cannon(GamePiece):
    """
    Represents the 'Cannon' game piece.
    """
    def __init__(self, team, p_type, pos, x_offset, y_offset):
        super().__init__(team, p_type, pos, x_offset, y_offset)
    
    def get_img_offset(self):
        return self._x_offset, self._y_offset

    def get_valid_moves(self, board):
        """
        Returns a list of all valid moves the Cannon GamePiece can make from its current position. Specifically, positions will be 
        added to the list that can be reached with valid movement and are either empty or occupied by an opposing team's GamePiece. 
        Spaces on the game board that are occupied by a GamePiece of the same team will not be added to the valid moves list.
        """
        pos = self.get_pos()
        col, row = pos             # unpacked tuple containing piece's grid prosition on the game board (Ex: 0, 0)
        valid_moves = []

        # orthogonal traversals
        positive_traverse_range = range(1, 10)
        negative_traverse_range = range(-1, -10, -1)

        # positive row traverse loop
        for i in range(2):
            if i == 0:
                traverse = negative_traverse_range
            else:
                traverse = positive_traverse_range

            for j in range(2):                  # loop through columns (1st iteration) and rows (2nd iteration)
                if j == 0:
                    x = col
                    board_range = 0
                else:
                    x = row
                    board_range = 1
                
                jump_count = 0
                for k in traverse:
                    if x + k not in board.board_ranges()[board_range]:
                        jump_count = 0
                        break
                    else:
                        if j == 0:
                            move_var = (x + k, row)
                        if j == 1:
                            move_var = (col, x + k)

                        # if jump_count >= 2:
                            # break
                        space_contents = board.get_space_contents(move_var)
                        if isinstance(space_contents, Cannon):
                            jump_count = 0
                            break
                        if jump_count == 0:
                            if space_contents == '---':
                                continue
                            else:
                                jump_count += 1
                        elif jump_count == 1:
                            if space_contents == '---':
                                valid_moves.append(move_var)
                            elif space_contents.get_team() != self.get_team():
                                if isinstance(space_contents, Cannon):
                                    jump_count += 1
                                    continue
                                valid_moves.append(move_var)
                                jump_count += 1
                            else:
                                jump_count = 0
                                break
                        else:
                            jump_count = 0
                            break

        coord_tup = None

        if pos == (3, 0) or pos == (3, 7):
            coord_tup = (col + 2, row + 2)
        if pos == (5, 0) or pos == (5, 9):
            coord_tup = (col - 2, row + 2)
        if pos == (3, 2) or pos == (3, 9):
            coord_tup = (col + 2, row - 2)
        if pos == (5, 2) or pos == (5, 9):
            coord_tup = (col - 2, row - 2)
        
        if coord_tup is not None:
            space_contents = board.get_space_contents(coord_tup)
            if space_contents == '---' or space_contents.get_team() != self.get_team():
                if (row <= 2 and (board.get_space_contents((4, 1)) != '---') or (not isinstance(board.get_space_contents((4, 1)), Cannon))):
                    valid_moves.append(coord_tup)
                if row >= 7 and (board.get_space_contents((4, 8)) != '---' or (not isinstance(board.get_space_contents((4, 8)), Cannon))):
                    valid_moves.append(coord_tup)

        return valid_moves
