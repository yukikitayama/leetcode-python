"""
- Problem says numbers in board is positive, so make it negative to flag to be crushed
- To be stable state, repeat the above steps by recursion
  - Use another flag to indicate whether need recursion, todo
"""


from typing import List


class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        R, C = len(board), len(board[0])

        # Flag for recursion
        todo = False

        # Check horizontal
        for r in range(R):
            # -2 because at least 3 contiguous requirement
            for c in range(C - 2):

                if abs(board[r][c]) == abs(board[r][c + 1]) == abs(board[r][c + 2]) != 0:

                    # Flag to be crushed
                    board[r][c] = board[r][c + 1] = board[r][c + 2] = -abs(board[r][c])
                    todo = True

        # Check vertical
        for r in range(R - 2):
            for c in range(C):
                if abs(board[r][c]) == abs(board[r + 1][c]) == abs(board[r + 2][c]) != 0:

                    board[r][c] = board[r + 1][c] = board[r + 2][c] = -abs(board[r][c])
                    todo = True

        print(f'After flagging')
        [print(row) for row in board]
        print()

        for c in range(C):
            wr = R - 1

            print(f'c: {c}')

            # Copy the above things to down for gravity
            for r in range(R - 1, -1, -1):

                # wr is bigger than or equal to r
                # so when it find positive, the positive value overwrites the
                # negative value is the bottom or lower rows
                # But overwriting numbers stay above, which need to be 0 in the below for loop
                if board[r][c] > 0:
                    board[wr][c] = board[r][c]
                    # At the end of this for loop, wr decremented by number of negatives and
                    # remaining positive in the column
                    wr -= 1

            print(f'After wr -= 1 with wr: {wr}')
            [print(row) for row in board]
            print()

            # Fill the fallen down things to 0 to flag they don't exist there any more
            for wr in range(wr, -1, -1):
                board[wr][c] = 0

            print('After = 0')
            [print(row) for row in board]
            print()

        return self.candyCrush(board) if todo else board


if __name__ == '__main__':
    board = [[110, 5, 112, 113, 114], [210, 211, 5, 213, 214], [310, 311, 3, 313, 314], [410, 411, 412, 5, 414],
             [5, 1, 512, 3, 3], [610, 4, 1, 613, 614], [710, 1, 2, 713, 714], [810, 1, 2, 1, 1], [1, 1, 2, 2, 2],
             [4, 1, 4, 4, 1014]]
    print(Solution().candyCrush(board))
