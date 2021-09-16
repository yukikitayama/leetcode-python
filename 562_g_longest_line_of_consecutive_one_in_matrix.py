from typing import List


class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        if len(mat) == 0:
            return 0

        # Initialize answer
        ones = 0

        # Horizontal
        for row in range(len(mat)):
            # By reseting count here, only getting horizontal row count of ones
            count = 0
            for col in range(len(mat[0])):
                if mat[row][col] == 1:
                    count += 1
                    ones = max(ones, count)
                else:
                    count = 0

        # Vertical
        for col in range(len(mat[0])):
            count = 0
            for row in range(len(mat)):
                if mat[row][col] == 1:
                    count += 1
                    ones = max(ones, count)
                else:
                    count = 0

        # Upper diagonal
        for i in range(min(len(mat), len(mat[0]))):
            count = 0
            # i: 0
            # [row: 0, col: 0], [row: 1, col: 1], [row: 2, col: 2], ...
            # i: 1
            # [row: 0, col: 1], [row: 1, col: 2], [row: 2, col: 3]
            for row, col in zip(range(0, len(mat)), range(i, len(mat[0]))):
                if mat[row][col] == 1:
                    count += 1
                    ones = max(ones, count)
                else:
                    count = 0

        # When i = 0, upper diagonal and lower diagonal are the same

        # Lower diagonal
        for i in range(min(len(mat), len(mat[0]))):
            count = 0
            # i: 0
            # [row: 0, col: 0], [row: 1, col: 1], [row: 2, col: 2], ...
            # i: 1
            # [row: 1, col: 0], [row: 2, col: 1], [row: 3, col: 2], ...
            for row, col in zip(range(i, len(mat)), range(0, len(mat[0]))):
                if mat[row][col] == 1:
                    count += 1
                    ones = max(ones, count)
                else:
                    count = 0

        # Upper anti-diagonal
        for i in range(min(len(mat), len(mat[0]))):
            count = 0
            for row, col in zip(range(0, len(mat)), range(len(mat[0]) - i - 1, -1, -1)):
                if mat[row][col] == 1:
                    count += 1
                    ones = max(ones, count)
                else:
                    count = 0

        # Lower anti-diagonal
        for i in range(min(len(mat), len(mat[0]))):
            count = 0
            for row, col in zip(range(i, len(mat)), range(len(mat[0]) - 1, -1, -1)):
                if mat[row][col] == 1:
                    count += 1
                    ones = max(ones, count)
                else:
                    count = 0

        return ones


mat = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]
mat = [[1,1,1,1],[0,1,1,0],[0,0,0,1]]
mat = [[0,0,0],[0,1,0],[0,0,0]]
print(Solution().longestLine(mat))
