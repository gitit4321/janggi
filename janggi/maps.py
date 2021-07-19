class Map:
    def __init__(self):
        self._alg_to_coord = self.init_alg_to_coord_map()
        self._coord_to_alg = self.init_coord_to_alg_map()
    
    def init_alg_to_coord_map(self):
        """
        Creates a dictionary, mapping the numbers and letters used for algebraic notation piece locations to the corresponding rows and columns used as 
        coordinates on the game board.
        """
        alg_to_coord_map = {}
        alg_to_coord_map['rows'] = {}
        alg_to_coord_map['cols'] = {}
        letters = 'abcdefghi'
        
        for i in range(9):
            alg_to_coord_map['cols'][letters[i]] = i

        for i in range(1, 11):
            alg_to_coord_map['rows'][str(i)] = i - 1

        return alg_to_coord_map
    
    def init_coord_to_alg_map(self):
        """
        Creates a dictionary, mapping the rows and columns used as coordinates on the game board to their respective algebraic notation representations.
        """
        coord_to_pos_map = {}
        coord_to_pos_map['cols'] = {}
        coord_to_pos_map['rows'] = {}
        letters = 'abcdefghi'
        
        for i in range(9):
            coord_to_pos_map['cols'][i] = letters[i]

        for i in range(1, 11):
            coord_to_pos_map['rows'][i - 1] = str(i)

        return coord_to_pos_map

    def get_alg_to_coord_map(self):
        """
        Returns a dictionary mapping algebraic noation representations of spaces on the game board to their nested list coordinate representaions."""
        return self._alg_to_coord

    def get_coord_to_alg_map(self):
        """
        Returns a dictionary mapping nested list coordinate representations of spaces on the game board to their algebraic notaion representations. 
        """
        return self._coord_to_alg

    def map_to_alg(self, coord_tup):
        """
        Returns a string in the form of the algebraic notation representation of the coordinates for a given space on the board. (column, row). (Ex: (3, 5) returns 'd6'.
        """
        alg_map = self.get_coord_to_alg_map()
        c, r = coord_tup

        col = alg_map['cols'][c]
        row = alg_map['rows'][r]
        

        return str(col + row)
    
    def map_to_coord(self, alg):
        """
        Returns a tuple containing the row and column of a given algebraic notation string. (Ex: 'd6' return (3, 5).
        """
        coord_map = self.get_alg_to_coord_map()

        if len(alg) == 3:
            col = coord_map['cols'][alg[0]]
            row = coord_map['rows'][alg[1:]]
        else:
            col = coord_map['cols'][alg[0]]
            row = coord_map['rows'][alg[1]]
            
        return col, row
