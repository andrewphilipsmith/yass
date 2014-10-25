import logging
import sys

class SudokuGrid():

    def __init__(self, grid_values):
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        # check that we have 
        if len(grid_values) != 81:
            # raise exception
            raise TypeError("incorrect number of values for SudokuGrid constructor. 81 expected, {} found".format(len(grid_values)))
        else:
            self.grid = grid_values 
            

    def _get_subset(self, index, slice):
        # if 0>index>10
        result = [ self.grid[i] for i in slice ]
        return result

    def get_row(self, index):
        return self._get_subset(index, range((9*index),9*(index+1)))

    def get_col(self, index):
        return self._get_subset(index, range(index,index+81,9))

    def get_squ(self, index):
        # gives the index of the first cell in the square
        firstcell = lambda n:27*(n/3) + 3*(n%3)
        # for a given first cell, gives a list of all nine cells
        cellblock = lambda m:range(m,m+3) + range(m+9,m+12) + range(m+18,m+21)
        return self._get_subset(index, cellblock(firstcell(index)))

