import copy

table = """
╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗
║   │ 4 │ 1 ║ 6 │   │   ║ 3 │   │ 5 ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║   │   │   ║   │   │ 7 ║   │   │ 2 ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║   │   │ 5 ║ 9 │   │   ║   │   │   ║
╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
║ 7 │   │   ║   │   │ 5 ║ 4 │ 8 │   ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║ 3 │   │ 9 ║   │   │ 8 ║   │ 2 │   ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║   │ 4 │   ║ 7 │ 6 │   ║   │   │ 9 ║
╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
║   │   │ 4 ║ 3 │   │   ║   │ 9 │ 1 ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║   │ 6 │ 7 ║ 5 │   │   ║   │   │ 4 ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║   │ 9 │   ║   │ 4 │ 1 ║ 2 │   │   ║
╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝
"""

start = {
    1: 0,  2: 4,  3: 1,  4: 0,  5: 0,  6: 0,  7: 0,  8: 0,  9: 5,
    10: 6, 11: 0, 12: 0, 13: 0, 14: 0, 15: 7, 16: 9, 17: 0, 18: 0,
    19: 3, 20: 0, 21: 5, 22: 0, 23: 0, 24: 2, 25: 0, 26: 0, 27: 0,
    28: 7, 29: 0, 30: 0, 31: 3, 32: 0, 33: 9, 34: 0, 35: 4, 36: 0,
    37: 0, 38: 0, 39: 5, 40: 0, 41: 0, 42: 8, 43: 7, 44: 6, 45: 0,
    46: 4, 47: 8, 48: 0, 49: 0, 50: 2, 51: 0, 52: 0, 53: 0, 54: 9,
    55: 0, 56: 0, 57: 4, 58: 0, 59: 6, 60: 7, 61: 0, 62: 9, 63: 0,
    64: 3, 65: 0, 66: 0, 67: 5, 68: 0, 69: 0, 70: 0, 71: 4, 72: 1,
    73: 0, 74: 9, 75: 1, 76: 0, 77: 0, 78: 4, 79: 2, 80: 0, 81: 0
}


class SudokuBaseClass:
    all_numbers = set({1, 2, 3, 4, 5, 6, 7, 8, 9})

    def __init__(self, index, table):
        self.table = table
        self.index = index
        self._elements = []
        self.build_elements()

    @property
    def values(self):
        return [el.value for el in self._elements]

    @property
    def missing_values(self):
        return list(self.all_numbers - set(self.values))

    def build_elements(self):
        for index in self.element_indexes:
            self._elements.append(
                GridPoint(index, self.table)
            )

    @property
    def element_indexes(self):
        raise NotImplemented()


class GridPoint:

    def __init__(self, index, table):
        self.table = table
        self._index = index
        self._possible_values = set()
        self.square_index = None
        self.row_index = None
        self.column_index = None
        self.find_intersections()

    def find_intersections(self):
        """
        Given the point on the grid, this function calculates the row, column
        and square the point belongs to
        """
        self.square_index = self._find_square()
        self.row_index = self._find_row()
        self.column_index = self._find_column()

    def _find_square(self):
        if 9 >= self._index >= 1:
            return 1
        if 18 >= self._index >= 10:
            return 2
        if 27 >= self._index >= 19:
            return 3
        if 36 >= self._index >= 28:
            return 4
        if 45 >= self._index >= 37:
            return 5
        if 54 >= self._index >= 46:
            return 6
        if 63 >= self._index >= 55:
            return 7
        if 72 >= self._index >= 64:
            return 8
        if 81 >= self._index >= 73:
            return 9

    def _find_row(self):
        if self._index in [1, 2, 3, 10, 11, 12, 19, 20, 21]:
            return 1
        if self._index in [4, 5, 6, 13, 14, 15, 22, 23, 24]:
            return 2
        if self._index in [7, 8, 9, 16, 17, 18, 25, 26, 27]:
            return 3
        if self._index in [28, 29, 30, 37, 38, 39, 46, 47, 48]:
            return 4
        if self._index in [31, 32, 33, 40, 41, 42, 49, 50, 51]:
            return 5
        if self._index in [34, 35, 36, 43, 44, 45, 52, 53, 54]:
            return 6
        if self._index in [55, 56, 57, 64, 65, 66, 73, 74, 75]:
            return 7
        if self._index in [58, 59, 60, 67, 68, 69, 76, 77, 78]:
            return 8
        if self._index in [61, 62, 63, 70, 71, 72, 79, 80, 81]:
            return 9

    def _find_column(self):
        if self._index in [1, 4, 7, 28, 31, 34, 55, 58, 61]:
            return 1
        if self._index in [2, 5, 8, 29, 32, 35, 56, 59, 62]:
            return 2
        if self._index in [3, 6, 9, 30, 33, 36, 57, 60, 63]:
            return 3
        if self._index in [10, 13, 16, 37, 40, 43, 64, 67, 70]:
            return 4
        if self._index in [11, 14, 17, 38, 41, 44, 65, 68, 71]:
            return 5
        if self._index in [12, 15, 18, 39, 42, 45, 66, 69, 72]:
            return 6
        if self._index in [19, 22, 25, 46, 49, 52, 73, 76, 79]:
            return 7
        if self._index in [20, 23, 26, 47, 50, 53, 74, 77, 80]:
            return 8
        if self._index in [21, 24, 27, 48, 51, 54, 75, 78, 81]:
            return 9

    @property
    def index(self):
        return self._index

    @property
    def value(self):
        return self.table[self.index] or None

    @property
    def possible_values(self):
        return self._possible_values

    @property
    def is_set(self):
        """
        Return True if a number is set for this cell, False otherwise.
        """
        return bool(self.table[self.index])

    def set_value(self, value):
        self.table[self.index] = value


class Line(SudokuBaseClass):
    """
    Represents a line on the grid, indexed from 1 to 9, up to bottom
    """
    starting_numbers = {1: 1, 2: 4, 3: 7, 4: 28, 5: 31, 6: 34, 7: 55, 8: 58, 9: 61}

    @property
    def starting_number(self):
        return self.starting_numbers[self.index]

    @property
    def element_indexes(self):
        result = []
        for i, n in enumerate(range(3)):
            if i == 0:
                result.append(self.starting_number)
            else:
                result.append(self.starting_number + i)
        for i in range(3):
            result.append(self.starting_number + 9 + i)
        for i in range(3):
            result.append(self.starting_number + 2*9 + i)

        return result


class Column(SudokuBaseClass):
    """
    Represents a column in the grid, indexed from 1 to 9, left to right
    """
    starting_numbers = {1: 1, 2: 2, 3: 3, 4: 10, 5: 11, 6: 12, 7: 19, 8: 20, 9: 21}

    @property
    def starting_number(self):
        return self.starting_numbers[self.index]

    @property
    def element_indexes(self):
        result = []
        for i in range(3):
            result.append(self.starting_number + 3 * i)
        for i in range(27, 34, 3):
            result.append(self.starting_number + i)
        for i in range(54, 61, 3):
            result.append(self.starting_number + i)

        return result


class Square(SudokuBaseClass):
    starting_numbers = {1: 1, 2: 10, 3: 19, 4: 28, 5: 37, 6: 46, 7: 55, 8: 64, 9: 73}

    @property
    def starting_number(self):
        return self.starting_numbers[self.index]

    @property
    def element_indexes(self):
        return [n for n in range(self.starting_number, self.starting_number + 9)]


def find_obvious_numbers(lines, columns):
    """
    First iteration, look for obvious choices when one number is the only possible choice given
    from crossing lines and columns
    """
    for _, line in lines.items():
        for i, v in enumerate(line.values):
            if v is None and len(set(line.missing_values) - set(columns[i+1].missing_values)) == 1:
                # we found there is only one number that can go here
                print("Found that :", set(line.missing_values) - set(columns[i+1].missing_values))
                print(f"Goes on line {_} in place {i+1}")
                # start[(_ * 9) - (9 - i) + 1] = list(
                #    line.missing_values - columns[i+1].missing_values)[0]


def find_and_fill_one_missing_value(objects):
    for _, obj in objects.items():
        if len(obj.missing_values) == 1:
            for point in obj._elements:
                if not point.is_set:
                    value = list(obj.missing_values)[0]
                    print(f'Setting value for point {point.index} to {value}')
                    point.set_value()


def find_all_possibilities_for_all_grid_points(lines, columns, squares):
    """
    Call this once before starting solving the puzzle, it will find for every free cell
    all possible number that can fit.
    """
    for _, line in line.items():
        for el in line._elements:
            find_all_possible_values_for_grid_point(el)


def find_all_possible_values_for_grid_point(grid_point, columns, squares, lines):
    if not grid_point.is_set:
        # find numbers that fit
        column = columns[grid_point.column_index]
        square = squares[grid_point.square_index]
        line = lines[grid_point.row_index]
        missing_on_row = set(line.missing_values)

        # Create a copy of the possible number set to remove eventually found numbers
        possible_values = copy.copy(missing_on_row)
        for value in missing_on_row:
            if value in column.values or value in square.values:
                # remove from the possible numbers
                possible_values.discard(value)
        grid_point._possible_values = possible_values


def main():
    lines = {n: Line(n, start) for n in range(1, 10)}
    columns = {n: Column(n, start) for n in range(1, 10)}
    squares = {n: Square(n, start) for n in range(1, 10)}
    find_and_fill_one_missing_value(lines)
    find_and_fill_one_missing_value(columns)


if __name__ == '__main__':
    main()
