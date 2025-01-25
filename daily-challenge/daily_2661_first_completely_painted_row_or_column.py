from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:

        # From mat, number to (r, c)
        mat_to_pos = {}
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                mat_to_pos[mat[r][c]] = (r, c)

        # row_count size row, col_count size col
        row_count = [0] * len(mat)
        col_count = [0] * len(mat[0])

        # Scan arr
        for i in range(len(arr)):
            r, c = mat_to_pos[arr[i]]

            row_count[r] += 1
            col_count[c] += 1

            # If current row_count = col size, or col_count = row size, return arr index
            if row_count[r] == len(mat[0]) or col_count[c] == len(mat):
                return i
