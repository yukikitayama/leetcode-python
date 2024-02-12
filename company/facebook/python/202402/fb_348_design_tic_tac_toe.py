"""
Naive
  create matrix
  fill 1 or 2 in each cell
  At the end of move(), scan
    row,
    col
    diagonal,
    anti diagonal
    T: O(4N)

diagonal
  (0, 0), (1, 1), (2, 2)

anti diagonal
  if n = 3
  (0, 2), (1, 1), (2, 0)
  (0, n - 0 - 1), (1, n - 1- 1)
"""


class TicTacToe:

    def __init__(self, n: int):
        self.matrix = [[0] * n for _ in range(n)]
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        self.matrix[row][col] = player

        if (
                # Check curr row
                self.check_row(row, col, player)
                # Check curr col
                or self.check_col(row, col, player)
                # Check diagonal if curr at diagonal
                or self.check_diagonal(player)
                # Check anti-diagonal if curr at anti-diagonal
                or self.check_anti_diagonal(player)
        ):
            return player

        else:
            return 0

    def check_row(self, row, col, player):
        # Loop
        col = 0
        while col < len(self.matrix[0]):
            if self.matrix[row][col] != player:
                return False
            col += 1

        return True

    def check_col(self, row, col, player):
        # Loop
        row = 0
        while row < len(self.matrix):
            if self.matrix[row][col] != player:
                return False
            row += 1

        return True

    def check_diagonal(self, player):
        row = 0

        while row < len(self.matrix):
            if self.matrix[row][row] != player:
                return False
            row += 1

        return True

    def check_anti_diagonal(self, player):
        row = 0

        while row < self.n:
            if self.matrix[row][self.n - row - 1] != player:
                return False
            row += 1

        return True

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)