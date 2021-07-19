import pygame
from .constants import *
from .game_pieces import general, guard, horse, elephant, chariot, cannon, soldier


class Board:
    def __init__(self):
        """
        Initialize game board and relevant metadata
        """
        self._board = [
            ['---', '---', '---', '---', '---', '---', '---', '---', '---'],
            ['---', '---', '---', '---', '---', '---', '---', '---', '---'],
            ['---', '---', '---', '---', '---', '---', '---', '---', '---'],
            ['---', '---', '---', '---', '---', '---', '---', '---', '---'],
            ['---', '---', '---', '---', '---', '---', '---', '---', '---'],
            ['---', '---', '---', '---', '---', '---', '---', '---', '---'],
            ['---', '---', '---', '---', '---', '---', '---', '---', '---'],
            ['---', '---', '---', '---', '---', '---', '---', '---', '---'],
            ['---', '---', '---', '---', '---', '---', '---', '---', '---'],
            ['---', '---', '---', '---', '---', '---', '---', '---', '---'],
        ]
        self._pieces = self.initialize_pieces_list()    # create list of all necessary GamePiece objects
        self.populate_board(self._pieces)               # place GamePiece objects on their proper starting locations on the board
        self._checkmate = False                         # checkmate check
        self._winner = None                             # 'red' or 'blue'

    def initialize_pieces_list(self):
        """
        Initializes and returns a list containg two sub-lists. The first holds all GamePiece objects for player 'r' and 
        the second for player 'b'.
        """

        game_pieces = []
        red_pieces = (
            [general.General('r', 'Ge', (4, 1), -40, -43)] + 
            [guard.Guard('r', 'Gu', (3, 0), -24, -26)] +
            [guard.Guard('r', 'Gu', (5, 0), -24, -26)] +
            [horse.Horse('r', 'Ho', (2, 0), -33, -36)] +
            [horse.Horse('r', 'Ho', (7, 0), -33, -36)] +
            [elephant.Elephant('r', 'El', (1, 0), -33, -36)] + 
            [elephant.Elephant('r', 'El', (6, 0), -33, -36)] + 
            [chariot.Chariot('r', 'Ch', (0, 0), -33, -36)] + 
            [chariot.Chariot('r', 'Ch', (8, 0), -33, -36)] + 
            [cannon.Cannon('r', 'Ca', (1, 2), -33, -36)] + 
            [cannon.Cannon('r', 'Ca', (7, 2), -33, -36)] + 
            [soldier.Soldier('r', 'So', (0, 3), -24, -26)] +
            [soldier.Soldier('r', 'So', (2, 3),-24, -26)] +
            [soldier.Soldier('r', 'So', (4, 3), -24, -26)] +
            [soldier.Soldier('r', 'So', (6, 3), -24, -26)] +
            [soldier.Soldier('r', 'So', (8, 3), -24, -26)]
            )

        blue_pieces = (
            [general.General('b', 'Ge', (4, 8), -40, -43)] + 
            [guard.Guard('b', 'Gu', (3, 9), -24, -26)] +
            [guard.Guard('b', 'Gu', (5, 9), -24, -26)] +
            [horse.Horse('b', 'Ho', (2, 9), -33, -36)] +
            [horse.Horse('b', 'Ho', (7, 9), -33, -36)] +
            [elephant.Elephant('b', 'El', (1, 9), -33, -36)] + 
            [elephant.Elephant('b', 'El', (6, 9), -33, -36)] + 
            [chariot.Chariot('b', 'Ch', (0, 9), -33, -36)] + 
            [chariot.Chariot('b', 'Ch', (8, 9), -33, -36)] + 
            [cannon.Cannon('b', 'Ca', (1, 7), -33, -36)] + 
            [cannon.Cannon('b', 'Ca', (7, 7), -33, -36)] + 
            [soldier.Soldier('b', 'So', (0, 6), -24, -26)] +
            [soldier.Soldier('b', 'So', (2, 6), -24, -26)] +
            [soldier.Soldier('b', 'So', (4, 6), -24, -26)] +
            [soldier.Soldier('b', 'So', (6, 6), -24, -26)] +
            [soldier.Soldier('b', 'So', (8, 6), -24, -26)]
            )
            
        game_pieces += red_pieces, blue_pieces

        return game_pieces
    
    def populate_board(self, pieces_list):
        """
        Takes a list composed of two nested lists containing all GamePiece objects for both players as an argument. It places all GamePiece objects on 
        their proper starting locations on the board in addition to assigning the proper algebraic notation locations to each GamePiece.
        """        
        for i in range(len(pieces_list)):           # [['r']['b']] 
            for piece in pieces_list[i]:            # for piece in inner lists
                pos = piece.get_pos()
                piece_type = type(piece)

                if isinstance(piece, piece_type):
                    self.set_piece(piece, pos)

    def get_board(self):
        """
        Return raw board representation. (For use by program).
        """
        return self._board

    def get_pieces_on_board(self):
        """
        Returns a list of all pieces present on the board. The list includes GamePiece name and position.
        """
        return self._pieces

    def get_space_contents(self, pos):
        """
        Returns the GamePiece object or '---' string (indicating empty position) present at the specified position.
        """
        col, row = pos
        return self._board[row][col]

    def get_checkmate(self):
        """
        Returns the state of checkmate. (True of False)
        """
        return self._checkmate

    def get_winner(self):
        """
        Returns the winner. (Is None until a winner is found. Then become either 'red' or 'blue' respectively).
        """
        return self._winner

    def move(self, piece_obj, pos):
        """
        Moves the given piece to the given position
        """
        if type(piece_obj) == str:
            return False
        col, row = pos
        self._board[row][col] = piece_obj
        piece_obj.move(pos)

    def set_piece(self, piece_obj, pos):
        """
        Place GamePiece object argument on board at given positions and update piece's position string.
        """
        col, row = pos
        self._board[row][col] = piece_obj

        if type(piece_obj) != str:
            piece_obj.set_pos(pos)
            piece_obj.calc_pg_pos()

    def remove_piece(self, piece_obj):
        """
        Removes the given GamePiece object from the 'Pieces list'.
        """
        team = piece_obj.get_team()

        if team == 'r':
            self._pieces[0].remove(piece_obj)
        else:
            self._pieces[1].remove(piece_obj)

    def get_general_obj_and_pos(self, player):
        """
        Returns a tuple containing the General GamePiece Object for the given player ('red' or 'blue') and the General 
        GamePiece's current position.
        """
        if player == 'red':
            team = 0
        else:
            team = 1

        board = self.get_board()

        for piece in self.get_pieces_on_board()[team]:
            if isinstance(piece, general.General):
                return piece, piece.get_pos()

    def is_in_check(self, player):
        """
        Returns True if the player passed as argument is in check. Returns False otherwise.
        """
        if player == 'red':
            opponent = 'blue'
        else:
            opponent = 'red'
            
        gen_obj, gen_pos = self.get_general_obj_and_pos(player)
        all_moves = self.get_moves_dict()

        if gen_pos in all_moves[opponent]:
            return True
        return False

    def get_moves_dict(self):
        """
        Creates and returns a dictionary composed of two nested dicitonaries containing all poissble moved for both teams. 
        Dictionary keys are board spaces (Ex: (3, 5)) and values are a list of all objects that can reach that space with a 
        valid move (Ex: [bEl, bSo, bCa]).
        """
        moves_dict = {}
        moves_dict['red'] = {}
        moves_dict['blue'] = {}

        for i in range(2):
            if i == 0:
                team = 'red'
            else:
                team = 'blue'
            for piece in self.get_pieces_on_board()[i]:
                for space in piece.get_valid_moves(self):
                    if space not in moves_dict[team]:
                        moves_dict[team][space] = [piece]
                    else:
                        moves_dict[team][space].extend([piece])
        
        return moves_dict

    def get_valid_moves_to_uncheck_self(self, player, opponent):
        """
        If in check, returns a dictionary of moves that are valid to uncheck (if any).
        """
        valid_moves_to_uncheck_self = {}
        
        player_gen_obj, player_gen_pos = self.get_general_obj_and_pos(player)
        # can the player move their General out of check?
        gen_moves = []
        all_moves = self.get_moves_dict()
        
        for space in player_gen_obj.get_valid_moves(self):
            if space not in all_moves[opponent]:
                gen_moves.append(space)
        
        # check if movement would put the General in check at other space locatioin 
        gen_moves = self.future_moves(player_gen_obj, player_gen_pos, player_gen_pos, gen_moves, opponent)
        if gen_moves != []:
            valid_moves_to_uncheck_self[player_gen_obj] = gen_moves

        # store pieces and moves that can catpure the opponent piece(s) putting thier general in check.
        pieces_checking_general = all_moves[opponent][player_gen_pos]
        pieces_to_caputure_or_block = len(pieces_checking_general)
        for piece in pieces_checking_general:
            if piece.get_pos() in all_moves[player]:
                for p in all_moves[player][piece.get_pos()]:
                    if isinstance(p, general.General):
                        continue
                    if p in valid_moves_to_uncheck_self:
                        continue
                    else:
                        valid_moves_to_uncheck_self[p] = [piece.get_pos()]

            # store pieces and moves that can block the opponent piece(s) putting thier general in check.
            piece_coords = piece.get_pos()
            player_gen_coords = player_gen_pos
        
            if isinstance(piece, horse.Horse):
                blocking_pieces = self.block_horse_check(piece_coords, player_gen_coords, piece, all_moves, player)
                if blocking_pieces is not None:
                    valid_moves_to_uncheck_self.update(blocking_pieces)

            if isinstance(piece, elephant.Elephant):
                blocking_pieces = self.block_elephant_check(piece_coords, player_gen_coords, piece, all_moves, player)
                if blocking_pieces is not None:
                    valid_moves_to_uncheck_self.update(blocking_pieces)

            if isinstance(piece, chariot.Chariot) or isinstance(piece, cannon.Cannon):
                blocking_pieces = self.block_chariot_or_cannon_check(piece_coords, player_gen_coords, piece, all_moves, player)
                if blocking_pieces is not None:
                    valid_moves_to_uncheck_self.update(blocking_pieces)

        if pieces_to_caputure_or_block > 1:
            valid_moves_to_uncheck_self = self.multi_piece_check_verification(player_gen_pos, valid_moves_to_uncheck_self, opponent)

        return valid_moves_to_uncheck_self

    def multi_piece_check_verification(self, player_gen_pos, valid_moves_to_uncheck_self, opponent):
        """
        Used when the current player is in check to calculate/verify valid moves that can remove the player from check. 
        Makes sure that the proposed move won't also expose the current player to check via another space or piece. 
        Updates and returns a dictionary containing all moves that pass this test.
        """
        valid_moves = {}
        board = self.get_board()
        
        for piece_obj in valid_moves_to_uncheck_self:
            if valid_moves_to_uncheck_self[piece_obj] == []:
                continue
            piece_pos = piece_obj.get_pos()
            for space in valid_moves_to_uncheck_self[piece_obj]:
                space_contents = board.get_space_contents(space)
                board.set_piece(piece_obj, space)
                board.set_piece('---', piece_pos)
                all_moves = self.get_moves_dict()
                if player_gen_pos not in all_moves[opponent]:
                        valid_moves[piece_obj] = space
                board.set_piece(piece_obj, piece_pos)
                board.set_piece(space_contents, space)
        return valid_moves

    def future_moves(self, piece_obj, piece_pos, player_gen_pos, moves, opponent):
        """
        Used when the current player is not yet in check, yet verifies that the proposed move will not expose the current player to check. 
        Returns a list of all valid moves that pass this test.
        """
        valid_moves = []

        for space in moves:
            space_contents = self.get_space_contents(space)
            self.set_piece(piece_obj, space)
            self.set_piece('---', piece_pos)
            all_moves = self.get_moves_dict()
            if isinstance(piece_obj, general.General):
                if space not in all_moves[opponent]:
                    valid_moves.append(space)
            else:
                if player_gen_pos not in all_moves[opponent]:
                    valid_moves.append(space)
            self.set_piece(piece_obj, piece_pos)
            self.set_piece(space_contents, space)
        return valid_moves

    def block_horse_check(self, piece_coords, player_gen_coords, piece_obj, all_moves, player):
        """
        If the current player is in check by an opponents Horse, returns a dictionary containing all of these spaces between that 
        Horse GamePice and the current player's General that will successfully block the check.
        """
        blocking_pieces = {}

        # find blockable spaces
        col_diff, row_diff = player_gen_coords[0] - piece_coords[0], player_gen_coords[1] - piece_coords[1]
        blockable_spaces = []

        if row_diff > 0:
            row_diff -= 1
        else:
            row_diff += 1 

        if col_diff > 0:
            col_diff -= 1
        else:
            col_diff += 1

        blockable_spaces.append((piece_coords[0] + col_diff, piece_coords[1] + row_diff))
            
        # see if player pieces can move there
        for space in blockable_spaces:
            if space in all_moves[player]:
                for blocking_piece in all_moves[player][space]:
                    if not isinstance(blocking_piece, general.General):
                        blocking_pieces[blocking_piece] = [space]
            
        if blocking_pieces != {}:
            return blocking_pieces
        return None

    def block_elephant_check(self, piece_coords, player_gen_coords, piece_obj, all_moves, player):
        """
        If the current player is in check by an opponents Elephant, returns a dictionary containing all of these spaces 
        between that Elephant GamePice and the current player's General that will successfully block the check.
        """
        blocking_pieces = {}

        # find blockable spaces
        col_diff, row_diff = player_gen_coords[0] - piece_coords[0], player_gen_coords[1] - piece_coords[1]
        blockable_spaces = []

        for i in range(1, 3):
            if col_diff > 0:
                col_diff -= 1
            else:
                col_diff += 1 

            if row_diff > 0:
                row_diff -= 1
            else:
                row_diff += 1

            blockable_spaces.append((piece_coords[0] + col_diff, piece_coords[1] + row_diff))

        # see if player pieces can move there
        for space in blockable_spaces:
            if space in all_moves[player]:
                for blocking_piece in all_moves[player][space]:
                    if not isinstance(blocking_piece, general.General):
                        blocking_pieces[blocking_piece] = [space]
            
        if blocking_pieces != {}:
            return blocking_pieces
        return None

    def block_chariot_or_cannon_check(self, piece_coords, player_gen_coords, piece_obj, all_moves, player):
        """
        If the current player is in check by an opponents Chariot or Cannon, returns a dictionary containing all of these spaces 
        between that Chariot or Cannon GamePice and the current player's General that will successfully block the check.
        """
        blocking_pieces = {}

        for i in range(2):
            if i == 0:
                x, y = 0, 1
            else:
                x, y = 1, 0

            # If i == 0, same column. If i == 1, same row
            if piece_coords[x] == player_gen_coords[x]:
                lower = min(piece_coords[y], player_gen_coords[y])
                upper = max(piece_coords[y], player_gen_coords[y])
                var = piece_coords[x]
                diff_range = range(lower + 1, upper)
                for j in diff_range:
                    if i == 0:
                        var_pos = (var, j)
                    else:
                        var_pos = (j, var)
                    space_between = var_pos
                    if space_between in all_moves[player]:
                        for blocking_piece in all_moves[player][space_between]:
                            if not isinstance(blocking_piece, general.General):
                                blocking_pieces[blocking_piece] = [space_between]


        if blocking_pieces != {}:
            return blocking_pieces
        return None

    def make_move(self, move_from, move_to):
        """
        Moves a player piece from 'move_from' to 'move_to'. If move is invalid (square being moved from doesn't contain a piece belonging to the player 
        whose turn it is, or if the indicated move is not legal, or if the game has already been won) it returns False. Otherwise it makes the given move, 
        removes captured pieces (if any), updates '_turn', and returns True.
        """
        # check that space being moved from is not empty and of the correct team
        game_piece = self.get_space_contents(move_from)

        # obtain current piece's team ('r' or 'b') and assign it to the full word ('red' ot 'blue')
        if game_piece.get_team() == 'r':
            player = 'red'
            opponent = 'blue'
        else:
            player = 'blue'
            opponent = 'red'

        # if player is in check (pre-move)
        if self.is_in_check(player):

            # all valid moves from all sceanrios will be stored here with piece objects as keys and all valid moves that piece can make as its values. 
            valid_moves_to_uncheck_self = self.get_valid_moves_to_uncheck_self(player, opponent)

            # if piece being moved and space being moved to are present in 'valid_moves_to_uncheck_self' dictionary, 
            # move is valid. Update board and turn. Otherwise, return False.
            piece_set = False
            for piece in valid_moves_to_uncheck_self:
                if piece == game_piece:
                    if valid_moves_to_uncheck_self[piece] == []:
                        continue
                    if move_to in valid_moves_to_uncheck_self[piece]:
                        
                        move_to_contents = self.get_space_contents(move_to)
                        if move_to_contents != '---':
                            if move_to_contents.get_team() == game_piece.get_team():
                                return False
                            else:
                                self.remove_piece(move_to_contents)
                                self.set_piece(game_piece, move_to)
                                self.set_piece('---', move_from)
                                piece_set = True
                        else:
                            self.set_piece(game_piece, move_to)
                            self.set_piece('---', move_from)
                            piece_set = True
                            break
            if piece_set:

                # check for post move checkmate
                if self.is_in_check(opponent):

                    # all valid moves from all sceanrios will be stored here with piece objects as keys and all valid moves that piece can make as its values. 
                    valid_moves_to_uncheck_self = self.get_valid_moves_to_uncheck_self(opponent, player)

                    # if no valid moves, checkmate
                    if valid_moves_to_uncheck_self == {}:
                        self._checkmate = True
                        self._winner = player
                        return True
                return True
            return False

        # not in check
        else:

            # unpack current player general object and position
            player_gen_obj, player_gen_pos = self.get_general_obj_and_pos(player)

            # check that proposed move mon't expose general to check
            valid_moves = game_piece.get_valid_moves(self)
            valid_moves = self.future_moves(game_piece, move_from, player_gen_pos, valid_moves, opponent)

            # return False if move not valid
            if move_to not in valid_moves:
                return False

            #update board and turn
            move_to_contents = self.get_space_contents(move_to)
            if move_to_contents != '---':
                if move_to_contents.get_team() == game_piece.get_team():
                    return False
                else:
                    self.remove_piece(move_to_contents)
                    self.set_piece(game_piece, move_to)
                    self.set_piece('---', move_from)
            else:
                self.set_piece(game_piece, move_to)
                self.set_piece('---', move_from)

            # check for post move checkmate
            if self.is_in_check(opponent):

                # all valid moves from all sceanrios will be stored here with piece objects as keys and all valid moves that piece can make as its values. 
                valid_moves_to_uncheck_self = self.get_valid_moves_to_uncheck_self(opponent, player)

                # if no valid moves, checkmate
                if valid_moves_to_uncheck_self == {}:
                    self._checkmate = True
                    self._winner = player
                    return True
        return True

    def print_board(self):
        """
        Print formatted board for debugging purposes. (For use by humans).
        """
        print()
        print("                                  RED                            ")
        print("       a      b      c      d      e      f      g      h      i ")
        print("1  ", self._board[0], " 1")
        print("2  ", self._board[1], " 2")
        print("3  ", self._board[2], " 3")
        print("4  ", self._board[3], " 4")
        print("5  ", self._board[4], " 5")
        print("6  ", self._board[5], " 6")
        print("7  ", self._board[6], " 7")
        print("8  ", self._board[7], " 8")
        print("9  ", self._board[8], " 9")
        print("10 ", self._board[9], " 10")
        print("       a      b      c      d      e      f      g      h      i ")
        print("                                 BLUE                            ")
        print()

    def board_ranges(self):
        """
        Returns a tuple containing the valid ranges of the rows and columns on the game board.
        """
        cols = range(9)
        rows = range(10)
        
        return cols, rows

    def fortress_ranges(self):
        """
        Returns a 3-tuple containing the valid ranges of the rows (unique) and columns (shared) for both the red and blue fortress's.
        """
        cols = range(3, 6)
        red_rows = range(3)
        blue_rows = range(7, 10)
        
        return cols, red_rows, blue_rows


    # pygame movement purposes
    def get_valid_moves(self, game_piece):
        """
        Returns a list of valid moves for the given game piece (Used for rendering valid moves on screen)
        """
        valid_moves = []

        if game_piece.get_team() == 'r':
            player = 'red'
            opponent = 'blue'
        else:
            player = 'blue'
            opponent = 'red'

        if self.is_in_check(player):
            valid_moves_to_uncheck_self = self.get_valid_moves_to_uncheck_self(player, opponent)
            if game_piece in valid_moves_to_uncheck_self:
                valid_moves.extend(valid_moves_to_uncheck_self[game_piece])

        else:
            # unpack current player general object and position
            pos = game_piece.get_pos()
            player_gen_obj, player_gen_pos = self.get_general_obj_and_pos(player)

            # check that proposed move mon't expose general to check
            valid_moves = game_piece.get_valid_moves(self)
            valid_moves = self.future_moves(game_piece, pos, player_gen_pos, valid_moves, opponent)

        return valid_moves

    def draw(self, win):
        """
        Renders all board components to the screen.
        """
        self.draw_squares(win)
        self.draw_lines(win)
        self.draw_pieces(win)

    def draw_squares(self, win):
        """
        Renders each square on the game board.
        """
        win.fill(WOOD)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, WOOD, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def draw_lines(self, win):
        """
        Rendres the lines on the board that create the grid for game piece movement.
        """
        center_offset = SQUARE_SIZE // 2

        # draw rows
        for row in range(ROWS):
            start_pos = (center_offset, (row * SQUARE_SIZE) + center_offset)
            end_pos = (center_offset + (SQUARE_SIZE * (ROWS - 2)), (row * SQUARE_SIZE) + center_offset)
            pygame.draw.line(win, BLACK, start_pos, end_pos, 3)

        # draw cols
        for col in range(COLS):
            start_pos = ((col * SQUARE_SIZE) + center_offset, center_offset)
            end_pos = ((col * SQUARE_SIZE) + center_offset, center_offset + (SQUARE_SIZE * (COLS)))
            pygame.draw.line(win, BLACK, start_pos, end_pos, 3)

        # red side diagonals
        start_pos = ((SQUARE_SIZE * 3) + center_offset, SQUARE_SIZE * 0 + center_offset)
        end_pos = ((SQUARE_SIZE * 5) + center_offset, SQUARE_SIZE * 2 + center_offset)
        pygame.draw.line(win, BLACK, start_pos, end_pos, 3)

        start_pos = ((SQUARE_SIZE * 3) + center_offset, SQUARE_SIZE * 2 + center_offset)
        end_pos = ((SQUARE_SIZE * 5) + center_offset, SQUARE_SIZE * 0 + center_offset)
        pygame.draw.line(win, BLACK, start_pos, end_pos, 3)

        # blue side diagonals
        start_pos = ((SQUARE_SIZE * 3) + center_offset, SQUARE_SIZE * 7 + center_offset)
        end_pos = ((SQUARE_SIZE * 5) + center_offset, SQUARE_SIZE * 9 + center_offset)
        pygame.draw.line(win, BLACK, start_pos, end_pos, 3)

        start_pos = ((SQUARE_SIZE * 3) + center_offset, SQUARE_SIZE * 9 + center_offset)
        end_pos = ((SQUARE_SIZE * 5) + center_offset, SQUARE_SIZE * 7 + center_offset)
        pygame.draw.line(win, BLACK, start_pos, end_pos, 3)

    def draw_pieces(self, win):
        """
        Renders each game piece on the board.
        """
        for i in range(2):
            for piece in self.get_pieces_on_board()[i]:
                img_string = './janggi/resources/'
                if i == 0:
                    img_string += 'red_'
                else:
                    img_string += 'blue_'
                if isinstance(piece, general.General):
                    img_string += 'general.png'
                if isinstance(piece, guard.Guard):
                    img_string += 'guard.png'
                if isinstance(piece, horse.Horse):
                    img_string += 'horse.png'
                if isinstance(piece, elephant.Elephant):
                    img_string += 'elephant.png'
                if isinstance(piece, chariot.Chariot):
                    img_string += 'chariot.png'
                if isinstance(piece, cannon.Cannon):
                    img_string += 'cannon.png'
                if isinstance(piece, soldier.Soldier):
                    img_string += 'soldier.png'
                piece_img = pygame.image.load(img_string)
                win.blit(piece_img, piece.get_pg_pos())