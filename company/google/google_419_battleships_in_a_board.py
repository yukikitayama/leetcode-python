from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:

        m = len(board)
        n = len(board[0])
        ans = 0

        for i in range(m):
            for j in range(n):
                # first row, or previous row same column (adjacent top) has no ship
                # first column, or previous column same row (adjacent left) has no ship
                if board[i][j] == 'X' and (i == 0 or board[i - 1][j] == '.') and (j == 0 or board[i][j - 1] == '.'):
                    # Increment because we can place ship
                    ans += 1

        return ans


if __name__ == '__main__':
    board = [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]
    print(Solution().countBattleships(board))
