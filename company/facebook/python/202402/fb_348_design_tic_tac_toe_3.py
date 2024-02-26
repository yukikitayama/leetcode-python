class TicTacToe:

    def __init__(self, n: int):
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.anti_diagonal = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        counter = 1 if player == 1 else -1

        # Update
        self.rows[row] += counter
        self.cols[col] += counter
        if row == col:
            self.diagonal += counter
        if row == self.n - col - 1:
            self.anti_diagonal += counter

        # Check winning condition
        if (
            abs(self.rows[row]) == self.n
            or abs(self.cols[col]) == self.n
            or abs(self.diagonal) == self.n
            or abs(self.anti_diagonal) == self.n
        ):
            return player
        else:
            return 0

class TicTacToe1:

    def __init__(self, n: int):
        self.board = [[0] * n for _ in range(n)]
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:

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
                if self.board[i][-(i + 1)] != player:
                    return False
            return True

        # Move
        self.board[row][col] = player

        # Check winning condition and return result
        if (
            check_horizontal(row, player)
            or check_vertical(col, player)
            or (row == col and check_diagonal(player))
            or (row == self.n - col - 1 and check_anti_diagonal(player))
        ):
            return player
        else:
            return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)