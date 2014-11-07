
import unittest
import fixtures
import sudoku_grid



class TestSudokuGrid(unittest.TestCase):

    def setUp(self):
        self.working_grid = sudoku_grid.SudokuGrid(fixtures.grid_working)
        self.failing_grid = sudoku_grid.SudokuGrid(fixtures.grid_fail)
        self.partial_grid = sudoku_grid.SudokuGrid(fixtures.grid_partial_working)
        self.real_grid = sudoku_grid.SudokuGrid(fixtures.grid_real)
        self.ambiguious_grid = sudoku_grid.SudokuGrid(fixtures.grid_ambiguious)
        
    def test_class_grid_constructor(self):
        pass

    def test_class_grid_constructor_wrong_parameters(self):
        self.assertRaises(TypeError, sudoku_grid.SudokuGrid, fixtures.grid_wrong_number_of_params)

    def test_grid_get_column(self):
        self.assertEqual(self.working_grid.get_col(0), fixtures.grid_working_col0, msg="column 0 failed")
        self.assertEqual(self.working_grid.get_col(1), fixtures.grid_working_col1, msg="column 1 failed")
        self.assertEqual(self.working_grid.get_col(2), fixtures.grid_working_col2, msg="column 2 failed")
        self.assertEqual(self.working_grid.get_col(3), fixtures.grid_working_col3, msg="column 3 failed")
        self.assertEqual(self.working_grid.get_col(4), fixtures.grid_working_col4, msg="column 4 failed")
        self.assertEqual(self.working_grid.get_col(5), fixtures.grid_working_col5, msg="column 5 failed")
        self.assertEqual(self.working_grid.get_col(6), fixtures.grid_working_col6, msg="column 6 failed")
        self.assertEqual(self.working_grid.get_col(7), fixtures.grid_working_col7, msg="column 7 failed")
        self.assertEqual(self.working_grid.get_col(8), fixtures.grid_working_col8, msg="column 8 failed")

    def test_grid_get_row(self):
        self.assertEqual(self.working_grid.get_row(0), fixtures.grid_working_row0, msg="row 0 failed")
        self.assertEqual(self.working_grid.get_row(1), fixtures.grid_working_row1, msg="row 1 failed")
        self.assertEqual(self.working_grid.get_row(2), fixtures.grid_working_row2, msg="row 2 failed")
        self.assertEqual(self.working_grid.get_row(3), fixtures.grid_working_row3, msg="row 3 failed")
        self.assertEqual(self.working_grid.get_row(4), fixtures.grid_working_row4, msg="row 4 failed")
        self.assertEqual(self.working_grid.get_row(5), fixtures.grid_working_row5, msg="row 5 failed")
        self.assertEqual(self.working_grid.get_row(6), fixtures.grid_working_row6, msg="row 6 failed")
        self.assertEqual(self.working_grid.get_row(7), fixtures.grid_working_row7, msg="row 7 failed")
        self.assertEqual(self.working_grid.get_row(8), fixtures.grid_working_row8, msg="row 8 failed")

    def test_grid_get_square(self):
        self.assertEqual(self.working_grid.get_squ(0), fixtures.grid_working_squ0, msg="square 0 failed")
        self.assertEqual(self.working_grid.get_squ(1), fixtures.grid_working_squ1, msg="square 1 failed")
        self.assertEqual(self.working_grid.get_squ(2), fixtures.grid_working_squ2, msg="square 2 failed")
        self.assertEqual(self.working_grid.get_squ(3), fixtures.grid_working_squ3, msg="square 3 failed")
        self.assertEqual(self.working_grid.get_squ(4), fixtures.grid_working_squ4, msg="square 4 failed")
        self.assertEqual(self.working_grid.get_squ(5), fixtures.grid_working_squ5, msg="square 5 failed")
        self.assertEqual(self.working_grid.get_squ(6), fixtures.grid_working_squ6, msg="square 6 failed")
        self.assertEqual(self.working_grid.get_squ(7), fixtures.grid_working_squ7, msg="square 7 failed")
        self.assertEqual(self.working_grid.get_squ(8), fixtures.grid_working_squ8, msg="square 8 failed")

    def test_subsets_from_cell_num(self):
        for cell in range(0,81):
            self.assertEqual(sudoku_grid.subsets_from_cell_num(cell), fixtures.grid_subsets_from_cell_number[cell], msg="cell {} failed".format(cell))
        
    def test_subset_is_compliant(self):
        for x in range(0, 27):
            self.assertTrue(self.working_grid._subset_is_compliant(self.working_grid.get_subset(x)))
            self.assertTrue(self.partial_grid._subset_is_compliant(self.partial_grid.get_subset(x)))
            self.assertFalse(self.failing_grid._subset_is_compliant(self.failing_grid.get_subset(x)))

    def test_subset_is_solved(self):
        for x in range(0, 27):
            self.assertTrue(self.working_grid._subset_is_solved(self.working_grid.get_subset(x)))
            self.assertFalse(self.failing_grid._subset_is_solved(self.failing_grid.get_subset(x)))

    def test_grid_is_solved(self):
        self.assertTrue(self.working_grid.is_grid_solved())
        self.assertFalse(self.failing_grid.is_grid_solved())

    def test_grid_is_complete(self):
        self.assertTrue(self.working_grid.is_complete())
        self.assertTrue(self.failing_grid.is_complete())
        self.assertFalse(self.partial_grid.is_complete())
    
    def test_grid_is_compliant(self):
        self.assertTrue(self.working_grid.is_compliant())
        self.assertTrue(self.partial_grid.is_compliant())
        self.assertFalse(self.failing_grid.is_compliant())
        
    def test_solve_grid(self):
        solved_working = self.working_grid.solve()
        self.assertEquals(solved_working[0],sudoku_grid.SudokuGrid.solved)
        self.assertEquals(solved_working[1],self.working_grid)
        # print "number of iterations = ".format(solved_working[2])
        
        solved_failing = self.failing_grid.solve()
        self.assertEquals(solved_failing[0],sudoku_grid.SudokuGrid.invalid)
        self.assertEquals(solved_failing[1],None)
        # print "number of iterations = ".format(solved_working[2])
        
#        self.assertEquals(self.partial_grid.solve(),(sudoku_grid.SudokuGrid.solved, self.working_grid))
#       self.assertEquals(self.ambiguious_grid.solve(),(sudoku_grid.SudokuGrid.ambiguious, None))

    def test_unused_val_from_cell(self):
        for x in range(0, 81):
            print "x={}  cells={} fixture={} ".format(x, self.real_grid.unused_val_from_cell(x), fixtures.grid_real_unused_val_from_cell[x])
            self.assertEquals(self.real_grid.unused_val_from_cell(x), 
            fixtures.grid_real_unused_val_from_cell[x])
        #self.assertEquals(False)
        
    def test_get_blank_cells(self):
        self.assertEquals(sorted(sudoku_grid.get_blank_cells(self.partial_grid.grid)), sorted(fixtures.grid_partial_blank_cell_indicies))
        self.assertEquals(sorted(sudoku_grid.get_blank_cells(self.partial_grid.get_subset(0))), [8])

        self.assertEquals(sorted(sudoku_grid.get_blank_cells(self.real_grid.grid)), sorted(fixtures.grid_real_blank_cell_indicies))

        
if __name__ == '__main__':
    # maosmtoshape = reload(maosmtoshape)
    unittest.main()