import logging
import sys

import fixtures

def index_row(n): return range((9*n),9*(n+1))

def index_col(n): return range(n,n+81,9)

def index_squ(index):
    # gives the index of the first cell in the square
    firstcell = lambda n:27*(n/3) + 3*(n%3)
    # for a given first cell, gives a list of all nine cells
    cellblock = lambda m:range(m,m+3) + range(m+9,m+12) + range(m+18,m+21)
    return cellblock(firstcell(index))

def print_grid(grid):
    if len(grid) == 81:
        for r in range(0,81,9):
            print "grid:   {}".format(grid[r:r+9])

def get_blank_cells(alist):
    """
    Return the cell numbers of all blank cells. Makes no attempt to identify
    an optimum order to test the cells, only that the cell is not solved.
    """
    return [i for i, x in enumerate(alist) if x < 1 ]
    # return map(self.grid.index, filter(lambda n:n not in [1,2,3,4,5,6,7,8,9], self.grid)).pop()

            
    
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
            # self.index_squ = lambda n:
    
    def __eq__(self, other): 
        return self.grid == other.grid
        
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
        return self._get_subset(index, index_row(index))

    def get_col(self, index):
        return self._get_subset(index, index_col(index))

    def get_squ(self, index):
        # gives the index of the first cell in the square
        return self._get_subset(index, index_squ(index))

    def _subset_is_compliant(self, subset):
        return [1,2,3,4,5,6,7,8,9] == sorted(subset)

    def is_grid_compliant(self):
        for x in range(0, 27):
            if not self._subset_is_compliant(self.get_subset(x)):
                return False
        return True

    def is_complete(self):
        f = lambda my_bol,my_int : my_bol and (my_int in [1,2,3,4,5,6,7,8,9])
        return reduce(f, self.grid, True)

    def _list_of_new_grids(self, next_cell):
        new_grids = []
        for t in [1,2,3,4,5,6,7,8,9]:
            new_grid = self.grid
            new_grid[next_cell] = t
            print "Trying added value {} to cell number {}".format(t, next_cell)
            new_grids.append(SudokuGrid(new_grid).solve())
        return new_grids

    def _filter_solved_grids(self, solution):
        return solution[0] == SudokuGrid.solved
        #if 2 == len(solution):
        #else:
        #    return False
        #try:
        #    return solution[0] == SudokuGrid.solved
        #except IndexError:
        #    # print solution
        #    return False

    
    def solve(self):
        # print self.grid
        if self.is_grid_compliant():
            print "SOLVED!"
            return (SudokuGrid.solved, self)
        elif self.is_complete():
            #print "DEAD END"
            return (SudokuGrid.invalid, None)
        else:
            solutions = []
            for next_cell in self._get_blank_cells():
                # new_grids = []
                for t in [1,2,3,4,5,6,7,8,9]:
                    new_grid = list(self.grid)
                    new_grid[next_cell] = t
                    #print "Trying added value {} to cell number {}".format(t, next_cell)
                    new_grid_object =  SudokuGrid(new_grid)
                    result = new_grid_object.solve()
                    try:
                        if result[0] == SudokuGrid.solved:
                            solutions.append(result)
                    except IndexError:
                        print "result = {}".format(result)
                        print_grid(new_grid)
                        exit()

                # new_results = self._list_of_new_grids(next_cell)
                # new_results = map(solve, new_grids)
                # solutions.extend(filter(self._filter_solved_grids, new_results))
                # filtered_list = [i for i, x in enumerate(new_results) if x[0]==SudokuGrid.solved ]
                # print "filtered_list = {}".format(filtered_list)
                # solutions.extend(filtered_list)
                # print solutions
                
    
            if len(solutions) > 0:
                return solutions
            else:
                return SudokuGrid.invalid, None

            #elif len(solutions) > 1:
            #    return SudokuGrid.ambiguious, None
                            
        
 
if __name__ == '__main__':
    result = SudokuGrid(fixtures.grid_partial_working).solve()
    print result[0]
    #print result[0][1]
    #print result[1].grid
    print_grid(result[0][1].grid)
