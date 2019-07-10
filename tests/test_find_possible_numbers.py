from collections import defaultdict
from unittest import TestCase

from solve import Column, GridPoint, Line, Square, find_all_possible_values_for_grid_point


class FindPossibleNumbersForGridPointTestCase(TestCase):

    def test_case_only_one_cell_free(self):
        """
        Ensure that when the cell is the only empty for a square, the right number is set
        as possible value

         X 6 2 | 8 5 1 | 3 7 4
         8 5 1 |
         7 4 3 |
         ______ 
         2
         5
         6
         ______
         4
         3
         1
        """
        table = defaultdict(lambda: 0,
                            {1: 0,
                             2: 6,
                             3: 2,
                             4: 8,
                             5: 5,
                             6: 1,
                             7: 7,
                             8: 4,
                             9: 3,
                             10: 8,
                             11: 5,
                             12: 1,
                             19: 3,
                             20: 7,
                             21: 4,
                             28: 2,
                             31: 5,
                             34: 6,
                             55: 4,
                             58: 3,
                             61: 1})
        g = GridPoint(1, table)
        lines = {n: Line(n, table) for n in range(1, 10)}
        columns = {n: Column(n, table) for n in range(1, 10)}
        squares = {n: Square(n, table) for n in range(1, 10)}
        find_all_possible_values_for_grid_point(g, columns, squares, lines)
        self.assertEqual(g._possible_values, set({9}))
