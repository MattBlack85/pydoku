from unittest import TestCase

from solve import GridPoint

class GridPointTestCase(TestCase):

    def test_correct_initialisation(self):
        g = GridPoint(1, {})

        self.assertEqual(g.table, {})
        self.assertEqual(g._index, 1)
        self.assertEqual(g._possible_values, set())

    def test_interesctions_find_correct_first_grid_point(self):
        """
        Given an index 1 which equals to the first cell on the board,
        we expect to have the following interesections:
         - line 1
         - column 1
         - square 1
        """
        g = GridPoint(1, {})

        self.assertEqual(g.row_index, 1)
        self.assertEqual(g.square_index, 1)
        self.assertEqual(g.column_index, 1)

    def test_interesctions_find_correct_last_grid_point(self):
        """
        Given an index 81 which equals to the last cell on the board,
        we expect to have the following interesections:
         - line 9
         - column 9
         - square 9
        """
        g = GridPoint(81, {})

        self.assertEqual(g.row_index, 9)
        self.assertEqual(g.square_index, 9)
        self.assertEqual(g.column_index, 9)

    def test_interesctions_find_correct_middle_grid_point(self):
        """
        Given an index 41 which equals to the center cell on the board,
        we expect to have the following interesections:
         - line 5
         - column 5
         - square 5
        """
        g = GridPoint(41, {})

        self.assertEqual(g.row_index, 5)
        self.assertEqual(g.square_index, 5)
        self.assertEqual(g.column_index, 5)

    def test_interesctions_find_correct_edge_right_grid_point(self):
        """
        Given an index 48 which equals to the right edge cell on the board,
        we expect to have the following interesections:
         - line 4
         - column 9
         - square 6
        """
        g = GridPoint(48, {})

        self.assertEqual(g.row_index, 4)
        self.assertEqual(g.square_index, 6)
        self.assertEqual(g.column_index, 9)

    def test_grid_point_values(self):
        """
        Ensure the is_set API works properly
        """
        table = {1: 0}
        g = GridPoint(1, table)

        self.assertFalse(g.is_set)
        self.assertIsNone(g.value)
        g.set_value(5)
        self.assertTrue(g.is_set)
        self.assertEqual(g.value, 5)
        self.assertEqual(table[1], 5)
    
        
