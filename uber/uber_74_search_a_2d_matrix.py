"""
- Binary search 2 times
  - First apply binary search to the first column, to know which row we should go
  - Second, apply binary search to actually find the target
  - Time O(logn)

- Index in the virtual array is transformed into row and column index by
  - row = idx // n
  - col = idx % n
- Do binary search over the indices in the virtual array
  - Convert the index to row and column
  - Do binary search comparison to find the target
  - Update left and right
"""


from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        # -1 because otherwise it will be out of boundary
        right = m * n - 1

        while left <= right:

            mid = left + (right - left) // 2
            row = mid // n
            col = mid % n
            curr = matrix[row][col]

            if curr == target:
                return True
            elif curr > target:
                right = mid - 1
            else:
                left = mid + 1

        return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
print(Solution().searchMatrix(matrix, target))

m = 2
n = 3
for i in range(m * n):
    print(f'i: {i}, i // n: {i // n}, i % n: {i % n}, i // m: {i // m}')
