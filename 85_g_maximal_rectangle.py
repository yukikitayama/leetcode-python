from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        max_area = 0

        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        # print('DP')
        # [print(row) for row in dp]

        for i in range(len(matrix)):

            for j in range(len(matrix[0])):

                # If not 1, no need to calculate area
                if matrix[i][j] == '0':
                    continue

                # If j means if j >= 1, meaning do this summation from the second column,
                # because the first column does not have the previous
                # width is current row col location's so far max width
                width = dp[i][j] = dp[i][j - 1] + 1 if j else 1

                for k in range(i, -1, -1):
                    # dp[k][j] contains max width of the kth row
                    width = min(width, dp[k][j])
                    max_area = max(max_area, width * (i - k + 1))

        return max_area


"""
Time complexity
Let n be the number of rows and m be the number columns
In the most inner for loop takes O(n) to get maximum area for one point,
and we need to do this for every cell in the matrix taking O(nm)
so O(n * nm) = o(n**2m)

Space complexity
We allocate matrix with the same row and column length for dynamic programming,
so O(nm)
"""


matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(Solution().maximalRectangle(matrix))

