class Solution:
    def __init__(self):
        self.n = None

    def totalNQueens(self, n):
        self.n = n
        return self.backtrack(0, set(), set(), set())

    def backtrack(self, row, cols, diagonals, anti_diagonals):
        # Success and stop recursive backtrack
        if row == self.n:
            return 1

        # backtrack always return 0 until we finish iteration by reaching the final row and return 1 by the above if
        solutions = 0

        # Try all the columns in the current row
        for col in range(self.n):

            curr_diagonal = row - col
            curr_anti_diagonal = row + col

            # Skip if we can't put queen
            if col in cols or curr_diagonal in diagonals or curr_anti_diagonal in anti_diagonals:
                continue

            # We can put queen, so record the information
            cols.add(col)
            diagonals.add(curr_diagonal)
            anti_diagonals.add(curr_anti_diagonal)

            # Go to the next row
            solutions += self.backtrack(row + 1, cols, diagonals, anti_diagonals)

            # Backtrack by removing previous approaches
            # Python Set remove method takes a single element as an argument and removes it from the set
            cols.remove(col)
            diagonals.remove(curr_diagonal)
            anti_diagonals.remove(curr_anti_diagonal)

        # When we break for loop,
        # we tried all the rows by recursive backtrack function
        # and all the columns by for loop
        # So we can return solutions
        return solutions
