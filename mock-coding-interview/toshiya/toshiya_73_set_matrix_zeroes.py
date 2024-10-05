"""
2 scans
Hashset
  row index hashset
  col index hash
  if current row index in the row hash or current col index in col hash:
    inplace modify to 0
T: O(2MN)
S: O(M + N)

T: O(MN * (M + N)) = 200 * 200 * (400) = 16,000,000
S: O(1)
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        def update(r, c):
            for i in range(len(matrix[0])):
                if matrix[r][i] != 0:
                    matrix[r][i] = "#"

            for i in range(len(matrix)):
                if matrix[i][c] != 0:
                    matrix[i][c] = "#"

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    update(r, c)

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == "#":
                    matrix[r][c] = 0

    def setZeroes1(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if (r in rows or c in cols) and matrix[r][c] != 0:
                    matrix[r][c] = 0
