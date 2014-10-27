import logging
import sys

class SudokuGrid():

    solved = 1
    invalid = 2
    ambiguious = 3

    def __init__(self, grid_values):
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        # check that we have 
        if len(grid_values) != 81:
            # raise exception
            raise TypeError("incorrect number of values for SudokuGrid constructor. 81 expected, {} found".format(len(grid_values)))
        else:
            self.grid = grid_values 
            self.index_row = lambda n:range((9*n),9*(n+1))
            self.index_col = lambda n:range(n,n+81,9)
            # self.index_squ = lambda n:
            
    def index_squ(self, index):
        # gives the index of the first cell in the square
        firstcell = lambda n:27*(n/3) + 3*(n%3)
        # for a given first cell, gives a list of all nine cells
        cellblock = lambda m:range(m,m+3) + range(m+9,m+12) + range(m+18,m+21)
        return cellblock(firstcell(index))
            
    def _get_subset(self, index, slice):
        # if 0>index>10
        result = [ self.grid[i] for i in slice ]
        return result

    def get_subset(self, index):
        if index >= 0:
            if index < 9:
                return self.get_row(index)
            elif index < 18:
                return self.get_col(index-9)
            elif index < 27:
                return self.get_squ(index-18)
        
    def get_row(self, index):
        return self._get_subset(index, self.index_row(index))

    def get_col(self, index):
        return self._get_subset(index, self.index_col(index))

    def get_squ(self, index):
        # gives the index of the first cell in the square
        return self._get_subset(index, self.index_squ(index))

    def _subset_is_compliant(self, subset):
        return range(1,10) == sorted(subset)

    def is_grid_compliant(self):
        for x in range(1, 27):
            if not self._subset_is_compliant(self.get_subset(x)):
                return False
        return True

    def is_complete(self):
        f = lambda my_bol,my_int : my_bol and (0<my_int and my_int<10)
        return reduce(f, self.grid, True)
        
    def solve(self):
        pass