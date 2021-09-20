from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:

        n = 3
        board = [[0] * n for _ in range(n)]

        def checkRow(row, player_id):
            for col in range(n):
                # board cells are initialized with 0
                if board[row][col] != player_id:
                    return False
            return True

        def checkCol(col, player_id):
            for row in range(n):
                if board[row][col] != player_id:
                    return False
            return True

        def checkDiagonal(player_id):
            for i in range(n):
                if board[i][i] != player_id:
                    return False
            return True

        def checkAntiDiagonal(player_id):
            for i in range(n):
                if board[i][n - 1 - i] != player_id:
                    return False
            return True

        # Start game
        # Start with A by representing 1, and B is -1
        player = 1

        for move in moves:
            row, col = move
            board[row][col] = player

            if checkRow(row, player) \
                    or checkCol(col, player) \
                    or (row == col and checkDiagonal(player) \
                    or (row + col == n - 1 and checkAntiDiagonal(player))):
                return 'A' if player == 1 else 'B'

            player *= -1

        return 'Draw' if len(moves) == n * n else 'Pending'


"""
Time complexity
Let m be the length of moves. For each move, we need to go through 4 for-loops. Each for-loops takes n
So O(m * 4n) = O(mn)

Space complexity
O(n*n) for board
"""


moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
moves = [[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]
moves = [[0, 0], [1, 1]]
print(Solution().tictactoe(moves))
