"""
- Modify given array in place by summing current and previous
- Get min value of the bottom row
"""


from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for row in range(1, len(triangle)):
            for col in range(len(triangle[row])):
                smallest_above = float('inf')
                if col > 0:
                    smallest_above = triangle[row - 1][col - 1]
                # -1 because this col is used for index of previous row, which is 1 length shorter
                if col < len(triangle[row]) - 1:
                    smallest_above = min(smallest_above, triangle[row - 1][col])
                # += because it's cumulative sum
                triangle[row][col] += smallest_above

        return min(triangle[-1])


if __name__ == '__main__':
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    # 11
    triangle = [[-10]]
    # -10
    print(Solution().minimumTotal(triangle))
