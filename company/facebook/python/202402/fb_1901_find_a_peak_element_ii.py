"""
if a row
  binary search
    if nums[mid] < nums[mid + 1]
      search right
      left = mid + 1
    else:
      right = mid
      because mid element could be peak

First binary search horizontally,
  Second binary search to the column which contains the peak found by the first binary search
"""

from typing import List


class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:

        def find_max_row(col):
            max_ = float("-inf")
            row = -1
            for i in range(len(mat)):
                if mat[i][col] > max_:
                    max_ = mat[i][col]
                    row = i
            return row

        left_col = 0
        right_col = len(mat[0]) - 1

        while left_col <= right_col:

            mid_col = (left_col + right_col) // 2
            row = find_max_row(mid_col)

            left_num = -1
            right_num = -1

            if 0 <= mid_col - 1:
                left_num = mat[row][mid_col - 1]

            if mid_col + 1 < len(mat[0]):
                right_num = mat[row][mid_col + 1]

            if left_num < mat[row][mid_col] and mat[row][mid_col] > right_num:
                return [row, mid_col]

            # Reduce search by binary search
            elif left_num > mat[row][mid_col]:
                right_col = mid_col - 1
            else:
                left_col = mid_col + 1

    def findPeakGrid1(self, mat: List[List[int]]) -> List[int]:
        start_col = 0
        end_col = len(mat[0]) - 1

        while start_col <= end_col:

            max_row = 0

            mid_col = (start_col + end_col) // 2

            for row in range(len(mat)):

                if mat[row][mid_col] >= mat[max_row][mid_col]:
                    max_row = row

            if start_col <= mid_col - 1 and mat[max_row][mid_col - 1] > mat[max_row][mid_col]:
                left_is_big = True
            else:
                left_is_big = False

            if mid_col + 1 <= end_col and mat[max_row][mid_col] < mat[max_row][mid_col + 1]:
                right_is_big = True
            else:
                right_is_big = False

            if not left_is_big and not right_is_big:
                return [max_row, mid_col]
            elif right_is_big:
                start_col = mid_col + 1
            else:
                end_col = mid_col - 1

        return []
