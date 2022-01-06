from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        def search_rec(left, up, right, down):
            # Base case 1
            # Empty matrix
            if left > right or up > down:
                return False

            # Base case 2
            # If target is smaller than top-left corner smallest element
            # of if target is larger than bottom-right corner largest element,
            # target won't be in the rectangle
            elif target < matrix[up][left] or target > matrix[down][right]:
                return False

            mid = left + (right - left) // 2

            row = up
            # Keep incrementing row as long as row index in the boundary
            # locate row such that matrix[row - 1][mid] < target < matrix[row][mid]
            while row <= down and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1

            # Function is search_rec(left, up, right, down)
            # search_rec(left, row, mid - 1, down) is bottom-left corner
            # search_rec(mid + 1, up, right, row - 1) is top-right corner
            return search_rec(left, row, mid - 1, down) or search_rec(mid + 1, up, right, row - 1)

        # len(matrix[0]) - 1 is the rightmost column index
        # len(matrix) - 1 is the bottom row index
        return search_rec(0, 0, len(matrix[0]) - 1, len(matrix) - 1)


if __name__ == '__main__':
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]]
    target = 5
    print(Solution().searchMatrix())
