from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        row_min_max = float("-inf")

        for r in range(len(matrix)):
            row_min = min(matrix[r])
            row_min_max = max(row_min_max, row_min)

        col_max_min = float("inf")
        for c in range(len(matrix[0])):
            col_max = max(matrix[r][c] for r in range(len(matrix)))
            col_max_min = min(col_max_min, col_max)

        if row_min_max == col_max_min:
            return [row_min_max]
        else:
            return []

    def luckyNumbers1(self, matrix: List[List[int]]) -> List[int]:
        min_rows = [0] * len(matrix)
        max_cols = [0] * len(matrix[0])

        for r in range(len(matrix)):
            min_rows[r] = min(matrix[r])
            for c in range(len(matrix[0])):
                if matrix[r][c] > max_cols[c]:
                    max_cols[c] = matrix[r][c]

        ans = []
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == min_rows[r] and matrix[r][c] == max_cols[c]:
                    ans.append(matrix[r][c])

        return ans
