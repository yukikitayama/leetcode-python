from typing import List
import collections


class Excel:
    def __init__(self, height: int, width: str):
        self.height = height
        # Convert (A to Z) to (1 to 26)
        self.width = self._map(width) + 1
        # The values in form could be integer or hashmap
        # The hashmap is key (row, col) and value the count
        self.form = [[0] * self.width for _ in range(self.height)]

        # print('In constructor')
        # [print(row) for row in self.form]
        # print()

    def _map(self, char):
        # ord('A'): 65, ord('a'): 97
        return ord(char) - 65

    def set(self, row: int, column: str, val: int) -> None:
        # row - 1 because row is 1-based index
        self.form[row - 1][self._map(column)] = val

        # print('In set')
        # [print(row) for row in self.form]
        # print()

    def get(self, row: int, column: str) -> int:

        # print(f'In get, get(row:{row}, colunm: {column})')

        # Convert row and column to 0-based index
        r = row - 1
        c = self._map(column)

        # If the value at the current cell is just an integer,
        # we don't need to recursively calculate
        if type(self.form[r][c]) is int:
            return self.form[r][c]

        # Recursively run get() until it reaches the real integers
        else:
            # i is 0-based index but get() expects 1-based index row
            # j is also 0-based index, but get() expects A to Z character column
            # chr(65): 'A'
            # If form[r][c] is not integer, form[r][c] is a hashmap with key (row, col) and value the count
            # so for i, j in self.form[r][c] gives us i: row index, j: column index
            # so self.form[r][c][(i, j)] gives us a value of the hashmap accessed by key (i, j)
            # The value is the count which is about how many times pointing at the cell
            return sum(self.get(i + 1, chr(j + 65)) * self.form[r][c][(i, j)] for i, j in self.form[r][c])

    def sum(self, row: int, column: str, numbers: List[str]) -> int:

        # print(f'In sum, sum(row: {row}, column: {column}, numbers: {numbers})')

        # Count how many times a particular cell is called
        cells = collections.defaultdict(int)
        for string in numbers:

            # print(f'  string: {string}')

            if ':' not in string:
                i, j = self._parse(string)
                # ?
                cells[(i, j)] += 1

            else:
                start, end = string.split(':')
                i0, j0 = self._parse(start)
                i1, j1 = self._parse(end)
                for i in range(i0, i1 + 1):
                    for j in range(j0, j1 + 1):
                        cells[(i, j)] += 1

        # print(f'cells: {cells}')

        self.form[row - 1][self._map(column)] = cells

        # [print(row) for row in self.form]

        # The above set hashmap at row and column,
        # and the below actually gives us the sum from the hashmap
        return self.get(row, column)

    # Convert the alphabet plus integer like 'A1' to a tuple of row and column index
    def _parse(self, string: str):
        # ''.join() because digit could be up to 26, so '2' and '6' need to be connected and convert it to integere
        i = int(''.join(char for char in string if char.isdigit())) - 1
        # [bla bla][0] because it gives us the list of string with length 1
        # e.g. 'A10' -> ['A'] by list comprehension -> 'A' by [0] -> 0 by _map()
        j = self._map([char for char in string if char.isalpha()][0])
        return i, j



height = 3
width = 'C'
obj = Excel(height, width)
obj.set(1, 'A', 2)
print(obj.sum(3, 'C', ['A1', 'A1:B2']))
obj.set(2, 'B', 2)
print(obj.get(3, 'C'))


