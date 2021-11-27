"""
- Start: 11:10
- End: 11:19
- Solved:
- Saw solution: 1

Example 1
Input: n = 3, k = 2, row = 0, column = 0
Output: 0.06250

    0   1   2
0   *(2,2)  (2)

1           (1)

2   (2) (1)

- 1st move, 2/8
- 2nd move, 0.5 * 2/8 + 0.5 * 2/8
- 2/8 * (1/2 * 2/8 + 1/2 * 2/8) = 0.0625
  - On the 1st move, 2 possibilities to stay on the board, and
    on the 2nd move, 2 possibilities from one of the first moves and
    2 possibilities from the other of the first moves, so multiply 1/2 to each 2/8

Idea
- Use dynamic programming

"""


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # dp will be previous state of probabilities in each cell
        dp = [[0] * n for _ in range(n)]
        # At the initial setting, knight is 100% at the starting cell
        dp[row][column] = 1

        print('dp')
        [print(row) for row in dp]
        print()

        offsets = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

        for _ in range(k):

            # dp2 is the current state of probabilities in each cell
            dp2 = [[0] * n for _ in range(n)]

            for r, row in enumerate(dp):
                # Val is probability at a cell
                for c, val in enumerate(row):
                    for offset_row, offset_col in offsets:
                        # If the next cell is on chessboard
                        if 0 <= r + offset_row < n and 0 <= c + offset_col < n:
                            # val is probability at (r, c) and from this probability,
                            # calculate probability at the next cell (r + offset_row, c + offset_col)
                            # val / 8 because it iterates each 8 direction
                            # += val / 8 because at first step, 1/8, second step 1/8 * 1/8 = (1/8) / 8
                            # and it could reach (r + offset_row, c + offset_col) from multiple cells, so
                            # add up each individual probabilities at each iteration
                            dp2[r + offset_row][c + offset_col] += val / 8

            dp = dp2

            print(f'  dp2')
            [print(f'  {row}') for row in dp2]
            print()

        print(f'dp')
        [print(row) for row in dp]
        print()

        print(list(map(sum, dp)))

        # map(sum, dp) returns sum in each row
        # so the most outer sum() sums the sum of probabilities in each row into a single scaler
        return sum(map(sum, dp))


"""
- Time is O(n^2 * k) because for each k step, iterate n^2 chessboard
- Space is O(n^2) for the dynamic programming matrix
"""


n = 3
k = 2
row = 0
column = 0
print(Solution().knightProbability(n, k, row, column))




