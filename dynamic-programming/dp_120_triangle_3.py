"""
- Assume I can modify triangle in place
- Iterate each row from 1 to the end of the row in triangle
  - If column is 0, current row[i] = current row[i] + previous row[i]
  - If column is the end of the column in triangle, current row[i] = current row[i] + previous row[i - 1]
    - End index is the current row index
  - Else, current row[i] = current row[i] + min(previous row[i - 1], previous row[i])
- return min(the last row in triangle)
"""


from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for row in range(1, len(triangle)):
            for col in range(row + 1):

                if col == 0:
                    triangle[row][col] = triangle[row][col] + triangle[row - 1][col]

                elif col == row:
                    triangle[row][col] = triangle[row][col] + triangle[row - 1][col - 1]

                else:
                    triangle[row][col] = triangle[row][col] + min(
                        triangle[row - 1][col - 1],
                        triangle[row - 1][col]
                    )

        return min(triangle[-1])



triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
triangle = [[-10]]
print(Solution().minimumTotal(triangle))



