from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for row in range(1, len(triangle)):
            for col in range(row + 1):

                # Left edge
                if col == 0:
                    triangle[row][col] = triangle[row][col] + triangle[row - 1][col]

                # Right edge
                elif col == len(triangle[row]) - 1:
                    triangle[row][col] = triangle[row][col] + triangle[row - 1][col - 1]

                # otherwise, middle
                else:
                    triangle[row][col] = min(
                        triangle[row][col] + triangle[row - 1][col - 1],
                        triangle[row][col] + triangle[row - 1][col]
                    )

        return min(triangle[len(triangle) - 1])


"""
In-place bottom-up dynamic programming approach
Time: O(mn) by letting m be the number of length triangle, and n be the bottom lenght triangle
Space: O(1) because it's inplace
"""



triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
triangle = [[-10]]
print(Solution().minimumTotal(triangle))
