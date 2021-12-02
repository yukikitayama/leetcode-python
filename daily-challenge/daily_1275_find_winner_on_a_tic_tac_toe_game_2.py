from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:

        n = 3

        rows, cols = [0] * n, [0] * n
        diag = anti_diag = 0

        player = 1

        for row, col in moves:
            rows[row] += player
            cols[col] += player

            if row == col:
                diag += player

            if row + col == n - 1:
                anti_diag += player

            if any(abs(counter) == n for counter in (rows[row], cols[col], diag, anti_diag)):
                return 'A' if player == 1 else 'B'

            player *= -1

        return 'Draw' if len(moves) == n * n else 'Pending'


"""
Time complexity
Let m be the length of moves.
O(m) because for loop to moves and for each move, we only constant if check 

Space complexity
O(2n) for row and col array, so O(n)
"""


moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
moves = [[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]
moves = [[0, 0], [1, 1]]
print(Solution().tictactoe(moves))
