"""
init
  creats n by n matrix with 0
move
  assign 1 or 2 to matrix of row and col
  check vertical of col
  check horizontal of row
  check diagonal and anti-diagonal
"""


class TicTacToe:

    def __init__(self, n: int):
        self.board = [[0] * n for _ in range(n)]
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:

        self.board[row][col] = player

        def check_horizontal(row, player):
            for c in range(self.n):
                if self.board[row][c] != player:
                    return False
            return True

        def check_vertical(col, player):
            for r in range(self.n):
                if self.board[r][col] != player:
                    return False
            return True

        def check_diagonal(player):
            for i in range(self.n):
                if self.board[i][i] != player:
                    return False
            return True

        def check_anti_diagonal(player):
            for i in range(self.n):
                if self.board[i][self.n - i - 1] != player:
                    return False
            return True

        if check_horizontal(row, player):
            return player

        if check_vertical(col, player):
            return player

        if check_diagonal(player):
            return player

        if check_anti_diagonal(player):
            return player

        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)